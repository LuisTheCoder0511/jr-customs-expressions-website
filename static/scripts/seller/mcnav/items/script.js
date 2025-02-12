function createItemDiv(name){
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
    title_label.textContent = "Name of the item"

    const quantity_label = document.createElement("label")
    quantity_label.className = "seller_item_quantity"
    quantity_label.textContent = "Quantity in stock"

    const price_label = document.createElement("label")
    price_label.className = "seller_item_price"
    price_label.textContent = "$6.99"

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

createItemDiv("item1")
createItemDiv("item2")
createItemDiv("item3")
createItemDiv("item4")
createItemDiv("item5")
createItemDiv("item6")