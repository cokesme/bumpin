javascript:(function(document) {
    const article = document.querySelector("nav[aria-label='Private channels']");
    if (article) {
        article.parentElement.setAttribute("style", "display:none")
    }
    })(document);