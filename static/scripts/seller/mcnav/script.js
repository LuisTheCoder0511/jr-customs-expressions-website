const options = {method: "POST", headers: {"Content-Type": "application/json"}}

async function changeIframe(newSrc, extraArg){
    options.body = JSON.stringify({arg: newSrc, arg_extra: extraArg})
    fetch("/mcnav/", options)
        .then(response => response.text())
        .then(html => {
            const iframe = document.getElementById("seller_content_frame");
            iframe.srcdoc = html;
        })
        .catch(error => console.error("error:", error));
}