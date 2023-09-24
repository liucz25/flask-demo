from flask import Flask
"""
路由
"""
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!"

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!'%name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number  %d!'%postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revsion number  %f!'%revNo

@app.route('/flask')#注意 flask 后边没有 / ,访问时加/  不能 访问到 
def hello_flask():
    return "Hello flask!"
@app.route('/python/') #注意 python 后边有 / ,这样写是标准的，访问时加不加/都能访问到 
def hello_python():
    return "Hello python!"
if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    