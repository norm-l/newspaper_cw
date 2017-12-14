<template>
  <div class="articles">
    <div v-if="readingList">
      <!-- Check if there are any articles in the object. -->
      <div v-if="Object.keys(articles).length !== 0" class="center-block">
        <!-- Loop through the object finding all articles, attaching the classes to them -->
        <div v-for="article in articles" class="col-md-10 article-border">
          <!-- Article Title -->
          <h2 class="mt-3" v-text="article.title" />
          <!-- Article Header -->
          <p class="text-muted">
            <icon name="calendar" class="mr-1" />
            <small v-text="article.pub_date" />
            <icon name="user" class="ml-1 mr-1" />
            <small v-text="article.author" />
            <icon name="bookmark-o" class="ml-1 mr-1" />
            <small v-text="article.category" />
          </p>
          <!-- Article Content -->
          <div class="row">
            <div class="col-md-12">
              <!-- Article Image -->
              <img :src="article.article_img" class="float-left img-responsive mr-3 thumb img-thumbnail">
              <!-- Article Summary -->
              <p v-text="article.headline" />
            </div>
          </div>
          <!-- Continue reading the full article -->
          <button class="btn btn-success float-right mb-3" v-on:click="ReadArticle(article.id)">Continue Reading..</button>
          <ul class="list-unstyled mt-2">
            <!-- Article Tags -->
            <li>
              <icon name="tags" />
              <span v-for="tag in splitTags(article.tags)" class="badge badge-info ml-1" v-text="tag" />
            </li>
            <!-- Article Likes -->
            <li>
              <span class="like_button" v-on:click="LikeArticle(article.id)"><icon name="thumbs-up" /></span>
              <span class="badge badge-success ml-1" v-text="article.likes" />
            </li>
          </ul>
        </div>
      </div>
      <!-- No articles were found therefore we display a simple message -->
      <div v-else>
        <icon scale="5" name="warning" class="mt-5" />
        <p>
          <b>No Articles Found!</b>
        </p>
      </div>
    </div>
    <div v-else>
      <div class="center-block">
        <div class="col-md-10">
          <div class="text-l">
            <!-- Article Title -->
            <h2 class="mt-3" v-text="singleArticle.title" />
            <!-- Article Header -->
            <p class="text-muted">
              <icon name="calendar" class="mr-1" />
              <small v-text="singleArticle.pub_date" />
              <icon name="user" class="ml-1 mr-1" />
              <small v-text="singleArticle.author" />
              <icon name="bookmark-o" class="ml-1 mr-1" />
              <small v-text="singleArticle.category" />
            </p>
            <!-- Article Content -->
            <div class="row">
              <div class="col-md-12">
                <!-- Article Image -->
                <img :src="singleArticle.article_img" class="float-left img-responsive mr-3 thumb img-thumbnail">
                <!-- Article Summary -->
                <p v-text="singleArticle.content" />
              </div>
            </div>
            <!-- Back to articles the full article -->
            <button class="btn btn-success float-right mb-3" v-on:click="BackToList(singleArticle.id)">Back</button>
            <ul class="list-unstyled mt-2">
              <!-- Article Tags -->
              <li>
                <icon name="tags" />
                <span v-for="tag in splitTags(singleArticle.tags)" class="badge badge-info ml-1" v-text="tag" />
              </li>
              <!-- Article Likes -->
              <li>
                <span class="like_button" v-on:click="LikeArticle(singleArticle.id, true)"><icon name="thumbs-up" /></span>
                <span class="badge badge-success ml-1" v-text="singleArticle.likes" />
              </li>
            </ul>
            <commentComponent :da="sArticleId"></commentComponent>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import commentComponent from "./comments";
export default {
  name: "articles",
  components: {
    commentComponent
  },
  data() {
    // return {
    //   articles: [],
    //   singleArticle: {},
    //   sArticleId: 1,
    //   readingList: true,
    //   category: "Home"
    // };
    // For local use:
    return {
      articles: [
        {
          id: "1",
          title: "title1",
          author: "author1",
          pub_date: "February 2, 2017",
          content: "Small text example",
          category: "business",
          likes: 10,
          article_img: "./src/assets/default.png",
          tags: "test, wow, nice"
        }
      ],
      singleArticle:         {
          id: "2",
          title: "title1",
          author: "author1",
          pub_date: "February 2, 2017",
          content: "Small text example",
          category: "business",
          likes: 10,
          article_img: "./src/assets/default.png",
          tags: "test, wow, nice"
        },
      readingList: false,
      category: "Home",
      sArticleId: 1,
    };
  },
  mounted: function() {
    axios
      .get("/api/latestarticles")
      .then(response => {
        this.articles = response.data;
        this.readingList = true;

        this.articles.forEach(article => {
          this.GetLikes(article.id, false);
        });
      })
      .catch(err => {
        console.log(err);
      });
  },
  props: ["cat"],
  watch: {
    $props: {
      handler: function(val) {
        this.category = val.cat;
        this.GetLatestArticles(this.category);
      },
      deep: true
    }
  },
  methods: {
    GetLikes(id, is_single) {
      axios
        .get("/get_likes/" + id)
        .then(response => {
          if (is_single) {
            this.singleArticle.likes = response.data;
          } else {
            this.articles.forEach(function(article) {
              if (article.id === id) {
                article.likes = response.data;
              }
            });
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    splitTags(tags) {
      return tags.split(", ");
    },
    LikeArticle(id, is_single) {
      axios
        .post("/like/" + id)
        .then(response => {
          if (is_single) {
            this.GetLikes(id, true);
          } else {
            this.GetLikes(id, false);
          }
        })
        .catch(error => {
          if (error.response.status === 401) {
            alert("Please login to like articles!");
          } else {
            console.log(error);
          }
        });
    },
    ReadArticle(id) {
      axios
        .get("/api/article/" + id)
        .then(response => {
          this.singleArticle = response.data;
          this.GetLikes(id, true);
          this.sArticleId = this.singleArticle.id;
          this.readingList = false;
        })
        .catch(err => {
          console.log(err);
        });
    },
    BackToList(id) {
      this.GetLatestArticles(this.category);
      // this.GetLikes(id, false);
    },
    GetLatestArticles(category) {
      if (category == "Home") {
        axios
          .get("/api/latestarticles")
          .then(response => {
            this.articles = response.data;
            this.singleArticle = {};
            this.readingList = true;

            this.articles.forEach(article => {
              this.GetLikes(article.id, false);
            });
          })
          .catch(err => {
            console.log(err);
          });
      } else {
        var conf = { params: { category: category } };
        axios
          .get("/api/latestarticles", conf)
          .then(response => {
            this.articles = response.data;
            this.singleArticle = {};
            this.readingList = true;
          })
          .catch(err => {
            console.log(err);
          });
      }
    }
  }
};
</script>

<style scoped>
/* To display borders between articles and align all article text left */
.like_button {
  cursor: pointer;
}
.like_button:active {
  color: #428bca;
}
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
