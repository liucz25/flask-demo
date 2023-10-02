from flask.views import MethodView
from models import Book
from flask import request
from extension import db


class BookApi(MethodView):
    def get(self,book_id):
        if not book_id:
            books:[Book]=Book.query.all()
            results=[
                {
                    'id':book.id,
                    'book_name':book.book_name,
                    'book_type':book.book_type,
                    'book_price':book.book_price,
                    'book_number':book.book_number,
                    'book_publisher':book.book_publisher,
                    'author':book.author
                }for book in books
            ]
            return {
                'status':"success",
                'message':'数据查询成功',
                'result':results
            }
        else:
            # return "dantiao"
            book:[Book]=Book.query.get(book_id)
            return {
                'status':"success",
                'message':'数据查询成功',
                'result':[
                {
                    'id':book.id,
                    'book_name':book.book_name,
                    'book_type':book.book_type,
                    'book_price':book.book_price,
                    'book_number':book.book_number,
                    'book_publisher':book.book_publisher,
                    'author':book.author
                }
            ]                
            }

    def post(self):
        form =request.json
        # print(form)
        book=Book()
        book.book_name      = form.get('book_name')
        book.book_type      = form.get('book_type')
        book.book_price     = form.get('book_price')
        book.book_number    = form.get('book_number')
        book.book_publisher   = form.get('book_publisher')
        book.author         = form.get('author')
        # print(book.author,book.book_name,book.book_number,book.book_price,book.book_price,book.book_publisher)
        db.session.add(book)
        db.session.commit()
        return {
                'status':"success",
                'message':'数据添加成功'}
    def delete(self,book_id):
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
        return {
                'status':"success",
                'message':'数据删除成功'}
    def put(self,book_id):
        print("_________________________________________")
        print(book_id)
        book:[Book]=Book.query.get(book_id)
        form =request.json
        print(form.get('book_name'))
        book.book_name      = form.get('book_name')
        book.book_type      = form.get('book_type')
        book.book_price     = form.get('book_price')
        book.book_number    = form.get('book_number')
        book.book_publisher   = form.get('book_publisher')
        book.author         = form.get('author')
        db.session.commit()
        return {
                'status':"success",
                'message':'数据z修改成功'}