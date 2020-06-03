<template>
  <v-app>
    <v-container>
      <h1 v-text="info.usstate">,</h1>
      <h2 v-text="info.county"></h2>
      <h2>Total Population: {{info.totalpop}}</h2>
      <h2>Voting Age Population: {{info.votingagecitizen}}</h2>
      <h2>People Employed: {{info.employed}}</h2>
      <v-tabs v-model="tab">
        <v-tab>
          <h3>Gender</h3>
        </v-tab>
        <v-tab>
          <h3>Demographics</h3>
        </v-tab>
        <v-tab>
          <h3>How people commute</h3>
        </v-tab>
        <v-tab>
          <h3>Who people work for</h3>
        </v-tab>
        <v-tab>
          <h3>What job people work</h3>
        </v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <v-tab-item>
          <VueApexCharts width = 760 type="donut" :options="genderOptions" :series="genderSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width = 760 type="donut" :options="demoOptions" :series="demoSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width = 760 type="donut" :options="transportOptions" :series="transportSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width = 760 type="donut" :options="workOptions" :series="workSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width = 760 type="donut" :options="typeOptions" :series="typeSeries"></VueApexCharts>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </v-app>
</template>

<script>
const serve = require("./../functionsInteraction.js");
import VueApexCharts from "vue-apexcharts";
export default {
  name: "County",
  components: {
    VueApexCharts
  },
  props: {
    id: Number,
  },
  data: () => ({
    tab: null,
    info: [],
    genderSeries: [],
    transportSeries: [],
    workSeries: [],
    typeSeries: [],
    demoSeries: [],
    genderOptions: {
      labels: ["Male", "Female"]
    },
    transportOptions: {
      labels: [
        "Drive",
        "Car Pool",
        "Public Transit",
        "Walk",
        "Other Transportation"
      ]
    },
    workOptions: {
      labels: [
        "Private Work",
        "Public Work",
        "Self Employed",
        "Family Work",
        "Unemployed"
      ]
    },
    typeOptions: {
      labels: [
        "Professional",
        "Service Worker",
        "Office Worker",
        "Construction",
        "Production"
      ]
    },
    demoOptions: {
      labels: [
        "White",
        "Hispanic",
        "Black",
        "Native American",
        "Asian",
        "Pacific"
      ]
    }
  }),
  methods: {
    setup(e) {
      this.info = e[0];
      this.genderSeries.push(this.info.men);
      this.genderSeries.push(this.info.women);
      this.transportSeries.push(this.info.drive);
      this.transportSeries.push(this.info.carpool);
      this.transportSeries.push(this.info.transit);
      this.transportSeries.push(this.info.walk);
      this.transportSeries.push(this.info.othertransp);
      this.workSeries.push(this.info.privatework);
      this.workSeries.push(this.info.publicwork);
      this.workSeries.push(this.info.selfemployed);
      this.workSeries.push(this.info.familywork);
      this.workSeries.push(this.info.unemployment);
      this.typeSeries.push(this.info.professional);
      this.typeSeries.push(this.info.service_worker);
      this.typeSeries.push(this.info.office);
      this.typeSeries.push(this.info.construction);
      this.typeSeries.push(this.info.production);
      this.demoSeries.push(this.info.white);
      this.demoSeries.push(this.info.hispanic);
      this.demoSeries.push(this.info.black);
      this.demoSeries.push(this.info.nativeamerican);
      this.demoSeries.push(this.info.asian);
      this.demoSeries.push(this.info.pacific);
    }
  },
  mounted: function() {
    serve.getByID(this.id).then(e => this.setup(e));
  }
};
</script>