fetch("/base/header")
    .then(response => response.text())
    .then(data => {
        document.getElementById("header").innerHTML = data
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
