from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request
from app.models.menu_item import MenuItem
from app.models import db 

menu_bp = Blueprint('menu', __name__)


@menu_bp.route('/', methods=['GET'])
def get_menu() -> tuple[Response,int]:
    menu_items = MenuItem.query.all()
    
    response_message = jsonify([
        {"id": menu_item.id, "name": menu_item.name, "price": menu_item.price} 
        
         for menu_item in menu_items
        ]
      )
    response_status_code = HTTPStatus.OK
    
    return response_message, response_status_code


@menu_bp.route('/', methods=['POST']) 
def add_menu_item() ->  tuple[Response,int]:
    data = request.json or {}  # dictionary **{name="ada", price=20.4} => (name="ada", price=20.4)
    # new_item = MenuItem(name=data["name"], price=data["price"])
    new_item = MenuItem(**data)
    db.session.add(new_item)
    db.session.commit()

    response_message = jsonify({"message": "Menu item added successfully"})
    response_status_code = HTTPStatus.CREATED
    
    return response_message, response_status_code