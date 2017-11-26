webpackJsonp([1], {
    NHnr: function(e, t, i) {
        "use strict";

        function s(e) {
            i("S5cY")
        }

        function n(e) {
            i("XFK7")
        }
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        var u = i("7+uW"),
            a = {
                name: "articles",
                data: function() {
                    return {
                        title: "Article List",
                        articles: {
                            article1: {
                                title: "Article Title 1",
                                content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.",
                                url: "/article",
                                image: "/static/Newspaper/img/default.png"
                            },
                            article2: {
                                title: "Article Title 2",
                                content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.",
                                url: "/article",
                                image: "/static/Newspaper/img/default.png"
                            },
                            article3: {
                                title: "Article Title 3",
                                content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum hendrerit consequat leo fermentum condimentum. Fusce in eros malesuada, tincidunt felis eget, dignissim nisl. Integer vitae auctor nibh. Integer accumsan mauris eu nulla interdum scelerisque. Sed lacinia vitae augue et aliquet. Suspendisse ultrices felis in turpis consequat, sed pellentesque augue pellentesque. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis in enim quis est condimentum finibus. Suspendisse quis lacus dolor. Morbi ut enim eu lorem varius fringilla.",
                                url: "/article",
                                image: "/static/Newspaper/img/default.png"
                            }
                        }
                    }
                },
                methods: {}
            },
            l = function() {
                var e = this,
                    t = e.$createElement,
                    i = e._self._c || t;
                return i("div", {
                    staticClass: "articles"
                }, [i("h1", {
                    domProps: {
                        textContent: e._s(e.title)
                    }
                }), e._v(" "), 0 !== Object.keys(e.articles).length ? i("div", {
                    staticClass: "center-block"
                }, e._l(e.articles, function(t) {
                    return i("div", {
                        staticClass: "col-md-10 article-border"
                    }, [i("h1", {
                        domProps: {
                            textContent: e._s(t.title)
                        }
                    }), e._v(" "), i("img", {
                        staticClass: "pull-left img-responsive margin10 thumb img-thumbnail",
                        attrs: {
                            src: t.image
                        }
                    }), e._v(" "), i("p", {
                        domProps: {
                            textContent: e._s(t.content)
                        }
                    }), e._v(" "), i("a", {
                        staticClass: "btn btn-success pull-right marginBottom10",
                        attrs: {
                            href: t.url
                        }
                    }, [e._v("Continue Reading..")])])
                })) : i("div", [e._v("No Articles Found!")])])
            },
            r = [],
            c = {
                render: l,
                staticRenderFns: r
            },
            o = c,
            m = i("VU/8"),
            d = s,
            p = m(a, o, !1, d, "data-v-15be2831", null),
            g = p.exports,
            f = {
                name: "app",
                components: {
                    articles: g
                }
            },
            q = function() {
                var e = this,
                    t = e.$createElement,
                    i = e._self._c || t;
                return i("div", {
                    attrs: {
                        id: "app"
                    }
                }, [i("articles")], 1)
            },
            b = [],
            v = {
                render: q,
                staticRenderFns: b
            },
            h = v,
            _ = i("VU/8"),
            S = n,
            A = _(f, h, !1, S, null, null),
            C = A.exports;
        u.a.config.productionTip = !1, new u.a({
            el: "#app",
            template: "<App/>",
            components: {
                App: C
            }
        }), i("uWbR")
    },
    S5cY: function(e, t) {},
    XFK7: function(e, t) {},
    uWbR: function(e, t) {}
}, ["NHnr"]);
//# sourceMappingURL=app.9e7d5eab39a27a54483b.js.map
