<template lang="html">
  <v-card elevation="2">
    <v-card-title>Cafe Badilico</v-card-title>
  </v-card>
</template>

<script>
import config from "../../config.json";
// import author from "../components/Author.vue";
// import author_placeholder from "../components/AuthorPlaceholder.vue";
import axios from "axios";
// import VueQueryBuilder from "vue-query-builder";

export default {
  name: "authors",
  components: {
    // author,
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
