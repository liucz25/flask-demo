from flask import Flask,request,flash,render_template
from form12 import ContactForm

"""
WTF 表单
"""
app=Flask(__name__)

app.secret_key='12345678'  # secrect 对 secert 错
@app.route('/',methods=['GET','POST'])
def contact():
    form1=ContactForm()
    # print(form1)
    if request.method == 'POST':
        # print(form1.validate())
        if form1.validate()==False:
            flash("填写信息中存在错误，请检查。")
            return render_template('contact12.html',form=form1)
        else:
            print("========================pass")
            return render_template("success12.html")

    elif request.method == 'GET':
        return render_template('contact12.html',form=form1)
# @app.route('/login',methods=['GET','POST'])
# def p():
#     pass


if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    