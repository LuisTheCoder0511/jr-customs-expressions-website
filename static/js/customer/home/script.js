import {queryItems} from "./content/items.js";

let contentState = sessionStorage.getItem("contentState")

if (contentState == null){
    state("items")
}

const popup_div = document.createElement("div")

popup_div.id = "account-popup"
popup_div.style.visibility = "visible"


let userData = null
await fetch("/read-account")
    .then(response => response.json())
    .then(data => {
        userData = data["account"]
        console.log(userData)
    })

if (userData["username"] === null){
    createGuestDiv().then()
} else {
    const username = userData['username']
    await fetch(`/read-user/${username}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            userData["name"] = data["name"]
        })
    createNameDiv(userData).then()
}

document.body.insertBefore(popup_div, document.getElementById("content"))

document.getElementById("button-items").addEventListener("click", () => {
    state("items")
    queryItems(10, 0, "None")
})

document.getElementById("button-reviews").addEventListener("click", () => {
    state("reviews")
})

document.getElementById("button-about").addEventListener("click", () => {
    state("about")
})

document.getElementById("button-policies").addEventListener("click", () => {
    state("policies")
})

document.getElementById("img-account").addEventListener("click", () => {
    if (popup_div.style.visibility === "hidden"){
        popup_div.style.visibility = "visible"
        popup_div.style.position = "absolute"
    } else {
        popup_div.style.visibility = "hidden"
        popup_div.style.position = "fixed"
    }
})

function state(targetState){
    contentState = targetState
    sessionStorage.setItem("contentState", contentState)
    fetch(`/${contentState}`)
        .then(r => r.text())
        .then(data => {
            const content = document.getElementById("content")
            content.innerHTML = data
        })
}

async function sign_out(){
    await fetch("/customer/signout")
        .then(() => {
            sessionStorage.clear()
            window.location.reload()
        })
}

async function createNameDiv(userData) {
    await fetch("/account/name")
        .then(r => r.text())
        .then(data => {
            popup_div.innerHTML = data
        })

    const nameA = popup_div.children[0]
    nameA.children[0].children[0].src = "/static/assets/images/facebook.png"
    nameA.children[1].children[0].textContent = userData["name"]
    nameA.children[1].children[1].textContent = `@${userData["username"]}`

    document.getElementById("account-popup-logout").addEventListener("click", sign_out)
}

async function createGuestDiv() {
    await fetch("/account/guest")
        .then(r => r.text())
        .then(data => {
            popup_div.innerHTML = data
        })
}

document.getElementById("button-items").click()