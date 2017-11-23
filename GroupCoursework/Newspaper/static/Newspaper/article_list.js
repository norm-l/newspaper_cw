Vue.component('article-list', {
	props: ['article-list'],
	template: '<li>{% verbatim %}{{ article-list.text }}{% endverbatim %}</li>'
})

var page = new Vue({
	el: '#app'
})

var articles = new Vue({
	el: '#article-list',
	data: {
		article_list: [
			{id: 0, articleTitle: 'articleTitle', articleAuthor: 'articleAuthor', articleContents: 'articleContents', datePosted: 'datePosted', articleCategory: 'articleCategory', userLikes: 'userLikes'},
			{id: 1, articleTitle: 'articleTitle1', articleAuthor: 'articleAuthor1', articleContents: 'articleContents1', datePosted: 'datePosted1', articleCategory: 'articleCategory1', userLikes: 'userLikes1'}
		]
	}
})