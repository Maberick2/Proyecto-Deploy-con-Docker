from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "return API funcionando en Azure."


if __name__ == "__main__":
    app.run()