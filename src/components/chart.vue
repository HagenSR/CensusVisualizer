<template>
<div>
<h1 v-text="ser"></h1>
  
  </div>
</template>
<script>
import VueApexCharts from "vue-apexcharts";
export default {
  components: {
    VueApexCharts
  },
  data: () => ({
    options: {
          labels: ["1991", "1992", "1993", "1994", "1995"]
    },
    series: [1]
  }),
  props: {
     ser: Array
  },
  beforeUpdate: () => {
    this.series = this.ser
    console.log(this.ser)
  }
};
</script>