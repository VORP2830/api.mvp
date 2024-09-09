from flask import Flask, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from database import init_db, db
from models.stock import Stock
from pydantic import BaseModel
from datetime import datetime

app = Flask(__name__)

# Configuração do OpenAPI/Swagger
info = Info(title="Stock Trading API", version="1.0.0")
app = OpenAPI(__name__, info=info)

 # Permitindo todas as origens
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Inicializando o banco de dados
init_db(app)

# Models para validação e documentação
class StockModel(BaseModel):
    code: str
    avg_price_paid: float
    quantity: int
    broker: str
    purchase_date: datetime = datetime.utcnow()

class StockUpdateModel(BaseModel):
    id: int
    code: str
    avg_price_paid: float
    quantity: int
    broker: str
    purchase_date: datetime

class QueryMode(BaseModel):
    id: int

# Rota para pegar todos os registros 
@app.get('/stocks', tags=[Tag(name='Stock', description='Rota para pegar todos os registros')])
def get_stocks():
    stocks = Stock.query.all()
    return jsonify({
        'items': [{
            'id': stock.id,
            'code': stock.code,
            'avg_price_paid': stock.avg_price_paid,
            'quantity': stock.quantity,
            'broker': stock.broker,
            'purchase_date': stock.purchase_date
        } for stock in stocks]
    })


# Rota para pegar um registro por ID
@app.get('/stock/', tags=[Tag(name='Stock', description='Rota para pegar um registro por ID')])
def get_stock(query: QueryMode):
    stock = Stock.query.get_or_404(query.id)
    return jsonify({
        'id': stock.id,
        'code': stock.code,
        'avg_price_paid': stock.avg_price_paid,
        'quantity': stock.quantity,
        'broker': stock.broker,
        'purchase_date': stock.purchase_date.isoformat()
    })

# Rota para criar um novo registro
@app.post('/stocks', tags=[Tag(name='Stock', description='Rota para criar um novo registro')])
def create_stock(body: StockModel):
    new_stock = Stock(
        code=body.code,
        avg_price_paid=body.avg_price_paid,
        quantity=body.quantity,
        broker=body.broker,
        purchase_date=body.purchase_date
    )
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({'message': 'Registro criado com sucesso!'}), 201

# Rota para editar um registro existente
@app.put('/stocks', tags=[Tag(name='Stock', description='Rota para editar um registro existente')])
def update_stock(body: StockUpdateModel):
    stock = Stock.query.get_or_404(body.id)
    stock.id = body.id
    stock.code = body.code
    stock.avg_price_paid = body.avg_price_paid
    stock.quantity = body.quantity
    stock.broker = body.broker
    stock.purchase_date = body.purchase_date
    db.session.commit()
    return jsonify({'message': 'Registro alterado com sucesso!'})

# Rota para deletar um registro
@app.delete('/stock/', tags=[Tag(name='Stock', description='Rota para deletar um registro')])
def delete_stock(query: QueryMode):
    stock = Stock.query.get_or_404(query.id)
    db.session.delete(stock)
    db.session.commit()
    return jsonify({'message': 'Registro deletado com sucesso!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
