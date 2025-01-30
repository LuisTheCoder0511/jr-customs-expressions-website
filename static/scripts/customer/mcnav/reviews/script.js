function reviewsHTML(){
    const nav = document.querySelector('.sub-content')
    fetch("base/reviews")
    .then(res=>res.text())
    .then(data => {
        nav.innerHTML=data
    })
}