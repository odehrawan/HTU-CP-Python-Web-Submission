from flask import Flask, request, Blueprint, render_template, redirect, session, url_for
from ..models.user import User
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import requests
import json

# create a blueprint
bp = Blueprint('user', __name__)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    middel_name = StringField('middel_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    submit = SubmitField('Sign In')


    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class SignupForm(FlaskForm):  
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    middel_name = StringField('middel_name', validators=[DataRequired()])
    birthdate = StringField('birthdate', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    submit = SubmitField('Sign In')
class EditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    middel_name = StringField('middel_name', validators=[DataRequired()])
    birthdate = StringField('birthdate', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    submit = SubmitField('Sign In')
class AddItemForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description= StringField('description', validators=[DataRequired()])
    submit = SubmitField('add-item')



DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

  
@bp.route("/create",methods=['GET','POST'])
def signup():
    #Read data from form
    form = SignupForm()

    if request.method == 'POST':

        #store the data from the form as json
        data = {'username':form.username.data,
        'password':form.password.data,
        'first_name':form.first_name.data,
        'middel_name':form.middel_name.data,
        'last_name':form.last_name.data}
        
        #send the json data to the api 
        result = requests.post('http://localhost:8080/api/v1/user_blueprint/create',json=data)
        print(result.text)

        return redirect(url_for('login'))
    
    return render_template('login/signup.html',form=form)

 
@bp.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        data = {'username':form.username.data,
        'password':form.password.data}

        r= requests.post('http://localhost:8080/api/v1/user_blueprint/login',json=data) 
        print(data) 

        return redirect('/')
    return render_template('login/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/edit-profile',methods=['GET','POST'])
def edit_user():
    form = EditForm()
    if request.method == 'GET':
        return render_template('edit-profile.html',form=form)  

    else:
        if form.validate_on_submit():

            data = {'username':form.username.data,
            'password':form.password.data,
            'first_name':form.first_name.data,
            'middel_name':form.middel_name.data,
            'last_name':form.last_name.data 
            }
            print(data)
          
    
            #send the json data to the api 
            result = requests.post('http://localhost:8080/api/v1/user_blueprint/edit-profile',json=data)

       
    
    return redirect('/')  
  
# @app.route("/test/x")
# def test_x():
#     r = requests.get('http://localhost:8080/api/v1/path_for_blueprint_x/test')

#     return r.json()


# @app.route("/test/y")
# def test_y():
#     r = requests.get('http://localhost:8080/api/v1/path_for_blueprint_y/test')

#     return r.json()