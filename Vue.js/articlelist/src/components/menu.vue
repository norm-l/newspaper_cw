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
            Email: {{user.username}}
          </b-col>
          <b-col>
            Name: {{user.name}}
          </b-col>
          <b-col>
            Tel: {{user.tel}}
          </b-col>
          <b-col>
            <b-button v-on:click="LogOut" type="button" variant="danger">Logout</b-button>
          </b-col>
        </b-row>
      </div>
      <div v-else>
        <b-row>
          <b-col>
            <b-form @submit.prevent="LogIn" inline novalidate validated>
              <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                <label class="sr-only" for="email" />
                <b-form-input v-model="user.username" class="form-control" type="email" placeholder="E-Mail" required />
              </b-input-group>
              <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
                <b-form-input v-model="user.password" type="password" placeholder="Password" required />
              </b-input-group>
              <b-button type="submit" variant="primary">Login</b-button>
            </b-form>
          </b-col>
          <b-col>
            <b-btn v-b-modal.modalPrevent>Register</b-btn>
          </b-col>
        </b-row>
      </div>
    </b-container>
    <b-modal id="modalPrevent" ref="modal" title="Register" @ok="handleOk" @shown="clearName">
      <b-form @submit.stop.prevent="handleSubmit" novalidate validated>
        <b-form-input type="email" class="form-control" placeholder="E-Mail" v-model="user.username" required />
        <b-form-input type="password" placeholder="Password" v-model="user.password" required />
        <b-form-input type="text" placeholder="Name" v-model="user.name" required />
        <b-form-input type="tel" pattern="\d+" placeholder="Phone Number" v-model="user.phone" required />
      </b-form>
    </b-modal>
  </div>
</template>


<script>
import axios from "axios";
import cookies from "cookies-js";

var csrftoken = "not-loaded";

export default {
  name: "menubar",
  data() {
    return {
      showAlert: false,
      isSubHidden: true,
      loggedIn: false,
      user: { username: "", password: "", name: "", phone: "" },
      // Placeholder object with a few articles.
      categories: {
        category0: { id: 0, name: "Home" },
        category1: { id: 1, name: "Business" },
        category2: { id: 2, name: "Politics" },
        category3: { id: 3, name: "Technology" }
      }
    };
  },
  created() {
    csrftoken = cookies.get("csrftoken");
    if (this.$session.exists()) {
      // The session exists (user is not logged out) so we get the user details
      this.user = this.$session.get("user");
      axios.defaults.headers.common["Authorization"] =
              "Token " + this.$session.get("token: ");
      this.loggedIn = true;
    }
  },
  props: ["cat"],
  methods: {
    toggleSub: function(event) {
      this.isSubHidden = !this.isSubHidden;
    },
    LogIn: function(event) {
      event.preventDefault();
      var config = {
        headers: {
          "content-type": "application/json",
          "X-CSRFToken": csrftoken
        },
        auth: {
          username: this.user.username,
          password: this.user.password
        }
      };
      axios
        .post("/login", JSON.stringify(this.user), config)
        .then(response => {
          // If the response was successful and contains a token
          if (response.status === 200 && "token" in response.data) {
            // Start a session
            this.$session.start();
            // Assign the jwt token from back-end to the session
            this.$session.set("token: ", response.data.token);
            // Save user details to the session
            this.$session.set("user", this.user);
            // Set the authorization header to the back-end token
            axios.defaults.headers.common["Authorization"] =
              "Token " + response.data.token;
            // User is now logged in
            this.loggedIn = true;
          }
        })
        .catch(error => {
          if (error.response.status === 403) {
            alert("Invalid username and/or password!");
          } else {
            console.log(error);
          }
        });
    },
    LogOut: function(event) {
      this.loggedIn = false;
      this.$session.destroy();
      this.clearName();
    },
    clearName() {
      this.user.username = "";
      this.user.password = "";
      this.user.name = "";
      this.user.phone = "";
    },
    TransformRegister(){
      var usr = {};
      usr.email = this.user.username;
      usr.password = this.user.password;
      usr.name = this.user.name;
      usr.phone = this.user.phone;

      return usr;
    },
    handleOk(evt) {
      // Prevent modal from closing
      evt.preventDefault();
      if (!this.user.username) {
        alert("Please enter your email");
      } else {
        this.handleSubmit();
      }
    },
    handleSubmit() {
      var config = {
        headers: {
          "content-type": "application/json",
          "X-CSRFToken": csrftoken
        }
      };
      axios
        .post("/register", JSON.stringify(this.TransformRegister()), config)
        .then(response => {
          alert("Succesfully registered! Please login");
        })
        .catch(error => {
          console.log(error);
        });
      this.clearName();
      this.$refs.modal.hide();
    },
    FilterCategory(category) {
      this.$emit("categoryChanged", category);
    },

  }
};
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

.hover-element > a {
  color: black;
}

.hover-element:hover {
  background-color: #328afc;
}

.hover-element:hover > a {
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
