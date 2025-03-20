let previousContent = null
let itemTemplate = ""
const prefix = "/static/code/"
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
}

function fetchHomeContent(name){
    document.getElementById("content").innerHTML = ""

    if (previousContent !== null){
        unloadCSS(`${prefix}css/home/${previousContent}/style.css`)
        unloadScript(`${prefix}js/home/${previousContent}/script.js`)
    }

    loadCSS(`${prefix}css/home/${name}/style.css`)
    loadScript(`${prefix}js/home/${name}/script.js`)

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
  const script = document.createElement('script')
  script.src = url
  script.id = "dynamicScript"
  document.head.appendChild(script)
}

function unloadScript() {
    const script = document.getElementById('dynamicScript')
    if (script){
        script.remove()
    }
}
