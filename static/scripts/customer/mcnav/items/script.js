let item_limit = 50
let page = 1
const container = document.getElementById("customer_item_container")
let loadingChild = container.children.namedItem("customer_item_loading")

async function item_fetch() {
    const item_offset = (page - 1) * item_limit
    const data = {
        limit: item_limit,
        offset: item_offset,
        filter: "",

        arg: "get_all"
    };
    console.log(data)

    try {
        const response = await fetch("/customer-item/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json()
    } catch (error) {
        alert("Oh no! Something went wrong!")
    }
}

function get_items() {
    console.log("Trying to refresh")
    item_fetch().then(x => {
        const item_query = x["get"]
        console.log(item_query)
        for (let key in item_query) {
            const item = item_query[key]
            createItemDiv(item)
        }
        if (loadingChild !== null) container.removeChild(loadingChild)
    })
}

function createItemDiv(data){
    const item_name = data["name"]
    const item_img = data["image"]
    const item_price = data["price"]
    const item_quantity = data["quantity"]
    const item_meta = data["meta"]
    console.log(data)


    const item_anchor = document.createElement("a")
    item_anchor.id = name
    item_anchor.className = "customer_item_a"


    const top_div = document.createElement("div")
    top_div.className = "customer_item_top_div"

    const item_image = document.createElement("img")
    item_image.className = "customer_item_img"
    const array = new Uint8Array(Object.values(item_img))
    const item_img_raw = new Blob([array], {type: 'image/png'})
    const url = URL.createObjectURL(item_img_raw)
    console.log(url)
    item_image.src = url
    item_image.draggable = false

    item_image.onload = () => URL.revokeObjectURL(url)

    top_div.appendChild(item_image)


    const bottom_div = document.createElement("div")
    bottom_div.className = "customer_item_bottom_div"

    const title_label = document.createElement("label")
    title_label.className = "customer_item_title"
    title_label.textContent = item_name

    const quantity_label = document.createElement("label")
    quantity_label.className = "customer_item_quantity"
    let text = "In stock"
    if (item_quantity === 0) text = "Sold out!"
    quantity_label.textContent = text

    const price_label = document.createElement("label")
    price_label.className = "customer_item_price"
    price_label.textContent = "$" + item_price

    const active_label = document.createElement("label")
    active_label.className = "customer_item_active"
    active_label.textContent = `Item is ${item_meta.active ? "active" : "inactive"}`


    bottom_div.appendChild(title_label)
    bottom_div.appendChild(quantity_label)
    bottom_div.appendChild(price_label)
    bottom_div.appendChild(active_label)


    item_anchor.appendChild(top_div)
    item_anchor.appendChild(bottom_div)

    console.log(item_anchor)
    container.appendChild(item_anchor)
}