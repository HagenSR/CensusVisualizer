<template>
  <v-app>
     <v-toolbar color="orange accent-1">
    <v-app-bar-nav-icon class="hidden-sm-and-down"></v-app-bar-nav-icon>
    <v-toolbar-title class="title mr-6 hidden-sm-and-down">Cryptocurrency</v-toolbar-title>
    <v-autocomplete
      v-model="model"
      :items="items"
      :loading="loading"
      :search-input.sync="search"
      chips
      clearable
      hide-details
      hide-selected
      item-text="county"
      item-value="countryid"
      label="Search for a county"
      prepend-icon="mdi-database-search"
      return-object
      solo
    >
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            Search for your favorite
            <strong>County</strong>
          </v-list-item-title>
        </v-list-item>
      </template>
      <template v-slot:selection="{ attr, on, item, selected }">
        <v-chip
          v-bind="attr"
          :input-value="selected"
          color="blue-grey"
          class="white--text"
          v-on="on"
        >
          <v-icon left>mdi-coin</v-icon>
          <span v-text="item.county"></span>
        </v-chip>
      </template>
      <template v-slot:item="{ item }">
        <v-list-item-avatar
          color="indigo"
          class="headline font-weight-light white--text"
        >
          {{ item.county.charAt(0) }}
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.county"></v-list-item-title>
          <v-list-item-subtitle v-text="item.countryid"></v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-icon>mdi-coin</v-icon>
        </v-list-item-action>
      </template>
    </v-autocomplete>
  </v-toolbar>
    <county  v-if="model" :id="model.countryid"></county>
  </v-app>
</template>
<script>
const serve = require("./../functionsInteraction.js");
import County from "./County";
export default {
  name: "Search",
  components: {
    County
  },
  data() {
    return {
      loading: false,
      items: [],
      names: [],
      search: null,
      select: null,
      model: null,
    }
  },
  watch: {
    search(val) {
      val && val !== this.select && this.querySelections(val);
      
    }
  },
  methods: {
    querySelections(v) {
      this.loading = true;
      // Simulated ajax query
      setTimeout(() => {
        serve.getCounty(v).then(e => {
          this.items = e;
          this.loading = false;
          console.log(e)
        });
      }, 1000);
    },
  }
}
</script>