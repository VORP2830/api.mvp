from database import db
from datetime import datetime

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    avg_price_paid = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    broker = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Stock {self.stock_code}>'
