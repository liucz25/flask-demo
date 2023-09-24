from flask import Flask,render_template,url_for
"""
模板 结构化
"""
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index4.html")




if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    