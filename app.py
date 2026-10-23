from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Actualizacion de mensaje, uso de docker."


if __name__ == "__main__":
    app.run()