<template>
  <div>
      <h1>{{info.County}}, {{info.State}}</h1>
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
              <td>{{info.TotalPop.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>Voting Age Population:</h2>
              </td>
              <td>{{info.VotingAgeCitizen.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>People Employed:</h2>
              </td>
              <td>{{info.Employed.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>GDP per capita:</h2>
              </td>
              <td>{{info.IncomePerCap.toLocaleString()}}</td>
            </tr>
            <tr>
              <td>
                <h2>Poverty:</h2>
              </td>
              <td>{{parseFloat(info.Poverty).toFixed(2)+"%"}}</td>
            </tr>
            <tr>
              <td>
                <h2>Child Poverty</h2>
              </td>
              <td>{{parseFloat(info.ChildPoverty).toFixed(2)+"%"}}</td>
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
    id: String
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
      console.log(e)
      this.info = e[0];
      this.genderSeries.push(parseInt(this.info.Men));
      this.genderSeries.push(parseInt(this.info.Women));
      this.transportSeries.push(parseInt(this.info.Drive));
      this.transportSeries.push(parseInt(this.info.Carpool));
      this.transportSeries.push(parseInt(this.info.Transit));
      this.transportSeries.push(parseInt(this.info.Walk));
      this.transportSeries.push(parseInt(this.info.OtherTransp));
      this.workSeries.push(parseInt(this.info.PrivateWork));
      this.workSeries.push(parseInt(this.info.PublicWork));
      this.workSeries.push(parseInt(this.info.SelfEmployed));
      this.workSeries.push(parseInt(this.info.FamilyWork));
      this.workSeries.push(parseInt(this.info.Unemployment));
      this.typeSeries.push(parseInt(this.info.Professional));
      this.typeSeries.push(parseInt(this.info.Service));
      this.typeSeries.push(parseInt(this.info.Office));
      this.typeSeries.push(parseInt(this.info.Construction));
      this.typeSeries.push(parseInt(this.info.Production));
      this.demoSeries.push(parseInt(this.info.White));
      this.demoSeries.push(parseInt(this.info.Hispanic));
      this.demoSeries.push(parseInt(this.info.Black));
      this.demoSeries.push(parseInt(this.info.Native));
      this.demoSeries.push(parseInt(this.info.Asian));
      this.demoSeries.push(parseInt(this.info.Pacific));
    }
  },
  created: function() {
    this.loading = false;
    serve.getByID(this.id).then(e => this.setup(e));
    this.loading = true;
  }
};
</script>