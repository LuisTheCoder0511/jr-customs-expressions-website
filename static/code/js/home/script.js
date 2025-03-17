let previousContent = null

function fetchContent(name){
    document.getElementById("content").innerHTML = ""

    if (previousContent !== null){
        unloadCSS(`/static/code/css/${previousContent}/style.css`)
    }

    loadCSS(`/static/code/css/${name}/style.css`)

    fetch(`/content/${name}`)
        .then(r => r.text())
        .then(text => {
            document.getElementById("content").innerHTML = text
        })

    previousContent = name;
}

function loadCSS(url) {
  const link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = url;
  document.head.appendChild(link);
}

function unloadCSS(url) {
  const links = document.querySelectorAll('link');
  links.forEach(link => {
    if (link.href.includes(url)) {
      link.remove();
    }
  });
}