const options = {
    method: 'POST'
}

window.addEventListener('pageshow', event => {
    if (event.persisted) {
        window.location.reload()
    }
})

function newFormData(data, files){
    const formData = new FormData()
    formData.append("data", JSON.stringify(data))
    if (files.length > 0){
        for (let i = 0; i < files.length; i++){
            const image = files[i]
            if (image !== null) {
                formData.append("files[]", files[i])
            }
        }
    }
    return formData
}