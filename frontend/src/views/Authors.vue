<template lang="html">
  <div>
    <sui-modal v-model="open" size="standard">
      <sui-modal-header>Find the Author of Your Choice</sui-modal-header>
      <sui-modal-content scrolling>
        <vue-query-builder :rules="rules" v-if="authors" v-model="query" />
        <!--        <sui-modal-description>-->
        <!--        </sui-modal-description>-->
      </sui-modal-content>
      <sui-modal-actions>
        <sui-button positive @click.native="toggle">
          <sui-icon name="search" />
          Find
        </sui-button>
      </sui-modal-actions>
    </sui-modal>
    <sui-card-group :stackable="true" class="centered doubling" v-if="authors">
      <author
        v-for="author in authors"
        :key="author.id"
        :id="author.id"
        :first_name="author.first_name"
        :last_name="author.last_name"
        :date_of_birth="author.date_of_birth"
        :bio="author.bio"
      />
    </sui-card-group>
    <div v-else>
      <sui-card-group :stackable="true" class="centered doubling">
        <author_placeholder v-for="i in 6" :key="i" />
      </sui-card-group>
    </div>
    <sui-button @click.native="toggle">Show Modal</sui-button>
  </div>
</template>

<script>
import config from "../../config.json";
import author from "../components/Author.vue";
import author_placeholder from "../components/AuthorPlaceholder.vue";
import axios from "axios";
import VueQueryBuilder from "vue-query-builder";

export default {
  name: "authors",
  components: {
    author,
    author_placeholder,
    VueQueryBuilder
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
