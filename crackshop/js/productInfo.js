let productsJSON = [{"name":"Grzyby halucynogenne","price":25,"seller":"Annon69","img":"img.png","id":1,"info":"XXXXXXXXXXXXXXXXXXXXXXXXXXX"},{"name":"Grzyby halucynogenne","price":25,"seller":"Annon69","img":"img.png","id":2,"info":"XXXXXXXXXXXXXXXXXXXXXXXXXXX"},{"name":"Grzyby halucynogenne","price":25,"seller":"Annon69","img":"img.png","id":3,"info":"XXXXXXXXXXXXXXXXXXXXXXXXXXX"},{"name":"Grzyby halucynogenne","price":25,"seller":"Annon69","img":"img.png","id":4,"info":"XXXXXXXXXXXXXXXXXXXXXXXXXXX"}]
let products = JSON.parse(productsJSON);

products.forEach(function(elem){
	console.log(elem)
})

let $main = $('main');




$('.product').on('click', function(){
	console.log(this)
})