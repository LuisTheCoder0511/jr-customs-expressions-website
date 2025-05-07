let previousContent = null
let itemTemplate = ""
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
}

function fetchHomeContent(name){
    document.getElementById("content").innerHTML = ""

    if (previousContent !== null){
        unloadCSS(`${previousContent}/style.css`)
        unloadScript(`${previousContent}/script.js`)
    }

    loadCSS(`${name}/style.css`)
    loadScript(`${name}/script.js`)

    fetch(`/content/${name}`)
        .then(r => r.text())
        .then(text => {
            document.getElementById("content").innerHTML = text
        })

    previousContent = name
}

function loadCSS(url) {
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = url
    link.id = "dynamicCSS"
    document.head.appendChild(link)
}

function unloadCSS() {
    const link = document.getElementById("dynamicCSS")
    if (link){
        link.remove()
    }
}

function loadScript(url) {
    try {
        const script = document.createElement('script')
        script.src = url
        script.id = "dynamicScript"
        document.head.appendChild(script)
    } catch (error) {
        print("Script doesn't exist")
    }
}

function unloadScript() {
    const script = document.getElementById('dynamicScript')
    if (script){
        script.remove()
    }
}
