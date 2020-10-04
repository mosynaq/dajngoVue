import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import authors from "../views/Authors";
import books from "../views/WorksOfArt.vue";
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
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () =>
    //   import(/* webpackChunkName: "about" */ "../views/worksofart.vue")
    component: books
  },
  {
    path: "/worksofart/:id/",
    name: "works_of_art_single",
    component: books
  },
  {
    path: "/authors/",
    name: "authors",
    component: authors
  },
  {
    path: "/authors/:id/",
    name: "author_single",
    component: author_single
  }
];

const router = new VueRouter({
  routes
});

export default router;
