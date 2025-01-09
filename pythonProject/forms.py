from flask_wtf import FlaskForm

from wtforms.fields import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, length, equal_to


class ProductForm(FlaskForm):

    name=StringField("შეიყვანეთ სათაური", validators=[DataRequired()])
    text=TextAreaField("ჩასვით ტექსტი", validators=[DataRequired()])
    img=StringField("ჩასვით ფოტო", validators=[DataRequired()])
    link = StringField("დატოვეთ ცარიელი")



    submit=SubmitField()

class RegisterForm(FlaskForm):
    username=StringField("ჩაწერეთ სახელი", validators=[DataRequired()])
    password=StringField("ჩაწერეთ პაროლი", validators=[DataRequired(), length(min=8, max=15)])
    repeat_password=PasswordField("გაიმეორეთ პაროლი", validators=[equal_to("password")])
    register=SubmitField("რეგისტრაცია")

class LoginForm(FlaskForm):
    username = StringField("ჩაწერეთ სახელი", validators=[DataRequired()])
    password = StringField("ჩაწერეთ პაროლი", validators=[DataRequired()])
    login = SubmitField("ავტორიზაცია")

class ThingForm(FlaskForm):
    text=TextAreaField("ჩასვით ტექსტი",validators=[DataRequired()])
    img=StringField("ჩასვით ფოტო",validators=[DataRequired()])
    link = StringField("დატოვეთ ცარიელი")
    submit=SubmitField()


class NewForm(FlaskForm):
    text=TextAreaField("ჩასვით ტექსტი",validators=[DataRequired()])
    img=StringField("ჩასვით ფოტო",validators=[DataRequired()])
    submit=SubmitField()

class TourForm(FlaskForm):
    name=TextAreaField("შეიყვანეთ სათაური",validators=[DataRequired()])
    img=StringField("ჩასვით ფოტო",validators=[DataRequired()])
    link = StringField("დატოვეთ ცარიელი")
    submit=SubmitField()

class InfoForm(FlaskForm):
    text=TextAreaField("ჩასვით ტექსტი",validators=[DataRequired()])
    name=StringField("შეიყვანეთ სათაური",validators=[DataRequired()])
    submit=SubmitField()

class DocForm(FlaskForm):
    text=TextAreaField("ჩასვით ტექსტი",validators=[DataRequired()])
    name=StringField("შეიყვანეთ სათაური",validators=[DataRequired()])
    submit=SubmitField()

class BakForm(FlaskForm):
    text=TextAreaField("ჩასვით ტექსტი",validators=[DataRequired()])
    name=StringField("შეიყვანეთ სათაური",validators=[DataRequired()])
    link = StringField("დატოვეთ ცარიელი")
    submit=SubmitField()

