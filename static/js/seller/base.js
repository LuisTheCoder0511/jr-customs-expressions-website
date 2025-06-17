fetch("/seller_base/header")
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
    })

fetch("/seller_base/sidebar")
    .then(response => response.text())
    .then(data => {
        const sidebar = document.getElementById("sidebar")
        sidebar.innerHTML = data
        sidebar.style.maxWidth = "44px"
        sidebar_texts()
        document.getElementById("dashboard").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            if (sidebar.style.maxWidth === "44px"){
                sidebar.style.maxWidth = "140px"
            } else {
                sidebar.style.maxWidth = "44px"
            }
            sidebar_texts()
        })

        document.getElementById("customize").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page/customize"
        })

        document.getElementById("products").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page/products"
        })

        document.getElementById("reviews").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page/reviews"
        })

        document.getElementById("finances").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page/finances"
        })

        document.getElementById("reports").children[0].addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/seller_page/reports"
        })
    })

function sidebar_texts(){
    const list = document.getElementsByClassName("sidebar_text")
    const iterator = list[Symbol.iterator]()
    let element = iterator.next()
    while (!element.done){
        const text = element.value
        if (text.style.visibility === "hidden"){
            text.style.visibility = "visible"
        } else {
            text.style.visibility = "hidden"
        }
        element = iterator.next()
    }

}
