<template>
  <div class="articles">
    <h1 v-text="title"></h1>
    <div v-if="Object.keys(articles).length !== 0" class="col-md-10 center-block">
      <div v-for="article in articles" class="article-border">
        <h1 v-text="article.title"></h1>
        <!-- <img :src="article.image" class="pull-left img-responsive thumb margin10 img-thumbnail"> -->
        <p v-text="article.content">
        </p>
        <!-- <a class="btn btn-readmore pull-right marginBottom10" :href="article.url">Continue Reading..</a> -->
      </div>
    </div>
    <div v-else>No Articles Found!</div>
  </div>
</template>

<script>
  export default {
    name: 'articles',
    data() {
      return {
        title: 'Article List',
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
.article-border {
  border-bottom: 1px solid #ddd;
  text-align: left;
}
.center-block {
    float: none;
}
.btn-readmore {
    color: #ffffff;
    background-color: #37d980;
    border-color: #37d980;
    border-radius: 0;
    margin-bottom: 10px
}
.open .dropdown-toggle.btn-blog {
    color: white;
    background-color: #34ca78;
    border-color: #34ca78;
}
.margin10 {
   margin-bottom: 10px;
   margin-right: 10px;
}
</style>
