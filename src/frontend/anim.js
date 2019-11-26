$(document).ready(() => {
    $('.message a').click(function(){
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
     });
});

chrome.tabs.getSelected(null, function(tab){
    document.getElementById("url-input").value = tab.url;
});