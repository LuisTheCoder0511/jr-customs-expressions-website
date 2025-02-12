
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
}
let remember_me_value = true;

function register_page(){
    window.location.replace("/login/register")
}

function login_page(){
    window.location.replace("/login/")
}

function register(){
    username()
        .then(r => )
    // window.location.replace("/")
}

function login(){
    alert("Login intruder!")
    window.location.replace("/")
}

async function username(){
    let username = document.getElementById("login_username").value

    options.body = JSON.stringify({username: username})

    await fetch("/login/submit-username", options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));

    console.log(username)
}

async function password(){
    let password = document.getElementById("login_password").value

    options.body = JSON.stringify({password: password})

    await fetch("/submit-password", options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));

    console.log(password)
}

function remember_me(){
    let visibility = "hidden"
    remember_me_value = !remember_me_value
    if (remember_me_value) visibility = "visible"
    document.getElementById("checkmark").style.visibility = visibility
}

remember_me()