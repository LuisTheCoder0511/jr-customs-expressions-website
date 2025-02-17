const input = document.getElementById("fileInput")
const image_input = document.getElementById("image_input")
let byteArray = null
input.addEventListener("input", inputFunction)

function inputFunction(event){
    const inputValue = event.target.files[0]
    console.log("Input:", inputValue)

    const reader = new FileReader()
    reader.onload = function(e){
        image_input.src = e.target.result

        inputValue.arrayBuffer().then(buffer => {
            byteArray = new Uint8Array(buffer);
            console.log("Byte Array:", byteArray); // Log the byte array
        });
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
        price: document.getElementById("price-text").value,
        quantity: parseInt(document.getElementById("quantity-text").value, 10),
        meta: "",

        arg: "add"
        // category: document.getElementById("category-text").value
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
        const responseData = await response.json();
        const responseJSON = JSON.stringify(responseData)
        responseElement = 'Response: ' + responseJSON;
        console.log(responseElement)
        let message = "Item not added! It seems that the item is already in the database."
        if (responseData["success"] === true){
            message = "Item added successfully!"
        }
        alert(message)
    } catch (error) {
        alert("Oh no! Something went wrong!")
    }
}
