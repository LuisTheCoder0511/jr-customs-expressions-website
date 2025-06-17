const click_a = document.getElementById("click_a")
const click_div = document.getElementById("click_div")
const submit_text = document.getElementById("submit_text")

const username = document.getElementById("username")
const password = document.getElementById("password")
const login_input_password2 = document.getElementById("login_input_password2")
const password2 = document.getElementById("password2")

let register = false

click_a.addEventListener("mousedown", e => {
    if (e.button !== 0) return
    register = !register
    if (register){
        click_div.textContent = "Already have an account?"
        click_a.textContent = "Login here!"

        submit_text.textContent = "Register"
        login_input_password2.style.visibility = "visible"
    } else {
        click_a.textContent = "Register here!"
        click_div.textContent = "Don't have an account?"

        submit_text.textContent = "Login"
        login_input_password2.style.visibility = "hidden"
    }
})

submit_text.addEventListener("mousedown", e => {
    if (e.button !== 0) return
    let pass = true

    if (username.value === "") {
        window.alert("Username is required!")
        pass = false
    }

    if (password.value === ""){
        window.alert("Password is required!")
        pass = false
    }

    if (register && password.value !== password2.value){
        window.alert("Password does not match!")
        pass = false
    }

    if (!pass) return

    let method = "register"
    if (!register) method = "login"

    const form = new FormData()
    const data = {
        data: {
            username: username.value,
            raw_password: password.value
        }
    }
    form.append("data", JSON.stringify(data))
    options.body = form

    fetch("/api/" + method, options)
        .then(r => r.json())
        .then(data => {
            if (data["redirect"]){
                window.location.href = "/"
            }
        })
})