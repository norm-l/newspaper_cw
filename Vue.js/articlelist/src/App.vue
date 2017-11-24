<template>
  <div id="app">
    <articles></articles>
  </div>
</template>

<script>
import articles from './components/articles'
export default {
  name: 'app',
  components: {
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
  margin-top: 60px;
}
</style>
