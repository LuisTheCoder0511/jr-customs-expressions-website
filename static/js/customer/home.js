function readAbout(){
    fetch("/static/assets/data/about.txt")
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load the text file')
            }
            return response.text()
        })
        .then(data => {
            document.getElementById("about_text").textContent = data
        })
        .catch(error => {
            console.error('Error:', error);
        })
}

function loadProducts(){
    const list = document.getElementsByClassName("product_template_click")
    const iterator = list[Symbol.iterator]()
    let element = iterator.next()
    while (!element.done){
        const template = element.value
        template.addEventListener("mousedown", e => {
            if (e.button !== 0) return
            window.location.href = "/customer_page/product"
        })
        element = iterator.next()
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const targetId = sessionStorage.getItem("scrollTarget")
    if (targetId) {
        scrollInto(targetId)
        sessionStorage.removeItem("scrollTarget")
    }
})

function scrollInto(name){
    document.getElementById(name).scrollIntoView({
        behavior: "smooth",
        block: "center",
        inline: "nearest"
    })
}

readAbout()
loadProducts()