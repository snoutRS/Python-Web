from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    d1 ={
        "学院":['国际', '海天', '工管', '海天', '艺术', '电信'],
        "销量":[90, 70, 55, 100, 60, 70, 90],
        "进货量":[80, 60, 65, 80, 90, 70, 30]
    }
    a = [90, 70, 55, 100, 60, 70, 90]
    name = ['产品1', '产品2', '产品3', '产品4', '产品5', '产品6', '产品7']
    return render_template("hello.html", a=a, name=name, d1=d1)


if __name__ == '__main__':
    app.run()

