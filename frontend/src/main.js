import Vue from "vue";
import App from "./App.vue";
// import router from "./router";
// import store from "./store";

import "animate.css/animate.css";
import 'semantic-ui-css/semantic.css'; // may need to change the path

Vue.config.productionTip = false;

new Vue({
    // router,
    // store,
    render: h => h(App)
}).$mount("#app");
