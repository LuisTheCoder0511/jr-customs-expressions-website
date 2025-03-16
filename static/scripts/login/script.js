
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
}
let remember_me_value = true;

function register_page(){
    window.location.replace("/register")
}

function login_page(){
    window.location.replace("/login")
}

function register(username, password){
    submit(username, password).then()
    window.location.replace("/")
}

function login(username, password){
    submit(username, password).then()
    alert("Login intruder!")
    window.location.replace("/")
}

async function submit(username, password){
    console.log("submitting")
    options.body = JSON.stringify({data: [username, password]})

    await fetch("/submit-data", options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

function remember_me(){
    let visibility = "hidden"
    remember_me_value = !remember_me_value
    if (remember_me_value) visibility = "visible"
    document.getElementById("checkmark").style.visibility = visibility
}

remember_me()