replacement()

function feature(){
    console.log("Feature selected")
    changeColor(".item_div_feature")
}

function select(){
    console.log("Select selected")
    changeColor(".item_div_select")
}

function changeColor(elementString){
    const element = document.querySelector(elementString)
    const targetColor = "gray"
    if (element.style.backgroundColor === targetColor) element.style.backgroundColor = ""
    else element.style.backgroundColor = targetColor
}

document.querySelectorAll("span").forEach(span => {
    span.addEventListener("click", e => {
        e.stopPropagation()
    })
})