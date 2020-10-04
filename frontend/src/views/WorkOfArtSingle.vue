<template>
  <sui-container :text="true">
    <sui-segment v-if="this.author">
      <sui-header>
        {{ this.title }}
        <sui-header-subheader>
          by {{ this.author.last_name + ", " + this.author.first_name }}
        </sui-header-subheader>
      </sui-header>
      <p class="linebreaks">{{ this.description }}</p>
    </sui-segment>
    <sui-segment v-else>
      <div class="ui fluid placeholder">
        <div class="header">
          <div class="short line"></div>
          <div class="very short line"></div>
        </div>
        <div class="paragraph">
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
          <div class="line"></div>
        </div>
      </div>
    </sui-segment>
  </sui-container>
</template>

<script>
import axios from "axios";
import config from "../../config.json";

export default {
  name: "WorkOfArtSingle",
  data() {
    return {
      title: null,
      price: null,
      rating: null,
      description: null,
      image: null,
      type: null,
      author: null
    };
  },
  methods: {
    getSingleWorkOfArt(id) {
      let url = new URL(config.api_worksOfArt_url);
      url.pathname += id + "/";

      axios.get(url.toString()).then(response => {
        this.title = response.data.title;
        this.price = response.data.price;
        this.rating = response.data.rating;
        this.description = response.data.description;
        this.image = response.data.image;
        this.type = response.data.type;
        this.author = response.data.author;
      });
    }
  },
  mounted() {
    let id = this.$route.params.id;
    this.getSingleWorkOfArt(id);
  },
  watch: {
    $route(to) {
      this.getSingleWorkOfArt(to.params.id);
    }
  }
};
</script>

<style scoped>
.linebreaks {
  white-space: pre-wrap;
}
</style>
