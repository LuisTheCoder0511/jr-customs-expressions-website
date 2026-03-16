let hidden = true

fetch("/customer_base/header")
    .then(response => response.text())
    .then(data => {
        document.getElementById("header").innerHTML = data

        const popup = document.getElementById("popup")
        document.getElementById("account_button").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            if (hidden) {
                popup.style.visibility = "visible"
            } else {
                popup.style.visibility = "hidden"
            }
            hidden = !hidden
        })

        document.getElementById("seller").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page"
        })
    })

fetch("/customer_base/footer")
    .then(response => response.text())
    .then(data => {
        document.getElementById("footer").innerHTML = data
    })

function scrollTarget(name){
    if (window.location.pathname !== "/") {
        sessionStorage.setItem("scrollTarget", name)
        window.location.href = "/"
    } else scrollInto(name)
}