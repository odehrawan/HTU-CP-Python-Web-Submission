from flask import Blueprint, jsonify, request,session
from datetime import datetime
from ..models import User, Seller
from mongoengine import *

# define the blueprint
user_blueprint = Blueprint(name="user_blueprint", import_name=__name__)


# add create user function to the blueprint
@user_blueprint.route('/create', methods=['POST'])
def create_user():
    # Read the request data from the client
    data = request.get_json()

    # Create and save a user to the DB
    user = User(username=data['username'],
                password=User.generate_hash(data['password']),
                first_name=data['first_name'],
                middel_name=data['middel_name'],
                last_name=data['last_name']
                ).save()

    return user.to_json()

# login function to the blueprint
@user_blueprint.route('/login', methods=['POST'])
def login():
    # Read the request data from the client
    data = request.get_json()

    # Read credentials from request
    username = data['username']
    password = data['password']

    # Authenticate the user
    if User.authenticate(username, password):
        # Add user to session
        # session['user'] = user.to_json()
        response = {"msg": f"User {username} and {password}is now logged in."}
        print(username)
        return jsonify(response)
    else:
        response = {"msg": "Invalid credentials."}
        return jsonify(response)

# edit the user  function to the blueprint
@user_blueprint.route('/edit-profile',methods=['PUT'])
def edit_profile():
    # Retrieve the user
    user=User.objects().first()

    #Read JSON data from request from the client
    data =request.get_json()

    user.username = data['username']
    user.first_name = data['first_name']
    user.middel_name = data['middel_name']
    user.last_name = data['last_name']

    # user.username = username
    # user.first_name = first_name
    # user.middel_name = middel_name
    # user.last_name = last_name

    user.save()
    return user.to_json()

