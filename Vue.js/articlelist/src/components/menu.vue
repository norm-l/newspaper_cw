<template>
<div>
<b-nav fill pills>
	<a href = ""><b-nav-item class = "hover-element"><img :src="'./src//assets/grid-icon.png'"></b-nav-item></a>
    <b-nav-item href = "" class= "hover-element" v-for='category in categories' :key='category.id'> {{category.name}}</b-nav-item>
</b-nav>


</div>
</template>


<script>
  export default {
    name: 'menubar',
    data () {
      return {
        title: 'menu',
        // Placeholder object with a few articles.
        categories: {
          category1: {id: 0, name: 'Category1'},
          category2: {id: 1, name: 'Category2'},
          category3: {id: 2, name: 'Category3'}
        }
      }
    },
    methods: {
    }
  }
</script>

<style scoped>

.top-menu {
    width: 100vw;
}

.st {
    position: fixed;
    z-index: 200;
}

.flex-grow {
    flex: 1;
}

.test{
	background-color: black;
}


.hover-element{
	display: inline-block;
	padding: 1rem;
	background: #2c3e50;
}

.hover-element:hover{
	background-color: darkblue;
}


</style>



