import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import authors from "../components/Authors";
import books from "../components/Books.vue";
import hello from "../components/hello.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: hello
    },
    {
        path: "/worksofart/",
        name: "Works of Art",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        // component: () =>
        //   import(/* webpackChunkName: "about" */ "../views/worksofart.vue")
        component: books
    },
    {
        path: "/worksofart/:id/",
        name: "A single Work of Art",
        component: books

    },
    {
        path: "/authors/",
        name: "Authors",
        component: authors
    }
];

const router = new VueRouter({
    routes
});

export default router;
