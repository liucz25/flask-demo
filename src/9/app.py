from flask import Flask,make_response,request,session,redirect,url_for,render_template


"""
Session
"""
app=Flask(__name__)

app.secret_key='12345678'  # secrect 对 secert 错
@app.route('/')
def index():
    if 'username' in session:
        print("===============",session)
        user=session['username']
        # return "登录用户名是： %s <br><b><a href='/logout'>点击这里登出",user  #这样不行，不是print 不支持格式化输出
        return "登录用户名是： "+user+" <br><b><a href='/logout'>点击这里登出"
    return "您暂未登录， <br><b><a href='/login'>点击这里登录"
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    elif request.method =='GET':
        return render_template('index9.html')
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))



if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    