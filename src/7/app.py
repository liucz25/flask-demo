from flask import Flask,render_template,request,url_for,abort,redirect


"""
重定向和错误
"""
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index7.html')

@app.route('/login',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        if request.form['username']=='admin':
            return redirect(url_for('success'))
        else :
            abort(401)
    elif request.method == "GET":
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'log in successfully Admin'


if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    