from flask import Flask, render_template

app = Flask(__name__)


@app.route("/1")
def macrol1():
    return  render_template("h1.html")

@app.route("/2")
def macrol2():
    return  render_template("h2_user.html")

@app.route("/3")
def macrol3():
    return  render_template("h3_user.html")

if __name__ == "__main__":
    app.run()
