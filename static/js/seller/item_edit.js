sellerReplacement()

let categoriesMap = {}
let currentFile
let upload_method = "insert"
let timestamp_data

function loadImage(json_source){
    const preview = document.getElementById('preview');
    preview.src = json_source.img
    preview.dataset.hasImage = json_source.hasImage
    preview.style.display = 'block'
}

function addItemCategory(textValue){
    if (textValue in categoriesMap) return
    categoriesMap[textValue] = "Category"

    const div = document.createElement("div")
    div.className = "category_box"
    div.id = "id=" + textValue

    const text_div = document.createElement("div")
    text_div.className = "category_box_text"

    text_div.textContent = textValue

    div.appendChild(text_div)

    const div_delete = document.createElement("div")
    div_delete.className = "category_box_delete"

    const a = document.createElement("a")
    a.className = "category_box_click"
    a.addEventListener("click", () => {
        div.remove()
        delete categoriesMap[textValue]
        console.log(categoriesMap)
    })

    const img = document.createElement("img")
    img.className = "category_box_img"
    img.src = "/static/assets/images/x_icon.png"
    a.appendChild(img)
    div_delete.appendChild(a)
    div.appendChild(div_delete);

    document.getElementById("item_add_categories").appendChild(div)
}

function loadItemEditPage(data){
    const json_source = {
        img: data["url"],
        hasImage: data["HasImage"]
    }
    loadImage(json_source)
    currentFile = data["url"]

    document.getElementById("seller_management_content_title").textContent = "Edit Item"
    document.getElementById("nameInput").value = data["Name"]
    document.getElementById("descriptionInput").value = data["MetaData"]["description"]
    document.getElementById("priceInput").value = data["Price"]
    document.getElementById("quantityInput").value = data["Quantity"]

    const categoryData = data["MetaData"]["categories"]
    for (let key in categoryData){
        addItemCategory(key)
    }
}

function getImageEdit(timestamp) {
    timestamp_data = timestamp
    const json_form = new FormData
    const json_object = {
        data: {
            timestamp: timestamp
        },
        sql_method: "select_one"
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
            upload_method = "update"
            console.log(upload_method)
            loadItemEditPage(data)
        })
        .catch(error => {
            throw new Error("The item doesn't appear to exist: " + error)
        })
}


const url_param = new URLSearchParams(window.location.search)
const item_id = url_param.get("id")

if (item_id !== null) {
    getImageEdit(item_id)
}

document.getElementById('imageInput').addEventListener('change', function(event) {
    const fileInput = event.target;
    const files = fileInput.files;

    if (!files || files.length === 0) {
        // No file selected, so do nothing (and keep the previous one, if needed)
        return;
    }

    const file = files[0];

    if (file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = (e) => {
            const json_source = {
                img: e.target.result,
                hasImage: "1"
            }
            currentFile = file
            loadImage(json_source)
        }

        reader.readAsDataURL(file)

    } else {
        alert("Please select a valid image file.")
    }
})

document.getElementById("categoriesInput").addEventListener("keydown", e => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault()

        const textValue = document.getElementById("categoriesInput").value
        document.getElementById("categoriesInput").value = ""

        addItemCategory(textValue)
    }
})

document.getElementById("item_add_upload").addEventListener("click", async function() {
    const json_form = new FormData()
    const meta_data = {
        description: document.getElementById("descriptionInput").value,
        categories: categoriesMap
    }
    const json_object = {
        data: {
            name: document.getElementById("nameInput").value,
            price: document.getElementById("priceInput").value,
            quantity: document.getElementById("quantityInput").value,
            has_image: parseInt(document.getElementById('preview').dataset.hasImage),
            data: JSON.stringify(meta_data)
        },
        sql_method: upload_method
    }

    if (upload_method === "update"){
        json_object["data"]["timestamp"] = timestamp_data
    }

    console.log(meta_data)
    console.log(json_object["data"])

    json_form.append("file", currentFile)
    json_form.append("data", JSON.stringify(json_object))
    options.body = json_form

    await fetch("/seller/api/items", options)
        .then(r => r.text())
        .then(t => console.log(t))
})