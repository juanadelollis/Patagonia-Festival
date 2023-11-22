from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from fechas import fechas
from users import users
from entradas import entradas
from zones import zones

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir cualquier origen


# Get Data Routes



@app.route('/fechas')   # en el de ellos es available days
def getFechas():
    return jsonify({'fechas': fechas})

@app.route('/zones')
def getZones():
    return jsonify(zones)

@app.route('/entradas', methods=['GET'])
def getEntradas():
    return jsonify(entradas)


@app.route('/buy', methods=['POST'])
def buy():
     entrada = request.get_json()
     print("entrada", entrada)
     entradas.append(entrada)
     print("entrada", entrada)
     return jsonify({'message': 'Compra Exitosa'})


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    username = data["name"]
    password = data["password"]
    
    user = next((user for user in users if user["name"] == username and user["password"] == password), None)
    if user:
        return jsonify({"status": "success", "user": user}), 200
    else:
        return jsonify({"status": "error"}), 401

@app.route('/registro', methods=['POST'])
def registro():
  data = request.get_json()
  name = data['name']
  password = data['password']

  if name in [user['name'] for user in users]:
    return jsonify({'success': False, 'error': 'El usuario ya existe'})
  # Crear el usuario

  new_user = {'id': len(users) + 1, 'name': name, 'password': password}
  users.append(new_user)


  return jsonify({'success': True})




@app.route('/usuarios')   # en el de ellos es available days
def GetUsuarios():
    return jsonify({'usuarios': users})



if __name__ == '__main__':
    app.run(debug=True, port=5000)