from flask import Blueprint, jsonify, request
from ..models import Item
from wtforms import BooleanField




# define the blueprint
item_blueprint = Blueprint(name="item_blueprint", import_name=__name__)



# add view function to the blueprint
@item_blueprint.route('/test', methods=['GET'])
def test():
    output = {"msg": "I'm the test endpoint from blueprint_y."}
    return jsonify(output)


@item_blueprint.route('/add-item', methods=['POST'])
def add_item():
    # Read JSON data from request from the client
    data = request.get_json()

    # Create and save a new task list
    item= Item(
        title=data['title'],
        description=data['description'],
        price=data['price']
        # owner_id=data['user_id'],
        # created_at=datetime.now()
    ).save()
   
    return item.to_json()    

# add view item function to the blueprint
@item_blueprint.route('/<item_id>', methods = ['GET'])
def view_item(item_id):

    # Retrieve the item
    item = Item.objects(id = item_id)
   
    return item.to_json()

# add view all item function to the blueprint
@item_blueprint.route('/all')
def view_items():
    # Retrieve the item
    items = Item.objects()
   
    return items.to_json()


# add favorite item function to the blueprint
@item_blueprint.route('/favorite/<item_id>',methods=['GET'])
def set_favorite(item_id):

    # Retrieve the item
    item=Item.objects(id=item_id).first()

    if item.is_favorite == True:

        item.is_favorite = False
    else:
        item.is_favorite = True
    
    item.save()
    return item.to_json()

# add favorite item function to the blueprint
@item_blueprint.route('/favorites' ,methods=['GET'])
def view_favorites():

    # Retrieve the item
    favorites_items = Item.objects(is_favorite = True)
    
    return favorites_items.to_json()

# add search item function to the blueprint
@item_blueprint.route('/search', methods =['GET', 'POST'])
def search():

    # Retrieve the item
    items = Item.objects.search_text('Rawan')
    print(items)
    # items.title
    # if 'title' in request.args:
    #     items= items(title = request.args['title'])
     
    # if 'description' in request.args:
    #     items= items(description = request.args['description'])   
    return items.to_json()

# add descending sort item function to the blueprint
@item_blueprint.route('/descending-sort',methods=['GET','POST'])   
def descending_sort():


    # Retrieve the item
    descending_items = Item.objects().order_by('-price')
   
    return descending_items.to_json() 


# add ascending sort item function to the blueprint
@item_blueprint.route('/ascending-sort',methods=['GET','POST'])   
def ascending_sort():


    # Retrieve the item
    ascending_items = Item.objects().order_by('+price')
    
    return ascending_items.to_json() 


 

      


  
  

