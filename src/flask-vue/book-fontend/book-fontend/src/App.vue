<script setup>
// import HelloWorld from './components/HelloWorld.vue'
import DataShow from './components/DataShow.vue';
import DataAdd from './components/DataAdd.vue';
import DataEdit from './components/DataEdit.vue';
</script>

<template #app>
  <!-- <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" /> -->
  <div id="app">
    <DataAdd></DataAdd>
    <DataShow></DataShow>
    <DataEdit></DataEdit>

  </div>
  
</template>

<style scoped>

</style>
