import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false
new Vue({
  vuetify,
  VueApexCharts,
  render: h => h(App)
}).$mount('#app')
