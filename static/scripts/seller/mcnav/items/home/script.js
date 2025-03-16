let item_limit = 50
let page = 1
let state = sessionStorage.getItem("state")
if (state === null) state = "home"
console.log("State: " + state)

let edit_state = 0

async function get() {
    const item_offset = (page - 1) * item_limit
    const data = {
        limit: item_limit,
        offset: item_offset,
        filter: "",

        arg: "get_all"
    };
    console.log(data)

    try {
        const response = await fetch("/seller-item/", {
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

if (state === "home") {
    refresh()
}

function refresh(){
    const container = document.getElementById("seller_item_container")
    container.innerHTML = "";
    const loading_div = document.createElement("div")
    loading_div.id = "seller_item_loading"
    loading_div.textContent = "Loading..."
    container.appendChild(loading_div)
    get_items()
}

function get_items() {
    console.log("Trying to refresh")
    get().then(x => {
        const item_query = x["get"]
        console.log(item_query)
        for (let key in item_query) {
            const item = item_query[key]
            createItemDiv(item)
        }
        const container = document.getElementById("seller_item_container")
        let loadingChild = container.children.namedItem("seller_item_loading")
        if (loadingChild !== null) container.removeChild(loadingChild)
    })
}

function switchEditState(state){
    optionDiv(false);
    if (edit_state === state) edit_state = 0;
    else edit_state = state;
    optionDiv(true);
}

function optionDiv(targetDiv){
    if (edit_state === 0) return;
    let div;
    switch (edit_state){
        case 1:
            div = document.getElementById("enable");
            break;
        case 2:
            div = document.getElementById("disable");
            break;
        case 3:
            div = document.getElementById("delete");
            break;
    }

    let color = null;
    if (targetDiv){
        if (edit_state === 1){
            color = "yellow";
        } else if (edit_state === 2){
            color = "blue";
        } else {
            color = "red";
        }
    }
    div.style.backgroundColor = color;
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
    item_anchor.className = "seller_item_a"


    const top_div = document.createElement("div")
    top_div.className = "seller_item_top_div"

    const item_image = document.createElement("img")
    item_image.className = "seller_item_img"
    const array = new Uint8Array(Object.values(item_img))
    const item_img_raw = new Blob([array], {type: 'image/png'})
    const url = URL.createObjectURL(item_img_raw)
    console.log(url)
    item_image.src = url
    item_image.draggable = false

    item_image.onload = () => URL.revokeObjectURL(url)

    top_div.appendChild(item_image)


    const bottom_div = document.createElement("div")
    bottom_div.className = "seller_item_bottom_div"

    const title_label = document.createElement("label")
    title_label.className = "seller_item_title"
    title_label.textContent = item_name

    const quantity_label = document.createElement("label")
    quantity_label.className = "seller_item_quantity"
    let text = "In stock"
    if (item_quantity === 0) text = "Sold out!"
    quantity_label.textContent = text

    const price_label = document.createElement("label")
    price_label.className = "seller_item_price"
    price_label.textContent = "$" + item_price

    const active_label = document.createElement("label")
    active_label.className = "seller_item_active"
    active_label.textContent = `Item is ${item_meta.active ? "active" : "inactive"}`


    bottom_div.appendChild(title_label)
    bottom_div.appendChild(quantity_label)
    bottom_div.appendChild(price_label)
    bottom_div.appendChild(active_label)


    item_anchor.appendChild(top_div)
    item_anchor.appendChild(bottom_div)

    console.log(item_anchor)
    const container = document.getElementById("seller_item_container")
    container.appendChild(item_anchor)
}