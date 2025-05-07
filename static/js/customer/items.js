
if (!window.isAnchorListenerAdded) {
    document.addEventListener("click", e => {
        if (e.target.tagName === "A") {
            console.log("Clicked")
        }
    })
    window.isAnchorListenerAdded = true;
}

async function loadTemplate() {
    if (itemTemplate !== "") return
    options.body = ""
    await fetch("/item")
        .then(response => response.text())
        .then(data => {
            itemTemplate = data
        })

    document.getElementById("search_input").addEventListener("keypress", e => {
        if (e.key === 'Enter'){
            document.getElementById("search_enter").click()
        }
    })
}

function loadItems(search_name){
    if (search_name){
        name = document.getElementById("search_input").value
    } else {
        name = ""
    }

    options.body = JSON.stringify({
        sql_method: "select_all",
        offset: 0,
        limit: 5,
        data: {
            name: name
        }
    })

    fetch("api/database/items", options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            return response.json();
        })
        .then(data => {
            if (document.getElementById("item_container") === null) return;

            document.getElementById("item_container").innerHTML = ""

            if (data.length === 0){
                const labelP = document.createElement("p")
                labelP.textContent = "There seems to be no items yet. Try refreshing the page."
                document.getElementById("item_container").appendChild(labelP)
            } else {
                data.forEach(element => {
                    const item_box = document.createElement("div")
                    item_box.className = "item_box"

                    const item_div = document.createElement("a")
                    const timestamp = element["Timestamp"]
                    item_div.className = "item_div"
                    item_div.href = "/home/items/item"
                    item_div.innerHTML = itemTemplate
                    item_div.children[0].src = element["url"]
                    item_div.children[0].alt = timestamp
                    item_div.children[1].textContent = element["Name"]
                    item_div.children[2].textContent = element["Price"]
                    item_div.children[3].textContent = `Quantity: ${element["Quantity"]}`

                    item_box.appendChild(item_div)

                    document.getElementById("item_container").appendChild(item_box)
                })
            }
            console.log(data)
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error)
        })
}

loadTemplate().then(() => {
    loadItems(false)
})
