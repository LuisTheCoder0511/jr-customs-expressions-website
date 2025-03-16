from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    PORT = 8001
    app.run(port=PORT, debug=True)
