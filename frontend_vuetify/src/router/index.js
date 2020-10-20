import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import authors from "../views/Authors";
import WorksOfArt from "../views/WorksOfArt.vue";
import WorkOfArtSingle from "../views/WorkOfArtSingle.vue";
import home from "../views/home.vue";
import author_single from "../views/AuthorSingle";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home
  },
  {
    path: "/worksofart/",
    name: "worksofart",
    component: WorksOfArt
  },
  {
    path: "/worksofart/:id/",
    name: "WorksOfArtSingle",
    component: WorkOfArtSingle
  },
  {
    path: "/authors/",
    name: "authors",
    component: authors
  },
  {
    path: "/authors/:id/",
    name: "authorSingle",
    component: author_single
  }
];

const router = new VueRouter({
  routes
});

export default router;
