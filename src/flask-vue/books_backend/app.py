from flask import Flask
from extension import db,cors
from models import Book
from bookapi import BookApi

app=Flask(__name__)
cors.init_app(app)#跨域
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)


@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()

@app.route('/')
def hello_world():
    return "Hello World !!!"

book_view =BookApi.as_view('book_api')
app.add_url_rule('/books/',defaults={'book_id':None},
                 view_func=book_view,methods=['GET',])
app.add_url_rule('/books/',view_func=book_view,methods=['POST',])
app.add_url_rule('/books/<int:book_id>',
                 view_func=book_view,methods=['GET','PUT','DELETE'])




if __name__=='__main__':
    app.run(debug=True)