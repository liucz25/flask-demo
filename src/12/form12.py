from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField,EmailField
# from wtforms.fields import html5
from wtforms import validators

class ContactForm(FlaskForm):
    name = StringField("Name of Student",[validators.DataRequired("Please enter your name.")])
    # name = StringField("Name of Student")
    gender=RadioField("Gender",choices=[('M','Male'),('f','Female')])
    address =TextAreaField("Address")
    # email=EmailField("Email:",[validators.DataRequired(message="输入Email。")]) 
    email=EmailField("Email:") 
    age=IntegerField("age")
    languages=SelectField("Languages",choices=[('cpp','C++'),('py','Python')])
    submit=SubmitField("Send")