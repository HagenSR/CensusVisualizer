<template>
  <div>
      <h1>{{info.county}}, {{info.usstate}}</h1>
      <v-simple-table v-show="loading">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Name</th>
              <th class="text-left">Number</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <h2>Total Population:</h2>
              </td>
              <td>{{info.totalpop.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>Voting Age Population:</h2>
              </td>
              <td>{{info.votingagecitizen.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>People Employed:</h2>
              </td>
              <td>{{info.employed.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>GDP per capita:</h2>
              </td>
              <td>{{info.incomepercap.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>Poverty:</h2>
              </td>
              <td>{{parseFloat(info.poverty).toFixed(2)+"%"}}</td>
            </tr>
            <tr>
              <td>
                <h2>Child Poverty</h2>
              </td>
              <td>{{parseFloat(info.childpoverty).toFixed(2)+"%"}}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-tabs v-model="tab" grow>
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
          <VueApexCharts width="500px" type="donut" :options="genderOptions" :series="genderSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width="500px" type="donut" :options="demoOptions" :series="demoSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts
            width="500px"
            type="donut"
            :options="transportOptions"
            :series="transportSeries"
          ></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width="500px" type="donut" :options="workOptions" :series="workSeries"></VueApexCharts>
        </v-tab-item>
        <v-tab-item>
          <VueApexCharts width="500px" type="donut" :options="typeOptions" :series="typeSeries"></VueApexCharts>
        </v-tab-item>
      </v-tabs-items>
  </div>
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
    id: Number
  },
  data: () => ({
    tab: null,
    loading: true,
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
  created: function() {
    this.loading = false;
    serve.getByID(this.id).then(e => this.setup(e));
    this.loading = true;
  }
};
</script>