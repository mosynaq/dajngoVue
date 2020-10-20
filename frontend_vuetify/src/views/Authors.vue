<template lang="html">
  <v-container>
    <v-row>
      <v-col
        class="col-sm-6 col-md-4 col-12"
        v-for="author in authors"
        :key="author.id"
      >
        <Author
          :id="author.id"
          :first_name="author.first_name"
          :last_name="author.last_name"
          :date_of_birth="author.date_of_birth"
          :bio="author.bio"
        ></Author>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import config from "../../config.json";
import Author from "../components/Author.vue";
// import author_placeholder from "../components/AuthorPlaceholder.vue";
import axios from "axios";
// import VueQueryBuilder from "vue-query-builder";

export default {
  name: "authors",
  components: {
    Author
    // author_placeholder,
    // VueQueryBuilder
  },
  data() {
    return {
      authors: null,
      nextPageUrl: null,
      prevPageUrl: null,
      rules: [
        {
          type: "text",
          id: "first_name",
          label: "First Name"
        },
        {
          type: "text",
          id: "last_name",
          label: "Last Name"
        },
        {
          type: "text",
          id: "date_of_birth",
          label: "Date of Birth"
        },
        {
          type: "text",
          id: "bio",
          label: "Biography"
        }
      ],
      query: {},

      open: false
    };
  },
  mounted() {
    this.goToPage(config.api_authors_url);
  },
  methods: {
    goToPage(url) {
      axios.get(url).then(response => {
        this.authors = response.data.results;
        this.nextPageUrl = response.data.next;
        this.prevPageUrl = response.data.previous;
      });
    },
    goToNextPage() {
      this.goToPage(this.nextPageUrl);
    },
    goToPrevPage() {
      this.goToPage(this.prevPageUrl);
    },

    toggle() {
      this.open = !this.open;
    }
  }
};
</script>

<style scoped></style>
