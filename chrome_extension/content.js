function modify_klasjdflasjflsakfjsaf1231231231312355() {
    const article = document.querySelector("nav[aria-label='Private channels']");
    // find the parent and tag it with   
    // display: none;
    // TODO support toggling this
    // `document.querySelector` may return null if the selector doesn't match anything.
    if (article) {
        console.log("cool");
        article.parentElement.setAttribute("style", "display:none")
    } else {
        console.log("not cool");
    }
}

modify_klasjdflasjflsakfjsaf1231231231312355();