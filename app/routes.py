from flask import request, jsonify
from app import app, db
from app.models import Stock
from app.utils import is_db_connected

@app.route('/health', methods=['GET'])
def health_check():
    response = {
        "status": "healthy",
        "message": "The application is running fine!",
        "db_connection": "healthy" if is_db_connected() else "unhealthy"
    }
    return jsonify(response), 200

@app.route('/stocks', methods=['POST'])
def create_stock():
    data = request.get_json()
    if 'name' not in data or 'ticker' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_stock = Stock(name=data['name'], ticker=data['ticker'], price=data['price'])
    db.session.add(new_stock)
    db.session.commit()

    return jsonify({"message": "Stock added"}), 201

@app.route('/stocks', methods=['GET'])
def get_stocks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    stocks = Stock.query.paginate(page=page, per_page=per_page)

    stock_list = [{
        "id": stock.id,
        "name": stock.name,
        "ticker": stock.ticker,
        "price": stock.price
    } for stock in stocks.items]

    return jsonify({"stocks": stock_list, "total": stocks.total, "pages": stocks.pages})

@app.route('/stocks/<int:id>', methods=['GET'])
def get_single_stock(id):
    stock = Stock.query.get_or_404(id)
    return jsonify({"id": stock.id, "name": stock.name, "ticker": stock.ticker, "price": stock.price})

@app.route('/stocks/<int:id>', methods=['PUT'])
def update_stock(id):
    stock = Stock.query.get_or_404(id)
    data = request.get_json()
    stock.name = data.get('name', stock.name)
    stock.ticker = data.get('ticker', stock.ticker)
    stock.price = data.get('price', stock.price)
    db.session.commit()
    return jsonify({"message": "Stock updated"})

@app.route('/stocks/<int:id>', methods=['DELETE'])
def delete_stock(id):
    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    return jsonify({"message": "Stock deleted"})
