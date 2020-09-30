<template>
  <div>
    <sui-card-group :stackable="true" class="centered doubling" v-if="authors">
      <author v-for="author in authors" :key="author.id"
              :first_name="author.first_name" :last_name="author.last_name"
              :date_of_birth="author.date_of_birth" :bio="author.bio"/>
    </sui-card-group>
    <div v-else>
      <sui-card-group :stackable="true" class="centered doubling">
        <p v-for="i in 6" :key="i">no authors yet</p>
      </sui-card-group>
    </div>
  </div>
</template>

<script>
import config from "../../config.json";
import author from "./Author.vue";
import axios from "axios";

export default {
  name: "authors",
  components: {
    author
  },
  data() {
    return {
      authors: null,
    }
  },
  mounted() {
    axios.get(config.api_authors_url)
        .then(response => {
              this.authors = response.data.results;
            }
        )
  },
  props: {}
}
</script>

<style scoped>

</style>