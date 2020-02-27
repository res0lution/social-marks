(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://6acae5e7.ngrok.io/static/js/socialmarks.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();