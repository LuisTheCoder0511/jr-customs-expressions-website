function itemsHTML(){
    const nav = document.querySelector('.sub-content')
    fetch("base/items")
    .then(res=>res.text())
    .then(data => {
        nav.innerHTML=data
    })
}

itemsHTML()