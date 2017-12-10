<template>
  <div>
  <div>
    <b-form @submit="addComment" @reset="resetComment">
        <b-form-textarea placeholder="Enter your comment" v-model="comment" :rows="3" :max-rows="10"></b-form-textarea>
        <b-button type="submit" variant="primary">Add Comment</b-button>
    </b-form>
</div>
      <!-- Check if there are any articles in the object. -->
      <div v-if="Object.keys(comments).length !== 0" class="center-block">
        <!-- Loop through the object finding all articles, attaching the classes to them -->

        <b-list-group>
        <div v-for="comment in comments" :key='comment.id'>
              <b-list-group-item>
                 {{comment.user.name}} - {{comment.content}}
            </b-list-group-item>
        </div>
        </b-list-group>
      </div>
      <!-- No articles were found therefore we display a simple message -->
      <div v-else>
        <icon scale="5" name="warning" class="mt-5" />
        <p>
          <b>No Comments for this article! You are free to join the discussion</b>
        </p>
      </div>


  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'commentComponent',
  data() {
    return {
      articleId: null,
      comment: "",
      comments: [{user : {name: "Andrew"}, content : "Im a troll" }],
      
    }
  },
  mounted: function() {

  },
  props: ['displayArticle'],
  watch: {
    '$props': {
      handler: function(val) {
        this.articleId = val.id
      },
      deep: true
    }
  },
  methods: {
      addComment(event){
        event.preventDefault();
        console.log(this.comment);

      },
      resetComment(event){
        evt.preventDefault();
        this.comment = "";
      }

  }
}
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
