from flask import Flask,request,flash,render_template,redirect
from form13 import ContactForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import StringField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField,EmailField,HiddenField
from flask_wtf import FlaskForm
from wtforms import validators

"""
SQLAlchemy
"""
app=Flask(__name__)
# app.config['secret_key']='12345678'
app.secret_key='12345678'  # secrect 对 secert 错
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contacts.db'



db=SQLAlchemy(app)

class ContactDAO(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(1))
    address = db.Column(db.String(100))
    email = db.Column(db.String(50))
    age = db.Column(db.String(5))
    language=db.Column(db.String(20))
    date_created  = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,name,gender,address,email,age,language):
        self.name=name
        self.gender=gender
        self.address=address
        self.email=email
        self.age=age
        self.language=language
        

class ContactForm(FlaskForm):
    id = HiddenField("id")
    name = StringField("Name of Student",[validators.DataRequired("Please enter your name.")])
    # name = StringField("Name of Student")
    gender=RadioField("Gender",choices=[('M','Male'),('f','Female')])
    address =TextAreaField("Address")
    # email=EmailField("Email:",[validators.DataRequired(message="输入Email。")]) 
    email=EmailField("Email:") 
    age=IntegerField("age")
    languages=SelectField("Languages",choices=[('cpp','C++'),('py','Python')])
    submit=SubmitField("Send")






@app.route('/')
def show_all():
    form1=ContactForm()
    # print(ContactDAO.query.all()[0].data_create)
    return render_template('show13.html',contacts=ContactDAO.query.all(),form=form1)

@app.route('/add',methods=['POST','GET'])
def do_add():
    form1=ContactForm()
    if request.method == 'POST':
        if form1.validate()==False:
            flash('All fields are required.')
            return render_template("add13.html",form=form1)
        else:
            contact=ContactDAO(form1.name.data,
                               form1.gender.data,
                               form1.address.data,
                               form1.email.data,
                               form1.age.data,
                               form1.languages.data)
            try:
                db.session.add(contact)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                flash('there is an issue adding contact into db.{0}'.format(e))
                return render_template('add13.html',form=form1)
            
    elif request.method == 'GET':
        return render_template('add13.html',form=form1)        
@app.route('/delete/<int:id>')
def do_delete(id):
    to_delete=ContactDAO.query.get_or_404(id)
    try:
        db.session.delete(to_delete)
        db.session.commit()
    except Exception as e:
        flash('there is an issue deleteing contact into db.{0}'.format(e))
    return redirect("/")
    
@app.route('/update/<int:id>',methods = ['POST','GET'])
def do_update(id):
    form1=ContactForm()
    to_update=ContactDAO.query.get_or_404(id)

    if request.method =='GET':
        form1.id.data=to_update.id
        form1.name.data=to_update.name
        form1.gender.data=to_update.gender
        form1.address.data=to_update.address
        form1.email.data=to_update.email
        form1.age.data=to_update.age
        form1.languages.data=to_update.language
        return render_template('update13.html',form=form1) 

    elif request.method == 'POST':
        to_update.id=id
        to_update.name = form1.name.data
        to_update.gender = form1.gender.data
        to_update.address= form1.address.data
        to_update.email = form1.email.data
        to_update.age = form1.age.data
        to_update.language = form1.languages.data
      
        try:
            # db.session.save(to_update)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            flash('there is an issue updateing contact into db.{0}'.format(e))
            return redirect("/")   

if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
