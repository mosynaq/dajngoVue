<template>
  <div id="app">
    <sui-menu :attached="true" :borderless="true">
      <sui-menu-item position="left" :link="true" :icon="true">
        <sui-icon name="bars"/>
      </sui-menu-item>
      <sui-menu-item position="right" :link="true">
        <sui-icon name="left angle"/>
      </sui-menu-item>
      <sui-menu-item :link="true">
        <sui-icon name="right angle"/>
      </sui-menu-item>
    </sui-menu>

    <sui-container class="main-container">
      <books :items="worksOfArt"></books>
    </sui-container>
  </div>
</template>

<script>

import Vue from "vue";
import SuiVue from "semantic-ui-vue";
import axios from "axios";
import VueAxios from "vue-axios";
import books from "./components/Books.vue";

Vue.use(SuiVue);
Vue.use(VueAxios, axios);


export default {
  name: "app",
  components: {
    // SuiVue,
    books,
  },
  data() {
    return {
      worksOfArt: null,
      worksOfArtPrevPage: null,
      worksOfArtNextPage: null,
    }
  },
  mounted() {
    axios
        .get('http://127.0.0.1:8000/api/works-of-art/?format=json')
        .then(response => {
          this.worksOfArt = response.data.results;
          this.worksOfArtPrevPage = response.data.previous;
          this.worksOfArtNextPage = response.data.next;
        })
  }
};
</script>

<style lang="scss">
.main-container {
  padding-top: 2em;
}
</style>
