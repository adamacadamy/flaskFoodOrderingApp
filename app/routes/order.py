from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request
from app.models.order import Order
from app.models.menu_item import MenuItem
from app.models import db

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['POST'])
def place_order() -> tuple[Response, int]:
    data  = request.json or {}
    
    customer_name = data['customer_name']
    items = data['items'] # id of MenuItems
    items_str = ",".join(map(str, items)) 
    total_price = sum(
        MenuItem.query.get(item).price
        for item in items
    )
    new_order = Order(
        customer_name=customer_name,
        items=items_str,
        total_price=total_price 
    )
   
    db.session.add(new_order)
    db.session.commit()
    
    response_message= jsonify({
        "message": "Order placed successfully",
        "order_id": new_order.id
    })
    response_status_code = HTTPStatus.CREATED
    
    return response_message, response_status_code


@order_bp.route('/', methods=['GET'])
def get_order() -> tuple[Response, int]:
    
    orders = Order.query.all()
    response_message= jsonify([
        {
            "id": order.id,
            "customer_name": order.customer_name,
            "items": order.items,
            "total_price": order.total_price
        }
        for order in orders
    ])
    response_status_code = HTTPStatus.OK
    
    return response_message, response_status_code