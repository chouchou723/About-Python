webpackJsonp([0],{"1FP/":function(t,e){t.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAlCAYAAAAwYKuzAAAAAXNSR0IArs4c6QAAATtJREFUWAntWMsKwjAQtCqKIj5QxIv//2HeRA8+UJSKztSm1KVNjEGawwaWZLOPDpOy3TRpvccS0zhfu6YbHDYupxr7Gvv9GpvcPmJj2853u9Jq0X18ZRqf2MxXBjyR8SCzCv0udB91D+eeI2ACe2J8JMAHDDtj/MPMY3ONERwKXOaIXUGN2RVgKPXKoDIYykBofCdPkGKmnCAhhThPFzQRBzEQC9c6lAFlwMYA25oVpOgebM4N2FICY3sT7SDAMyRaBqNlToEpA7EwYLqZAQDx4k696W6GZc+UvqwOQm/NIEMI2xuWnSbHAg9n2btArnonCT0KZVAZDGUgND76d1C2WSzUrEO2wUL+zW+0qhz8GLj+D5qPRxYvAbLDnlZlLu3xH+KvAOeI/QBQylu5NEfsc0H28ZUP9YnNfF+0AyRndvEn/gAAAABJRU5ErkJggg=="},"7Otq":function(t,e,a){t.exports=a.p+"static/img/logo.1cc34d4.png"},eoc7:function(t,e){},gvxg:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=a("gyMJ"),s={data:function(){return{scancodeUrl:"",refreshCode:"",asklist:["发布文章","编辑文章","上传作品"],bgstyle:"",isShowAskImg:!1}},mounted:function(){this.clearLoginInfo(),this.getAuthCode()},computed:{},methods:{handleAskImg:function(t,e){this.isShowAskImg=e,this.bgstyle="img"+t},clearLoginInfo:function(){var t=this;o.a.postClearLoginInfo().then(function(e){var a=e.data,o=a.code,s=a.msg;a.data;"0"==o||t.$message.error(s)}).catch(function(t){console.error(t)})},getAuthCode:function(){var t=this;o.a.getAuthCode().then(function(e){var a=e.data,o=a.code,s=a.msg,r=a.data;if("0"===o){var n=void 0,i=void 0,c=window.sessionStorage;c.clear(),c.authorId=r.author.id?r.author.id:"",c.authorAvatarId=r.author.avatarId?r.author.avatarId:"",c.authorNickname=r.author.nickname?r.author.nickname:"",c.collectionId=r.targetData&&r.targetData.collectionId?r.targetData.collectionId:"",t.refreshCode&&t.refreshCode!=r.code&&(document.querySelector(".scanCode > img").src=document.querySelector(".scanCode > img").src),t.refreshCode=r.code,"ALLOW"===r.state?(n="ARTWORK"!==r.targetType.name?"article":"artwork",clearTimeout(i),t.$router.push({path:"/site/"+n,query:{targetType:r.targetType.name||"",targetId:r.targetId}})):i=setTimeout(function(){t.getAuthCode()},3e3)}else t.$message.error(s)}).catch(function(t){console.error(t)})},getQrcode:function(){return o.a.getQrcode()}}},r={render:function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"container"},[t._m(0),t._v(" "),o("main",[o("h2",[t._v("使用艺下app扫描")]),t._v(" "),o("div",{staticClass:"scanCode"},[o("img",{staticStyle:{width:"100%",height:"100%"},attrs:{src:t.getQrcode(),alt:"二维码"}})]),t._v(" "),o("img",{staticClass:"intro-icon",attrs:{src:a("1FP/"),alt:"扫描进入网页版"}}),t._v(" "),o("p",{staticClass:"intro"},[t._v("进入网页版编辑器")]),t._v(" "),o("ul",{staticClass:"asklist"},t._l(t.asklist,function(e,a){return o("li",{on:{mouseenter:function(e){t.handleAskImg(a+1,!0)},mouseleave:function(e){t.handleAskImg(a+1,!1)}}},[t._v(t._s(e))])})),t._v(" "),o("transition",{attrs:{name:"fade"}},[o("div",{directives:[{name:"show",rawName:"v-show",value:t.isShowAskImg,expression:"isShowAskImg"}],staticClass:"ask-img",class:t.bgstyle})])],1)])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"topBar"},[e("figure",[e("img",{attrs:{src:a("7Otq"),alt:"艺下"}}),this._v(" "),e("figcaption",[this._v("发／现／身／边／的／艺／术／玩／伴")])])])}]};var n=a("VU/8")(s,r,!1,function(t){a("eoc7")},"data-v-3d53af4e",null);e.default=n.exports}});