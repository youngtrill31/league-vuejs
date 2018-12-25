// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import VeeValidate from 'vee-validate';
import App from './App';
import router from './router';
import Home from './components/Home';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(VeeValidate);

// export const serverBus = new Vue();

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App, Home },
  template: '<App/>',
});
