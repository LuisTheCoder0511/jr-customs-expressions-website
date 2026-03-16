let product_method = ""
let product_images = []

function loadProducts(){
    const list = document.getElementsByClassName("product_template_click")
    const iterator = list[Symbol.iterator]()
    let element = iterator.next()
    while (!element.done){
        const template = element.value
        template.addEventListener("mousedown", e => {
            if (e.button !== 0) return
            document.getElementById("product_edit_window").style.visibility = "visible"
            product_method = "update"
        })
        element = iterator.next()
    }
}

function loadImage(json_source, element){
    element.src = json_source.img
    element.dataset.hasImage = "true"
    element.style.display = "block"

}

document.getElementById("products_add_button").addEventListener("mousedown", e => {
    if (e.button !== 0) return
    document.getElementById("product_edit_window").style.visibility = "visible"
    product_method = "insert"
    product_images = []
})

document.getElementById("submit_button").addEventListener("mousedown", e => {
    if (e.button !== 0) return

    const data = {
        data: {
            product_name: document.getElementById("product_edit_name").value,
            product_price: document.getElementById("product_edit_price").value,
            product_quantity: document.getElementById("product_edit_quantity").value,
            product_data: {
                description: document.getElementById("product_edit_description").value
            },
        }
    }

    for (let i = 1; i <= 7; i++){
        let imageElement = document.getElementById("image" + i)
        if (imageElement.dataset.hasImage === "true"){
            product_images[i] = imageElement.src
        }
    }

    const formData = newFormData(data, product_images)
    options.body = formData

    console.log(formData.get("data"))
    console.log(formData.get("files[]"))

    // fetch("/api/products/" + product_method)
    //     .then(result => result.text())
    //     .then(data => {
    //         console.log(data)
    //         window.alert("Submit complete!")
    //     })
})


document.getElementById("product_edit_window_close").addEventListener("mousedown", e => {
    if (e.button !== 0) return
    document.getElementById("product_edit_window").style.visibility = "hidden"
})

let i = 1
while (i <= 7) {
    let imageInput = document.getElementById("imageInput" + i)
    let imageElement = document.getElementById("image" + i)

    imageInput.addEventListener('change', event => {
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
                }
                loadImage(json_source, imageElement)
            }

            reader.readAsDataURL(file)

        } else {
            alert("Please select a valid image file.")
        }
    })
    i++
}

loadProducts()