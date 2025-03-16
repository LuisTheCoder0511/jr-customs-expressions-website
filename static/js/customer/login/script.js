let remember = "hidden"
let register = false
const form = document.getElementById('login_form')


document.getElementById("login_username").addEventListener("keypress", e => eventEnter(e))
document.getElementById("login_password").addEventListener("keypress", e => eventEnter(e))
// document.getElementById("login_name").addEventListener("keypress", e => eventEnter(e))


function eventEnter(e){
    if (e.key === "Enter") {
        document.getElementById("login_form").submit()
    }
}

function remember_me() {
    if (remember === "hidden") remember = "visible"
    else remember = "hidden"

    document.getElementById("checkmark").style.visibility = remember
    document.getElementById("checkmarkVisibility").value = remember
}

function register_switch(){
    register = !register;
    const forgot = document.getElementById("forgot")
    const login_button = document.getElementById("login_button")
    const login_welcome_text = document.getElementById("login_welcome_text")
    const other_login_text = document.getElementById("other_login_text")
    const other_login_link = document.getElementById("other_login_link")
    const third_party_logins_label = document.getElementById("third_party_logins_label")
    const register_input = document.getElementById("register")
    if (register){
        register_input.value = "true"
        forgot.style.visibility = "hidden"
        login_button.textContent = "Register"
        login_welcome_text.textContent = "Sign up"
        third_party_logins_label.textContent = "Sign up with"
        other_login_text.textContent = "Already have an account?"
        other_login_link.textContent = "Sign in!"
        fetchNameLabel().then()
    } else {
        register_input.value = "false"
        forgot.style.visibility = "visible"
        login_button.textContent = "Login"
        login_welcome_text.textContent = "Login"
        third_party_logins_label.textContent = "Sign in with"
        other_login_text.textContent = "Don't have an account?"
        other_login_link.textContent = "Sign up!"
        form.removeChild(document.getElementById("login_name_label"))
    }
}

async function fetchNameLabel() {
    await fetch("/login_label/name")
        .then(r => r.text())
        .then(data => {
            const tempDiv = document.createElement('div')
            tempDiv.innerHTML = data
            form.prepend(tempDiv.children[0])
        })
}