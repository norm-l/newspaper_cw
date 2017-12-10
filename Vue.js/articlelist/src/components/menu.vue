<template>
  <div>
    <b-nav fill pills>
      <b-nav-item v-on:click="toggleSub" class="hover-element"><img v-bind:class="{iconactive: !isSubHidden }" :src="'static/Newspaper/img/grid-icon.png'"></b-nav-item>
      <b-nav-item class="hover-element" v-for='category in categories' :key='category.id' id="" v-on:click="FilterCategory(category.name)"> {{category.name}}</b-nav-item>
    </b-nav>

    <b-container v-bind:class="{menuActive: isSubHidden }">
      <div v-if="loggedIn">
        <b-row>
          <b-col>
            Email: {{user.email}}
          </b-col>
          <b-col>
            Name: {{user.name}}
          </b-col>
          <b-col>
            Tel: {{user.tel}}
          </b-col>
          <b-col>
            <b-button v-on:click="LogOut" type="button" variant="danger">LogOut</b-button>
          </b-col>
        </b-row>

      </div>
      <div v-else>
        <b-row>
          <b-col>
            <b-form v-on:submit.prevent="LogIn" inline>
              <label class="sr-only" for="inlineFormInputGroupUsername2">Email</label>
              <b-input-group left="@" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input v-model="user.email" id="inlineFormInputGroupUsername2" placeholder="Username" />
              </b-input-group>
              <b-input-group left="Password" class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input v-model="user.password" type="password"></b-form-input>
              </b-input-group>
              <b-button type="submit" variant="primary">LogIn</b-button>
            </b-form>
          </b-col>
          <b-col>
            <b-btn v-b-modal.modalPrevent>Register</b-btn>
          </b-col>

        </b-row>
      </div>

    </b-container>

    <b-modal id="modalPrevent" ref="modal" title="Register" @ok="handleOk" @shown="clearName">
      <form @submit.stop.prevent="handleSubmit">
        <b-form-input type="email" placeholder="Email" v-model="user.email"></b-form-input>
        <b-form-input type="password" placeholder="Password" v-model="user.password"></b-form-input>
        <b-form-input type="text" placeholder="Name" v-model="user.name"></b-form-input>
        <b-form-input type="tel" placeholder="Phone" v-model="user.phone"></b-form-input>
      </form>
    </b-modal>

  </div>
</template>


<script>
import axios from 'axios';
import cookies from 'cookies-js';
var csrftoken = 'not-loaded';

export default {
  name: 'menubar',
  data() {
    return {
      isSubHidden: true,
      loggedIn: false,
      user: { email: "", password: "", name: "", phone: "" },
      // Placeholder object with a few articles.
      categories: {
        category0: {id: 0, name:"Home"},
        category1: { id: 1, name: 'Business' },
        category2: { id: 2, name: 'Politics' },
        category3: { id: 3, name: 'Technology' }
      },
    }
  },
  created() {
    csrftoken = cookies.get('csrftoken');
  },
  props: ['cat'],
  methods: {
    toggleSub: function(event) {
      this.isSubHidden = !this.isSubHidden
    },
    LogIn: function(event) {
      event.preventDefault();

      var config = {headers :
        {'content-type': 'application/json',
         'X-CSRFToken': csrftoken},
         auth: {
           username: this.user.email,
           password: this.user.password}
         };
      axios.post('/login', JSON.stringify(this.user), config)
        .then(function(response) {
          
          console.log("response.data.token: ", response.data.token)

          if(response.status === 200 && 'token' in response.data) {
            this.$session.start()
            this.$session.set('jwt', response.data.token)
            Vue.http.headers.common['Autherization'] = 'Bearer ' + response.data.token

            console.log("Logged in!: ", response);
            this.loggedIn = true
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    LogOut: function(event) {
      this.loggedIn = false;
      this.clearName()
    },
    clearName() {
      this.user.name = ''
      this.user.password = ''
      this.user.name = ''
      this.user.phone = ''
    },
    handleOk(evt) {
      // Prevent modal from closing
      evt.preventDefault()
      if (!this.user.email) {
        alert('Please enter your email')
      } else {
        this.handleSubmit()
      }
    },
    handleSubmit() {
      var config = {headers :
        {'content-type': 'application/json',
         'X-CSRFToken': csrftoken}};
      axios.post('/register', JSON.stringify(this.user), config)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
      this.clearName()
      this.$refs.modal.hide()
    },
    FilterCategory(category){
      this.$emit('categoryChanged', category);
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

.test {
  background-color: black;
}


.hover-element {
  display: inline-block;
  background: #a5a5a5;
  padding-top: 1.5em;
  padding-bottom: 1em;
  font-size: 18pt;
}

.hover-element>a {
  color: black;
}

.hover-element:hover {
  background-color: #328afc;
}

.hover-element:hover>a {
  color: white;
}


.menuActive {
  display: none;
}

.iconactive {
  transform: rotate(45deg);
}


.menu-img:hover {
  transform: rotate(45deg);
}
</style>
