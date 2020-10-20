from flask import Flask, render_template, request, jsonify,redirect,flash,url_for,session

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import requests
import json



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')
   


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
    price=StringField('price',validators=[DataRequired()])
    category=StringField('category',validators=[DataRequired()])

    submit = SubmitField('add-item')



DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

  
@app.route("/create",methods=['GET','POST'])
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

 
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        #store the data from the form as json
        data = {'username':form.username.data,
        'password':form.password.data}


        #send the json data to the api 
        r= requests.post('http://localhost:8080/api/v1/user/login',json=data) 
        
        print(data)
        


        return redirect(url_for('index'))
    return render_template('login/login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

class Exception():
    pass 

@app.route('/edit-profile',methods=['GET','POST'])
def edit_user():
    form = EditForm()
    if request.method == 'GET':
        return render_template('edit-profile.html',form=form)  

    else:


        #store the data from the form as json
      
        data = {'username':form.username.data,
        'password':form.password.data,
        'first_name':form.first_name.data,
        'middel_name':form.middel_name.data,
        'last_name':form.last_name.data}
     

              
        user.username = data['username']
        user.first_name = data['first_name']
        user.middel_name = data['middel_name']
        user.last_name = data['last_name']
        print(user.username)
        user.save()

              
        #send the json data to the api 
        result = requests.post('http://localhost:8080/api/v1/user/edit-profile',data=json)
        print(result.text)
        return redirect(url_for('index'))
             
    return render_template('login/login.html',form=form)  
  


@app.route("/add-item",methods=['GET','POSt'])
def add_item():
    form = AddItemForm()

    if request.method == 'GET':
        return render_template("add-item.html",form=form)

    else:   
        #store the data from the form as json
        data = {'title':form.title.data,
            'description':form.description.data,
            'price':form.price.data
            
            }
        print(data) 

        #send the json data to the api    
 
        r = requests.post(
            'http://localhost:8080/api/v1/item/add-item', json=data)

    return redirect('/')


@app.route("/item/<item_id>")
def view_item(item_id):
    
 
   #send the json data to the api 
    r = requests.get(
        'http://localhost:8080/api/v1/item/' + item_id)

    items = r.json()

    return render_template("view-item.html",items=items)


class Exception():
    pass 

@app.route("/items")
def view_items():
    form = AddItemForm()

    #store the data from the form as json
    data = {'title':form.title.data,
            'description':form.description.data
            
        }
    #send the json data to the api 
    r = requests.get(
        'http://localhost:8080/api/v1/item/all',json=data )
    if r.status_code != 200 :
       
        raise Exception("exception in request.get() http://localhost:8080/api/v1/item/all")
    else: 
        items = r.json()

    print(r.text)
   
    return render_template("view-item.html", items=items,form=form)

@app.route("/favorites")
def view_favorites():
    form = AddItemForm()
    #store the data from the form as json
    data = {'title':form.title.data,
            'description':form.description.data
            
        }
    #send the json data to the api 
    r = requests.get(
        'http://localhost:8080/api/v1/item/favorites', json = data )
    # if r.status_code != 200 :
       
    #     raise Exception("exception in request.get() http://localhost:8080/api/v1/item/favorites")
    # else: 
    items = r.json()
    
    return render_template("favorites-item.html",form=form, items=items)

@app.route("/search",methods=['GET','POST'])    
def search():
    form = AddItemForm()
    if request.method == 'GET':
        return render_template("search/search-item.html",form=form)

    else: 

        #store the data from the form as json  
       
        data = {'title':form.title.data,
                'description':form.description.data,
                
                
            }
        #send the json data to the api 
        r = requests.post(
            'http://localhost:8080/api/v1/item/search', json = data )


    items = r.json()
   
      
    return render_template("search/result_search.html",items=items)

@app.route("/descending-sort",methods=['GET','POST'])    
def descending_sort():

    form = AddItemForm()

    if request.method == 'GET':
        return render_template("sort/sort-item.html",form=form)

    else:   
        #store the data from the form as json   
        data = {'title':form.title.data,
                'description':form.description.data,
                'price':form.price.data
                
            }
        #send the json data to the api 
        r = requests.post(
            'http://localhost:8080/api/v1/item/descending-sort', json = data )


    descending_items =r.json()
        
      
    return render_template("sort/result_sort.html",descending_items=descending_items)
        
@app.route("/ascending-sort",methods=['GET','POST'])    
def ascending_sort():

    form = AddItemForm()

    if request.method == 'GET':
        return render_template("sort/sort-item.html",form=form)

    else:   

        #store the data from the form as json         
        data = {'title':form.title.data,
                'description':form.description.data,
                'price':form.price.data
                
            }
        #send the json data to the api 
        r = requests.post(
            'http://localhost:8080/api/v1/item/ascending-sort', json = data )

  
    ascending_items =r.json() 
  
      
     
    return render_template("sort/ascending_result.html",ascending_items=ascending_items )

@app.route("/seller/add-item",methods=['GET','POSt'])
def seller_add_item():
    form =AddItemForm()

    if request.method == 'GET':
        return render_template("seller-add-item.html",form=form)

    else:   
        #store the data from the form as json 
        data = {'title':form.title.data,
            'description':form.description.data,
            'price':form.price.data,
            'category':form.category.data,
            
            
            }
        print(data)    

        #send the json data to the api   
        r = requests.post(
            'http://localhost:8080/api/v1/seller/seller/add-item', json=data)

       
    return redirect('/')


@app.route('/edit-item/<seller_id>',methods=['GET','POST'])
def edit_item(seller_id):
    form = AddItemForm()
    if request.method == 'GET':
        return render_template('edit-item.html',form=form,seller_id=seller_id)  

    else:
        if form.validate_on_submit():
            
            #store the data from the form as json 
            data = {'title':form.title.data,
            'description':form.description.data,
            'price':form.price.data,
            'category':form.category.data,
            }
            print(data)
         
    
            #send the json data to the api 
            result = requests.post('http://localhost:8080/api/v1/seller/edit-item/<seller_id>',json=data)
       
    return redirect('/')  
        

if __name__ == "__main__":
    app.run(debug=True)