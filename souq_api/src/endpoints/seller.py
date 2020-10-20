from flask import Blueprint, jsonify, request
from datetime import datetime
from ..models import Seller,Item
from mongoengine import *
import json

# define the blueprint
seller_blueprint = Blueprint(name="seller_blueprint", import_name=__name__)



# add view function to the blueprint
@seller_blueprint.route('/test', methods=['GET'])
def test():
    output = {
        "msg": "I'm the test endpoint from the tasklist blueprint."
    }
    return jsonify(output)

# add create seller  function to the blueprint
@seller_blueprint.route('/seller/add-item', methods=['POST'])
def add_item():

    # Read JSON data from request from the client
    data = request.get_json()

    # Create and save a new item
    seller_item= Seller(
        title=data['title'],
        description=data['description'],
        category = data['category'],
        price = data['price'],
    ).save()
   
    return seller_item.to_json()  


# add edit seller item function to the blueprint
@seller_blueprint.route('/edit-item/<seller_id>',methods=['PUT'])
def edit_item(seller_id):

    # Retrieve the tasklist
    seller=Seller.objects().first()

    #Read JSON data from request from the client
    data =request.get_json()

    seller.title = data['title']
    seller.description = data['description']
    seller.price = data['price']
    seller.category = data['category']

    seller.save()
    return seller.to_json()






