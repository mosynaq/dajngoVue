<template>
  <sui-grid :columns="2" :padded="true">
    <sui-grid-column :width="4">
      <vue-query-builder :rules="rules"></vue-query-builder>
    </sui-grid-column>

    <sui-grid-column :width="12">
      <sui-container>
        <sui-card-group
            :stackable="true"
            class="centered doubling"
            v-if="authors"
        >
          <author
              v-for="author in authors"
              :key="author.id"
              :first_name="author.first_name"
              :last_name="author.last_name"
              :date_of_birth="author.date_of_birth"
              :bio="author.bio"
          />
        </sui-card-group>
        <div v-else>
          <sui-card-group :stackable="true" class="centered doubling">
            <author_placeholder v-for="i in 6" :key="i"/>
          </sui-card-group>
        </div>
      </sui-container>
    </sui-grid-column>
  </sui-grid>
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
      rules: [
        {
          type: "text",
          id: "first_name",
          label: "First Name",
        },
        {
          type: "text",
          id: "last_name",
          label: "Last Name",
        },
        {
          type:"text",
          id:"date_of_birth",
          label: "Date of Birth"
        },
        {
          type: "text",
          id: "bio",
          label: "Biography",
        },
      ]
    };
  },
  mounted() {
    axios.get(config.api_authors_url).then(response => {
      this.authors = response.data.results;
    });
  },
  props: {}
};
</script>

<style scoped></style>
