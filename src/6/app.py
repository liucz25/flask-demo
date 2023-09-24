from flask import Flask,render_template,request
from werkzeug.wrappers.response import ResponseStream

"""
将表单数据发送到模板
"""
app=Flask(__name__)

@app.route('/')
def student():
    return render_template('index5.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        rst=request.form
        # print(rst)
        return render_template("result5.html",result=rst)



if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    