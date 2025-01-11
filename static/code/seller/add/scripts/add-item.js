document.getElementById("upload-button-a").addEventListener("click", async () => {
    let responseElement = ""
    const data = {
        name: document.getElementById("name-text").value,
        description: document.getElementById("description-text").value,
        price: +document.getElementById("price-text").value,
        quantity: parseInt(document.getElementById("quantity-text").value, 10),
        item_type: document.getElementById("type-text").value
    };
    console.log(data)

    try {
        const response = await fetch("/seller#add", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        if (!response.ok) throw new Error('Network response was not ok');
        const responseData = await response.json();
        responseElement = 'Response: ' + JSON.stringify(responseData);
        console.log(responseElement)
        alert("Item added successfully!")
    } catch (error) {
        alert("Something went wrong!")
    }
});
