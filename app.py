from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home/index.html")

@app.route("/content/<name>")
def content(name):
    template = f"home/{name}/index.html"
    print("Template:", template)
    return render_template(template)

if __name__ == "__main__":
    PORT = 8001
    app.run(port=PORT, debug=True)
