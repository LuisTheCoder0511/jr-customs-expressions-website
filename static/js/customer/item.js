
// const params = new URLSearchParams(window.location.search)
// const id = params.get("id")

customerReplacement()

function itemPageDivs(element){
    const item_current_div = document.getElementById("item_current_div")

    item_current_div.children[0].textContent = element["Name"]
    item_current_div.children[2].textContent = element["Name"]

    item_current_div.children[3].textContent = element["Price"]
    item_current_div.children[4].textContent = `Quantity: ${element["Quantity"]}`

    item_current_div.children[6].textContent = element["MetaData"]["description"]

    const timestamp = element["Timestamp"]
    if (element["url"] !== undefined){
        item_current_div.children[1].children[0].src = element["url"]
    }
    item_current_div.children[1].children[0].alt = timestamp
}

function loadItemPage(element) {
    itemPageDivs(element)
}

function loadItem(timestamp){
    const json_form = new FormData
    const json_object = {
        data: {
            timestamp: timestamp
        },
        sql_method: "select_one"
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
            loadItemPage(data)
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error)
        })
}

const url_param = new URLSearchParams(window.location.search)
const item_id = url_param.get("id")

loadItem(item_id)