from flask import Flask, render_template, request, redirect, session

app = Flask(__name__ , template_folder="./templates")
#TODO 加密掩码随机字符
app.secret_key = "fvdnjsdnoajfvoikvdafs"

@app.route('/login',methods=['GET', 'POST'])

def login():
    if request.method =='GET':
        return render_template('login.html')
    #TODO 获取POST中传来的值 requset。args是获取GET传来的值
    user = request.form.get('user')
    pwd = request.form.get('pwd')

    #真实情况应与数据库联动 从数据库中动态查询账号密码
    if user == '123' and pwd == '123':
        #TODO 加密放入cook 通过加密防止直接进入index页面
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', **{'msg': '用户名密码错误'})


@app.route('/index',methods=['GET', 'POST'])

def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    return "欢迎登录"

@app.route('/logout',methods=['GET', 'POST'])

def logout():
    del session['user_info']
    return redirect('/login')

    return "欢迎登录"

if __name__=='__main__':
    app.run()