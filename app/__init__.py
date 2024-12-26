import os 
from flask  import Flask 
from flask_migrate import Migrate 
from dotenv import load_dotenv 
from app.models import db 
from app.routes import register_routes

# Load environmental variables
load_dotenv()
""" 
env = {
    
    "DATABASE_URI": "mysql+mysqlconnector://root:top!secret@localhost:3307/food_ordering_system"
}
"""

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app) # connection initializer
    Migrate(app, db) # create all tables from model
    
    # Register routes
    
    register_routes(app)
    
    return app