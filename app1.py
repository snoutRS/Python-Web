from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/tempdemo')
def tempdemo():
    return render_template('demo.html',name='aaa',msg='asdf')

@app.route('/tempdemo1')
def tempdemo1():
    dict1={"name":"罗小黑","msg":"asdf"}
    return render_template('demo1.html',dict1=dict1)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=80,debug=True)