
from flask import Flask 
 

def register_routes(app: Flask) -> None:
    from app.routes.menu import menu_bp
    from app.routes.order import order_bp
    
    app.register_blueprint(menu_bp, url_prefix="/menu")
    app.register_blueprint(order_bp, url_prefix="/order")