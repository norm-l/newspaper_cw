<template>
  <div class="articles">
    <h1 v-text="title"></h1>
    <!-- Check if there are any articles in the object. -->
    <div v-if="Object.keys(articles).length !== 0" class="center-block">
      <!-- Loop through the object finding all articles, attaching the classes to them -->
      <div v-for="article in articles" class="col-md-10 article-border">
        <!-- Article Title -->
        <h1 class="margin-top" v-text="article.title"></h1>
        <!-- Article Image -->
        <img :src="article.image" class="float-left img-responsive margin10 thumb img-thumbnail">
        <!-- Article Content/Summary -->
        <p v-text="article.content"></p>
        <!-- Continue reading the full article -->
        <a class="btn btn-success float-right margin-bottom" :href="article.url">Continue Reading..</a>
      </div>
    </div>
    <!-- No articles were found therefore we display a simple message -->
    <div v-else>No Articles Found!</div>
  </div>
</template>

<script>
  export default {
    name: 'articles',
    data() {
      return {
        title: 'Article List',
        // Placeholder object with a few articles.
        articles: {
          article1: {title: 'Article Title 1', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.', url: '', image: './src/assets/default.png'},
          article2: {title: 'Article Title 2', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.', url: '', image: './src/assets/default.png'},
          article3: {title: 'Article Title 3', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.', url: '', image: './src/assets/default.png'}
        }
      }
    },
    methods: {
    }
  }
</script>

<style scoped>
/* To display borders between articles and align all article text left */
.article-border {
  border-bottom: 1px solid #ddd;
  text-align: left;
}
.center-block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
/* Add a margin to the article image */
.margin10 {
   margin-bottom: 10px;
   margin-right: 10px;
}
.margin-bottom {
  margin-bottom: 10px;
}
.margin-top {
  margin-top: 10px;
}
</style>
