from flask import Flask, request, Blueprint, render_template, redirect, session, url_for
from ..models import Item, Task, User
from ..core import login_required

# create a blueprint
bp = Blueprint('item', __name__)
@bp.route("/add-item",methods=['GET','POSt'])
def add_item():
    form = AddItemForm()

    if request.method == 'GET':
        return render_template("add-item.html",form=form)

    else:   
         
        data = {'title':form.title.data,
            'description':form.description.data
            
            }
        print(data)    

        # Retrieve the user tasklists
        r = requests.post(
            'http://localhost:8080/api/v1/item/add-item', json=data)

        # Render the item view with the item
    return redirect('/')


@bp.route("/item/<item_id>")
def view_item(item_id):
    
 
    # Retrieve task list data
    r = requests.get(
        'http://localhost:8080/api/v1/item/' + item_id)

    # item = json.loads(r.json())
   

    return render_template("view-item.html")

@bp.route("/items")
def view_items():
    form = AddItemForm()
    data = {'title':form.title.data,
            'description':form.description.data
            
        }
    # Retrieve task list data
    r = requests.post(
        'http://localhost:8080/api/v1/item/all',json=data )

    # item = json.loads(r.json())
    context = {
    'item':Item.objects.all()
    }

    return render_template("view-item.html",context)