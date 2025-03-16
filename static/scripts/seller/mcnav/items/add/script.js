const input = document.getElementById("fileInput")
const image_input = document.getElementById("image_input")
let byteArray = null
input.addEventListener("input", inputFunction)

function inputFunction(event){
    const maxWidth = 1000
    const maxHeight = 1000

    const inputValue = event.target.files[0]
    console.log("Input:", inputValue)

    const reader = new FileReader()
    reader.onload = (e) => {
        const img = new Image()
        img.src = e.target.result

        img.onload = () => {
            const width = img.width
            const height = img.height
            if (width > maxWidth || height > maxHeight){
                alert("Image dimensions exceeds size of 1000x1000")
            } else {
                image_input.src = img.src
                inputValue.arrayBuffer().then(buffer => {
                    byteArray = new Uint8Array(buffer);
                });
            }
        }
    }

    reader.readAsDataURL(inputValue)

    event.target.files[0] = null
    event.target.value = null
}

function openFile() {
    input.click()
}

document.getElementById("upload-button-a").addEventListener("click", upload);

async function upload() {
    let responseElement = ""
    const data = {
        name: document.getElementById("name-text").value,
        description: document.getElementById("description-text").value,
        image: byteArray,
        categoryIDs: [],
        price: parseFloat(document.getElementById("price-text").value),
        quantity: parseInt(document.getElementById("quantity-text").value, 10),
        meta: {active: true},

        arg: "add"
        // category: document.getElementById("category-text").value
    };

    try {
        const response = await fetch("/seller-item/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('Network response was not ok');
        const responseData = await response.json();
        const responseJSON = JSON.stringify(responseData)
        responseElement = 'Response: ' + responseJSON;
        console.log(responseElement)
        let message = ""
        switch (responseData["status"]){
            case "success":
                message = "Item added successfully!"
                break
            case "price error":
                message = "Item price must be entered correctly (for example: 9.99)."
                break
            case "quantity error":
                message = "Item quantity must be entered correctly (for example: 12)."
                break
            case "name empty":
                message = "Item name cannot be empty!"
                break
            case "name required":
                message = "Item name is required!"
                break
            case "name error":
                message = "Item name not allowed! Try again with a different name!"
                break
            case "image required":
                message = "Item image is required!"
                break
            case "price free":
                message = "Item price cannot be free"
                break
            case "price required":
                message = "Item price is required!"
                break
            case "quantity 0":
                message = "Item quantity cannot be 0"
                break
            case "quantity required":
                message = "Item quantity is required!"
                break

        }
        if (responseData["status"] === "succes"){
            message = "Item added successfully!"
        }
        alert(message)
    } catch (error) {
        alert("Oh no! Something went wrong!")
    }
}
