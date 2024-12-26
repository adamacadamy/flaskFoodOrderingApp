from app.models import db 

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    items = db.Column(db.Text, nullable=False)
    total_price = db.Column(db.Float, nullable=False)