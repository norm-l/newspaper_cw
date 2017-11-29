<template>
  <div class="articles">
    <!-- Check if there are any articles in the object. -->
    <div v-if="Object.keys(articles).length !== 0" class="center-block">
      <!-- Loop through the object finding all articles, attaching the classes to them -->
      <div v-for="article in articles" class="col-md-10 article-border">
        <!-- Article Title -->
        <h2 class="mt-3" v-text="article.title" />
        <!-- Article Header -->
        <p class="text-muted">
          <icon name="calendar" class="mr-1"/>
          <small v-text="article.pub_date"/>
          <icon name="user" class="ml-1 mr-1"/>
          <small v-text="article.author"/>
          <icon name="bookmark-o" class="ml-1 mr-1"/>
          <small v-text="article.category"/>
        </p>
        <!-- Article Content -->
        <div class="row">
          <div class="col-md-12">
            <!-- Article Image -->
            <img :src="article.article_img" class="float-left img-responsive mr-3 thumb img-thumbnail">
            <!-- Article Summary -->
            <p v-text="article.content" />
          </div>
        </div>
        <!-- Continue reading the full article -->
        <a class="btn btn-success float-right mb-3" href="#">Continue Reading..</a>
        <ul class="list-unstyled mt-2">
          <!-- Article Tags -->
          <li>
            <icon name="tags"/>
            <span v-for="tag in splitTags(article.tags)" class="badge badge-info ml-1" v-text="tag"/>
          </li>
          <!-- Article Likes -->
          <li>
            <icon name="thumbs-up"/>
            <span class="badge badge-success ml-1" v-text="article.likes"/>
          </li>
        </ul>
    </div>
  </div>
    <!-- No articles were found therefore we display a simple message -->
    <div v-else>
      <icon scale="5" name="warning" class="mt-5"/>
      <p><b>No Articles Found!</b>
      <br />Have you added some in <a href="http://127.0.0.1:8000/admin/Newspaper/article/"><i>here</i></a>?</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
  export default {
    name: 'articles',
    data () {
      return {articles:[]}
      // For local use:
      // return {articles:[{title: 'title1', author: 'author1', pub_date: 'February 2, 2017', content: 'Small text example', category: 'business', likes: 10, article_img: './src/assets/default.png', tags: 'test, wow, nice'}]}
    },
    mounted: function() {
      axios.get("/api/latestarticles")
      .then(response => {this.articles = response.data})
      .catch((err) => {
        console.log(err);
      })
    },
    methods: {
      splitTags(tags) {
        return tags.split(', ');
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
/* In order to center all articles */
.center-block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
