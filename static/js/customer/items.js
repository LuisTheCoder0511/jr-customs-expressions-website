
if (!window.isAnchorListenerAdded) {
    document.addEventListener("click", e => {
        if (e.target.tagName === "A") {
            console.log("Clicked")
        }
    })
    window.isAnchorListenerAdded = true;
}

document.getElementById("search_input").addEventListener("keypress", e => {
    if (e.key === 'Enter'){
        document.getElementById("search_enter").click()
    }
})

customerReplacement()

function addItemTemplate(element, itemTemplate){
    const item_box = document.createElement("div")
    item_box.className = "item_box"

    const item_div = document.createElement("a")
    const timestamp = element["Timestamp"]
    item_div.className = "item_div"
    item_div.id = `item=${timestamp}`
    item_div.onclick = (() => {
        fetchCustomerContent("content/item", `?id=${timestamp}`)
    })
    item_div.innerHTML = itemTemplate
    if (element["url"] !== undefined){
        item_div.children[0].src = element["url"]
    }
    item_div.children[0].alt = timestamp
    item_div.children[1].textContent = element["Name"]
    item_div.children[2].textContent = element["Price"]
    item_div.children[3].textContent = `Quantity: ${element["Quantity"]}`

    item_box.appendChild(item_div)

    document.getElementById("item_container").appendChild(item_box)
}

function loadTemplate(element) {
    let data = ""
    const itemTemplate = async () => {
        const response = await fetch("/customer/template/item_template")
        return data = await response.text()
    }
    itemTemplate().then(data => {
        addItemTemplate(element, data)
    })
    return data
}

function loadItems(search_name){
    if (search_name){
        name = document.getElementById("search_input").value
    } else {
        name = ""
    }

    const json_form = new FormData
    const json_object = {
        data: {
            name: name
        },
        sql_method: "select_all",
        offset: 0,
        limit: 5
    }

    json_form.append("data", JSON.stringify(json_object))
    options.body = json_form

    fetch("/customer/api/items", options)
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
                    loadTemplate(element)
                })
            }
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error)
        })
}

loadItems(false)
