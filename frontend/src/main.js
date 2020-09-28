import Vue from "vue";
import App from "./App.vue";
// import router from "./router";
// import store from "./store";
// import "bootstrap";
// import {library} from "@fortawesome/fontawesome-svg-core";

// import "bootstrap/dist/css/bootstrap.css";
import "animate.css/animate.css";
import 'semantic-ui-css/semantic.css'; // may need to change the path

Vue.config.productionTip = false;

// import {faShoppingCart, faDollarSign} from "@fortawesome/free-solid-svg-icons";

// library.add(faShoppingCart, faDollarSign);

new Vue({
    // router,
    // store,
    render: h => h(App)
}).$mount("#app");
