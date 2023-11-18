from flask import Flask, jsonify, request
from flask_cors import CORS
from fechas import fechas
from users import users
from entradas import entradas
from zones import zones

app = Flask(__name__)
CORS(app)


# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes

@app.route('/fechas')   # en el de ellos es available days
def getFechas():
    return jsonify({'fechas': fechas})

@app.route('/zones')
def getZones():
    return jsonify(zones)

@app.route('/buy', methods=['POST'])
def buy():
     entrada = request.get_json()
     print("entrada", entrada)
     entradas.append(entrada)
     print("entrada", entrada)
     return jsonify({'message': 'Compra Exitosa'})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        article for article in articles if article['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
# @app.route('/articles', methods=['POST'])
# def addArticle():
#     new_article = {
#         'id': request.json['id'],
#         'title': request.json['title'],
#         'body': request.json['body'],
#         'fecha': request.json['fecha']
#     }
#     articles.append(new_article)
#     return jsonify({"message":"Artículo agregado satisfactoriamente", 'artcles': articles})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json();
    
    username = data["name"]
    password = data["password"]
    
    user = next((user for user in users if user["name"] == username and user["password"] == password), None)
    if user:
        return jsonify({"status": "success", "user": user}), 200
    else:
        return jsonify({"status": "error"}), 401

# @app.route('/account', methods=['POST'])
# def addUser():
#     new_user = {
#         'id': len(users) + 1,
#         'name': request.json['name'],
#         'password': request.json['password'],
#     }
#     users.append(new_user)
#     return jsonify({"message":"Usuario agregado satisfactoriamente", 'usuarios': users})

if __name__ == '__main__':
    app.run(debug=True, port=5000)