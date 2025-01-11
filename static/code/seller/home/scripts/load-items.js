let responseElement = ""

try {
    const response = await fetch("/seller#get", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Device": "Web"
        }
    });
    if (!response.ok) throw new Error('Network response was not ok');
    const responseData = await response.json();
    responseElement = 'Response: ' + JSON.stringify(responseData);
    // const data = {
    //     name: document.getElementById("name-text").value,
    //     description: document.getElementById("description-text").value,
    //     price: +document.getElementById("price-text").value,
    //     quantity: parseInt(document.getElementById("quantity-text").value, 10),
    //     item_type: document.getElementById("type-text").value
    // };
    console.log(responseElement)
    alert("Items loaded successfully!")
} catch (error) {
    alert("Something went wrong!")
}