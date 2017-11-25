<template>
<div>
<b-nav fill pills>
	<b-nav-item v-on:click="toggleSub" class = "hover-element"><img v-bind:class="{iconactive: !isSubHidden }" :src="'./src//assets/grid-icon.png'"></b-nav-item>
  <b-nav-item class= "hover-element" v-for='category in categories' :key='category.id' id = ""> {{category.name}}</b-nav-item>
</b-nav>

<b-container v-bind:class="{menuActive: isSubHidden }">
<b-row>
  <b-col>
  <b-form inline>
      <label class="sr-only" for="inlineFormInputGroupUsername2">Email</label>
      <b-input-group left="@" class="mb-2 mr-sm-2 mb-sm-0">
        <b-input id="inlineFormInputGroupUsername2" placeholder="Username" />
      </b-input-group>
      <b-input-group left="Password" class="mb-2 mr-sm-2 mb-sm-0">
      <b-form-input type="password"></b-form-input>
      </b-input-group>
      
      <b-button variant="primary">LogIn</b-button>
    </b-form>
  </b-col>
</b-row>

</b-container>


  


</div>
</template>


<script>
  export default {
    name: 'menubar',
    data () {
      return {
        isSubHidden: true,
        // Placeholder object with a few articles.
        categories: {
          category1: {id: 0, name: 'Category1'},
          category2: {id: 1, name: 'Category2'},
          category3: {id: 2, name: 'Category3'}
        }
      }
    },
    methods: {
      toggleSub: function (event) {
        this.isSubHidden = !this.isSubHidden
      }
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
	background: #a5a5a5;
  padding-top: 1.5em;
  padding-bottom: 1em;
  font-size: 18pt;
}

.hover-element > a{
  color: black;
}

.hover-element:hover{
	background-color: #328afc;
}

.hover-element:hover > a{
	color: white;
}


.menuActive{
  display: none;
}

.iconactive{
  transform: rotate(45deg);
}


.menu-img:hover{
  transform: rotate(45deg);
}


</style>



