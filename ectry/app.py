from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def h1():
    return render_template("h1.html")

if __name__ == "__main__":
    app.run()
