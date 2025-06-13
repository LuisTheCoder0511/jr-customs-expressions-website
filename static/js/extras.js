let hidden = true
let click_lock = false

fetch("/base/header")
    .then(response => response.text())
    .then(data => {
        document.getElementById("header").innerHTML = data
        const popup = document.getElementById("popup")
        document.getElementById("account_button").children[0].addEventListener("mousedown", () => {
            if (click_lock) return
            if (hidden) {
                popup.style.visibility = "visible"
            } else {
                popup.style.visibility = "hidden"
            }
            hidden = !hidden
        })
    })

fetch("/base/footer")
    .then(response => response.text())
    .then(data => {
        document.getElementById("footer").innerHTML = data
    })

function scrollTarget(name){
    if (window.location.pathname !== "/") {
        sessionStorage.setItem("scrollTarget", name)
        window.location.href = "/"
    } else scrollInto(name);
}

window.addEventListener("mousedown", () => {
    click_lock = true
})

window.addEventListener("mouseup", () => {
    click_lock = false
})