const like = document.getElementById("product_metadata_like_button")
like.addEventListener("click", () => {
    if (like.children[0].alt === "like"){
        like.children[0].src = "/static/assets/images/liked.png"
        like.children[0].alt = "liked"
    } else {
        like.children[0].src = "/static/assets/images/like.png"
        like.children[0].alt = "like"
    }
})