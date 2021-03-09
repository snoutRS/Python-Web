from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

@app.route('/demo')
def tempdemo():
    return render_template('demo.html',name='aaa',msg='asdf')

@app.route('/demo1')
def tempdemo1():
    dict1={"name":"罗小黑","msg":"asdf"}
    return render_template('demo1.html',dict1=dict1)

@app.route('/demo2')
def tempdemo2():
    return render_template('demo2.html',i = 123,s = 'abc',s_list=['abc','abb','aaa'],d={"name":'aaa',"age":43})

@app.route('/demo3')
def tempdemo3():
    return render_template('demo3.html',name1='这是传入值',name2=False)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=80,debug=True)