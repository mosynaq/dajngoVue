<template>
  <div id="app">
    <sui-menu fixed="top" :borderless="true" :inverted="true">
      <router-link class="item" to="/" active-class="active" exact>
        <sui-icon name="home" />
      </router-link>
      <router-link class="item" to="worksofart" active-class="active">
        <sui-icon name="book" />
        Works of Art
      </router-link>

      <router-link class="item" to="authors" active-class="active">
        <sui-icon name="user" />
        Authors
      </router-link>

      <sui-menu-item position="right">
        <sui-icon name="left angle" />
      </sui-menu-item>
      <sui-menu-item>
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
import filters from "./filters";

Vue.use(SuiVue);
Vue.use(VueMoment);
Vue.use(VueAxios, axios);
Vue.use(filters);

export default {
  name: "app",
  components: {},
  methods: {},
  data() {
    return {};
  }
};
</script>

<style lang="scss">
.main-content {
  padding-top: 4em;
}
</style>
