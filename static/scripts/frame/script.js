const options = {method: "POST", headers: {"Content-Type": "application/json"}}

async function changeIframe(client, content_div, newSrc, extraArg, state){
    const options_data = {client: client, arg: newSrc, arg_extra: extraArg}
    options.body = JSON.stringify(options_data)
    fetch("/mcnav/", options)
        .then(response => response.text())
        .then(html => {
            sessionStorage.setItem("state", state)
            sessionStorage.setItem("innerHTML", html);
            location.reload()
        })
        .catch(error => console.error("error:", error));
}


window.addEventListener("DOMContentLoaded", () => {
    const savedContent = sessionStorage.getItem("innerHTML")
    if (savedContent) {
        document.body.innerHTML = savedContent
    }

    const scriptsToLoad = [];
    const savedState = sessionStorage.getItem("state")
    switch (savedState){
        case "customer-items":
            scriptsToLoad.push("/static/scripts/customer/mcnav/items/script.js")
            break
        case "customer-reviews":
            scriptsToLoad.push("/static/scripts/customer/mcnav/reviews/script.js")
            break
        case "customer-policies":
            scriptsToLoad.push("/static/scripts/customer/mcnav/policies/script.js")
            break
        case "seller-add":
            scriptsToLoad.push("/static/scripts/seller/mcnav/items/add/script.js")
            break
        case "seller-home":
            scriptsToLoad.push("/static/scripts/seller/mcnav/items/home/script.js")
            break
    }

    scriptsToLoad.forEach((src) => {
        let script = document.createElement("script")
        script.src = src
        script.defer = true
        document.body.append(script)
    })

    sessionStorage.clear()
})