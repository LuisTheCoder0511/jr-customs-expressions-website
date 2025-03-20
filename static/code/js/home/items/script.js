async function loadTemplate() {
    if (itemTemplate !== "") return
    options.body = ""
    await fetch("/item")
        .then(response => response.text())
        .then(data => {
            itemTemplate = data
        })
}

function loadItems(){
    options.body = JSON.stringify({
        sql_method: "select_all",
        offset: 0,
        limit: 5,
        data: {
            name: ""
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
            data.forEach(element => {
                const item_div = document.createElement("div")
                item_div.className = "item_div"
                item_div.innerHTML = itemTemplate
                item_div.children[1].textContent = element[1]
                item_div.children[2].textContent = element[2]
                item_div.children[3].textContent = `Quantity: ${element[3]}`
                document.getElementById("item_content").appendChild(item_div)
            })
            console.log(data)
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error)
        })
}

loadTemplate().then()
loadItems()