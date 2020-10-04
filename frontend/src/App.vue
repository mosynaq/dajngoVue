<template>
  <div id="app">
    <sui-menu fixed="top" :borderless="true" :inverted="true">
      <router-link class="item" to="/" active-class="active" exact>
        <sui-icon name="home" />
      </router-link>
      <router-link class="item" to="/worksofart/" active-class="active">
        <sui-icon name="book" />
        Works of Art
      </router-link>

      <router-link class="item" to="/authors/" active-class="active">
        <sui-icon name="user" />
        Authors
      </router-link>

      <sui-menu-item
        position="right"
        :link="previousPaginationEnabled"
        :disabled="!previousPaginationEnabled"
        @click="goToPreviousPage()"
      >
        <sui-icon name="left angle" />
      </sui-menu-item>
      <sui-menu-item
        :link="nextPaginationEnabled"
        :disabled="!nextPaginationEnabled"
        @click="goToNextPage()"
      >
        <sui-icon name="right angle" />
      </sui-menu-item>
    </sui-menu>
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import SuiVue from "semantic-ui-vue";
import axios from "axios";
import VueAxios from "vue-axios";
import VueMoment from "vue-moment";

Vue.use(SuiVue);
Vue.use(VueMoment);
Vue.use(VueAxios, axios);

export default {
  name: "app",
  components: {
    // books,
    // hello
  },
  data() {
    return {
      authors: null,
      booksLoaded: true
    };
  },
  methods: {
    goToPage(url) {
      axios.get(url).then(response => {
        this.worksOfArt = response.data.results;
        this.worksOfArtPrevPage = response.data.previous;
        this.worksOfArtNextPage = response.data.next;
      });
    },
    goToNextPage() {
      this.goToPage(this.worksOfArtNextPage);
    },
    goToPreviousPage() {
      this.goToPage(this.worksOfArtPrevPage);
    }
  },

  computed: {
    previousPaginationEnabled: function() {
      return this.worksOfArtPrevPage !== null;
    },
    nextPaginationEnabled: function() {
      return this.worksOfArtNextPage !== null;
    }
  }
};
</script>

<style lang="scss">
.main-content {
  padding-top: 4em;
}
</style>
