from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=80,debug=True)