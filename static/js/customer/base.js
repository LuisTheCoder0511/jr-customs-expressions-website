const options = {
    method: 'POST'
}

function fetchCustomerContent(name, params = null){
    const context = `customer/${name}`
    let location = window.location.toString()
    const index = location.lastIndexOf("customer")

    if (index !== -1){
        location = location.slice(0, index)
    }

    let newURL = location + context
    if (params !== null){
        newURL += params
    }
    window.location.href = newURL
}

function customerReplacement(){
    document.getElementById("content").innerHTML = document.getElementById("replace_content").innerHTML
    document.getElementById("replace_content").remove()
}