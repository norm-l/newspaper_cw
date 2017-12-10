<template>
  <div id="app">
    <menubar :cat="category" @categoryChanged="category = $event"></menubar>
    <articles :cat="category"></articles>
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
import 'vue-awesome/icons'
import VueSession from 'vue-session'

Vue.use(VueSession)
Vue.use(BootstrapVue)


export default {
  name: 'app',
  components: {
    menubar,
    articles
  },
  data: function(){
    return{
      category: "Home"
    }
  },
  methods:{
    
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
