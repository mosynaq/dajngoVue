<template>
  <sui-container :text="true">
    <sui-segment>
      <sui-header>
        {{ this.last_name + ", " + this.first_name }}
        <sui-header-subheader>
          born {{ this.date_of_birth }}
        </sui-header-subheader>
      </sui-header>
      <p class="linebreaks">{{ this.bio }}</p>
    </sui-segment>
  </sui-container>
</template>

<script>
import axios from "axios";
import config from "../../config.json";

export default {
  name: "author_single",
  data() {
    return {
      first_name: null,
      last_name: null,
      date_of_birth: null,
      bio: null
    };
  },
  methods: {
    getSingleAuthor(id) {
      let url = new URL(config.api_authors_url);
      url.pathname += id + "/";

      axios.get(url.toString()).then(response => {
        this.first_name = response.data.first_name;
        this.last_name = response.data.last_name;
        this.date_of_birth = response.data.date_of_birth;
        this.bio = response.data.bio;
      });
    }
  },
  mounted() {
    let id = this.$route.params.id;
    this.getSingleAuthor(id);
  },
  watch: {
    $route(to) {
      this.getSingleAuthor(to.params.id);
    }
  }
};
</script>

<style scoped>
.linebreaks {
  white-space: pre-wrap;
}
</style>
