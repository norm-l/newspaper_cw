<template>
  <div id="app">
    <menubar></menubar>
    <articles></articles>
  </div>
</template>

<script>
import articles from './components/articles'
import menubar from './components/menu'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-material-design-icons/styles.css'

Vue.use(BootstrapVue)
export default {
  name: 'app',
  components: {
    menubar,
    articles
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
