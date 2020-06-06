<template>
  <v-container fluid style="margin: 0px; padding: 0px; width: 100%">
    <v-app>
      <Search></Search>
    </v-app>
  </v-container>
</template>


<script>
import Search from "./components/Search";

export default {
  name: "App",

  components: {
    Search
  },

  data: () => ({
    //
  })
};
</script>
