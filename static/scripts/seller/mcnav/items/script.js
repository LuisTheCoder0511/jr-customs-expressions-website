let item_limit = 50
let page = 1

async function get() {
    const item_offset = (page - 1) * item_limit

    let responseElement = ""
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

get().then(x => {
    const item_query = x["get"]
    console.log(item_query)
    for (let key in item_query){
        const item = item_query[key]
        createItemDiv(item)
    }
})


function createItemDiv(data){
    const item_name = data[1]
    const item_description = data[2]
    const item_img = data[3]
    const item_cat = data[4]
    const item_price = data[5]
    console.log(data)
    const item_quantity = data[6]


    const div = document.createElement("div")
    div.id = name
    div.className = "seller_item_div"

    const item_a = document.createElement("a")
    item_a.className = "seller_item_a"

    const item_image = document.createElement("img")
    item_image.className = "seller_item_img"
    item_image.src = "/static/assets/images/blank highlight.jpg"

    const label_div = document.createElement("div")
    label_div.className = "seller_item_label_div"

    const title_label = document.createElement("label")
    title_label.className = "seller_item_title"
    title_label.textContent = item_name

    const quantity_label = document.createElement("label")
    quantity_label.className = "seller_item_quantity"
    let text = "Quantity in stock"
    if (item_quantity === 0) text = "Sold out!"
    quantity_label.textContent = text

    const price_label = document.createElement("label")
    price_label.className = "seller_item_price"
    price_label.textContent = "$" + item_price

    label_div.appendChild(title_label)
    label_div.appendChild(quantity_label)
    label_div.appendChild(price_label)

    item_a.appendChild(item_image)
    item_a.appendChild(label_div)

    const item_div = document.createElement("div")
    item_div.className = "seller_item_bottom_div"

    const select = document.createElement("a")
    select.className = "seller_item_select"

    const select_image = document.createElement("img")
    select_image.src = "/static/assets/images/checkmark.png"

    select.appendChild(select_image)

    const feature = document.createElement("a")
    feature.className = "seller_item_feature"

    const feature_image = document.createElement("img")
    feature_image.src = "/static/assets/images/feature.png"

    feature.append(feature_image)

    item_div.appendChild(select)
    item_div.appendChild(feature)

    div.appendChild(item_a)
    div.appendChild(item_div)

    console.log(div)
    document.getElementById("seller_item_container").appendChild(div)
}

// createItemDiv("item1")
// createItemDiv("item2")
// createItemDiv("item3")
// createItemDiv("item4")
// createItemDiv("item5")
// createItemDiv("item6")