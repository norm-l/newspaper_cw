<template>
  <div>
  <div>
    <b-form @submit="addComment" @reset="resetComment">
        <b-form-textarea placeholder="Enter your comment" v-model="comment" :rows="3" :max-rows="10"></b-form-textarea>
        <b-button class="mt-2" type="submit" variant="primary">Add Comment</b-button>
    </b-form>
</div>
      <!-- Check if there are any articles in the object. -->
      <div v-if="Object.keys(comments).length !== 0" class="center-block">
        <!-- Loop through the object finding all articles, attaching the classes to them -->
        <b-list-group class="col-md-10">
          <div v-for="comment in comments" :key='comment.id'>
                <b-list-group-item class="mt-3">
                  <blockquote class="blockquote">
                    <p class="mb-0">{{comment.content}}</p>
                    <footer class="blockquote-footer"><cite>{{comment.user.name}}</cite></footer>
                  </blockquote>
                    <b-button v-on:click="DeleteComment(comment.id)" variant="danger">Delete</b-button>
              </b-list-group-item>
          </div>
        </b-list-group>
      </div>
      <!-- No articles were found therefore we display a simple message -->
      <div class="center-block" v-else>
        <icon scale="5" name="warning" class="mt-5" />
        <p>
          <b>No comments for this article! You are free to join the discussion</b>
        </p>
      </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "commentComponent",
  data() {
    return {
      articleId: null,
      comment: "",
      comments: []
    };
  },
  mounted: function() {
    this.articleId = this.da;
    this.DisplayComments(this.da);
  },
  props: ["da"],
  methods: {
    addComment(event) {
      event.preventDefault();
      var c = { content: "", article: null };
      c.content = this.comment;
      c.article = this.articleId;

      axios
        .post("/api/comment/" + this.articleId + "/", c)
        .then(response => {
          this.DisplayComments(this.da);
        })
        .catch(error => {
          if (error.response.status === 401) {
            alert("Please login to add a comment!");
          } else {
            console.log(error);
          }
        });
    },
    resetComment(event) {
      evt.preventDefault();
      this.comment = "";
    },
    DisplayComments(id) {
      axios
        .get("/api/comments/" + id)
        .then(response => {
          this.comments = response.data;
        })
        .catch(err => {
          console.log(err);
        });
    },
    DeleteComment(id) {
      axios
        .delete("/api/comment/" + id)
        .then(response => {
          this.DisplayComments(this.da);
        })
        .catch(error => {
          if (error.response.status === 401) {
            alert("Please login to delete a comment!");
          } else if (error.response.status === 404) {
            alert("Either you're trying to delete a comment which does not exist or you are not the owner of the comment!");
          } else {
            console.log(error);
          }
        });
    }
  }
};
</script>

<style scoped>
/* To display borders between articles and align all article text left */

.article-border {
  border-bottom: 1px solid #ddd;
  text-align: left;
}

.text-l {
  text-align: left;
}

/* In order to center all articles */

.center-block {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
