const nav = document.querySelector('.header')
fetch("base/header")
.then(res=>res.text())
.then(data => {
    nav.innerHTML=data
})