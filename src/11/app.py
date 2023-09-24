from flask import Flask,make_response,request,flash,redirect,url_for,render_template
from werkzeug.utils import secure_filename
import os
"""
文件上传
"""
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploaddir/'

@app.route('/')
def upload_file():
    return render_template('upload11.html')
@app.route('/uploader',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        f=request.files['file111']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return "file uploaded successfully"
    elif request.method == 'GET':
        return render_template('upload11.html')


if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    