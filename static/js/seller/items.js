sellerReplacement()

function feature(){
    console.log("Feature selected")
}

function trigger(){
    console.log("Trigger selected")
}

function remove(item_div){
    console.log("Delete selected")

    const json_form = new FormData()
    const json_object = {
        data: {
            timestamp: item_div.id.slice(5)
        },
        sql_method: "delete"
    }

    json_form.append("data", JSON.stringify(json_object))
    options.body = json_form

    fetch("/seller/api/items", options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            item_div.remove()
        })
}

function changeColor(element){
    const targetColor = "gray"
    if (element.style.backgroundColor === targetColor) element.style.backgroundColor = ""
    else element.style.backgroundColor = targetColor
}

function addItemTemplate(element, itemTemplate){
    const item_div = document.createElement("div")
    const timestamp = element["Timestamp"]
    item_div.className = "item_template"
    item_div.id = `item=${timestamp}`
    item_div.onclick = (() => {
        fetchSellerContent("content/item_edit", `?id=${timestamp}`)
    })
    item_div.innerHTML = itemTemplate
    const item_box = item_div.children[0]

    item_box.children[0].children[0].addEventListener("click", e => {
        e.stopPropagation()
        feature()
        changeColor(item_box.children[0].children[0])
    })

    if (element["url"] !== undefined){
        item_box.children[1].src = element["url"]
    }
    item_box.children[1].alt = timestamp

    const item_box_sub = item_box.children[2]

    item_box_sub.children[0].textContent = element["Name"]
    item_box_sub.children[1].textContent = `Quantity: ${element["Quantity"]}`
    item_box_sub.children[2].textContent = element["Price"]

    item_box.children[3].children[0].addEventListener("click", e => {
        e.stopPropagation()
        trigger()
    })
    item_box.children[3].children[1].addEventListener("click", e => {
        e.stopPropagation()
        let result = window.confirm("Are you sure you want to delete this item?")
        if (result) remove(item_div)
    })

    document.getElementById("seller_management_items_container").appendChild(item_div)
}

function loadTemplate(element) {
    let data = ""
    const itemTemplate = async () => {
        const response = await fetch("/seller/template/item_template")
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

    const json_form = new FormData()
    const json_object = {
        data: {
            name: name
        },
        sql_method: "select_all",
        offset: 0,
        limit: 5,
    }

    json_form.append("data", JSON.stringify(json_object))
    options.body = json_form

    fetch("/seller/api/items", options)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            return response.json();
        })
        .then(data => {
            console.log(data)
            if (document.getElementById("seller_management_items_container") === null) return;

            document.getElementById("seller_management_items_container").innerHTML = ""

            if (data.length === 0){
                const labelP = document.createElement("p")
                labelP.textContent = "There seems to be no items yet. Try refreshing the page or adding new items."
                document.getElementById("seller_management_items_container").appendChild(labelP)
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