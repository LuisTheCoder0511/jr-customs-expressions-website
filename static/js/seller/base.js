const options = {
    method: 'POST'
}

function fetchSellerContent(name, params = null){
    const context = `seller/${name}`
    let location = window.location.toString()
    const index = location.lastIndexOf("seller")

    if (index !== -1){
        location = location.slice(0, index)
    }

    let newURL = location + context
    if (params !== null){
        newURL += params
    }
    window.location.href = newURL
}

function sellerReplacement(){
    document.getElementById("seller_management_content").innerHTML = document.getElementById("seller_management_replace_content").innerHTML
    document.getElementById("seller_management_replace_content").remove()
}