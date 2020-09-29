<template>
  <div id="app">
    <sui-menu fixed="top" :borderless="true">
      <sui-menu-item :link="true" :icon="true">
        <sui-icon name="bars"/>
      </sui-menu-item>
      <sui-menu-item>
        <sui-checkbox :toggle="true" v-model="booksLoaded">books ready?</sui-checkbox>
      </sui-menu-item>
      <sui-menu-item position="right" :link="previvusPaginationEnabled" :disabled="!previousPaginationEnabled"
                     @click="goToPreviousPage();">
        <sui-icon name="left angle"/>
      </sui-menu-item>
      <sui-menu-item :link="nextPaginationEnabled" :disabled="!nextPaginationEnabled" @click="goToNextPage();">
        <sui-icon name="right angle"/>
      </sui-menu-item>

    </sui-menu>
    <sui-container class="main-content">
      <books :items="worksOfArt" :booksLoaded="booksLoaded"></books>
    </sui-container>
  </div>
</template>

<script>

import Vue from "vue";
import SuiVue from "semantic-ui-vue";
import axios from "axios";
import VueAxios from "vue-axios";
import books from "./components/Books.vue";

import config from "../config.json"

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
      booksLoaded: true,
      worksOfArt: null,
      worksOfArtPrevPage: null,
      worksOfArtNextPage: null,
    }
  },
  methods: {
    goToPage(url) {
      axios
          .get(url)
          .then(response => {
            this.worksOfArt = response.data.results;
            this.worksOfArtPrevPage = response.data.previous;
            this.worksOfArtNextPage = response.data.next;
          })
    },
    goToNextPage() {
      this.goToPage(this.worksOfArtNextPage)
    },
    goToPreviousPage() {
      this.goToPage(this.worksOfArtPrevPage)
    }
  },
  mounted() {
    axios
        .get(config.api_worksOfArt_url)
        .then(response => {
          this.worksOfArt = response.data.results;
          this.worksOfArtPrevPage = response.data.previous;
          this.worksOfArtNextPage = response.data.next;
        })
  },
  computed: {
    previousPaginationEnabled: function () {
      return this.worksOfArtPrevPage !== null;
    },
    nextPaginationEnabled: function () {
      return this.worksOfArtNextPage !== null;
    }
  }
}
;
</script>

<style lang="scss">
.main-content {
  padding-top: 4em;
}
</style>
