const nav = document.querySelector('.mcnav_seller_content')
fetch("mcnav/items")
.then(res=>res.text())
.then(data => {
    nav.innerHTML=data
})