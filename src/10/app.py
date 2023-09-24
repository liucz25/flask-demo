from flask import Flask,make_response,request,flash,redirect,url_for,render_template


"""
消息闪现
"""
app=Flask(__name__)

app.secret_key='12345678'  # secrect 对 secert 错
@app.route('/')
def index():
    return render_template('index10.html')
@app.route('/login',methods=['GET','POST'])
def login():
    errorMsg =None

    if request.method == 'POST':
        if request.form['username']!='admin' or request.form['password']!="123":
            errorMsg="用户名，密码错误，必须为admin 123"
        else:
            flash("You were successfully logged in !")
            return redirect(url_for('index'))

    return render_template('login.html',error = errorMsg)
    # return render_template('login.html',code = errorMsg)# 可以

if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    