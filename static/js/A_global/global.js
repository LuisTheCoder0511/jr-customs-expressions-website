const options = {
    method: 'POST'
}

window.addEventListener('pageshow', event => {
    if (event.persisted) {
        window.location.reload()
    }
})