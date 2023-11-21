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
"""
@app.route('/registro', methods=['POST'])
def postUser():
    data = request.get_json()
    
    username = data["name"]
    password = data["password"]
    
    user = next((user for user in users if user["name"] == username and user["password"] == password), None)
    if user:
        return jsonify({"status": "error"}), 401
    else:
        user["id"] = len(users) + 1
        users.append(user)
        return jsonify({"status": "success"}), 200
"""
@app.route('/registro', methods=['POST'])
def registro():
  """
  Endpoint para registrar un nuevo usuario.

  Parámetros:
    name: El nombre del usuario.
    password: La contraseña del usuario.

  Devuelve:
    Un objeto JSON con los siguientes campos:
      success: True si el registro fue exitoso, False de lo contrario.
      error: Un mensaje de error si el registro no fue exitoso.
  """

  data = request.get_json()
  name = data['name']
  password = data['password']

  # Validar que el usuario no exista

  if name in users:
    return jsonify({'success': False, 'error': 'El usuario ya existe'})

  # Crear el usuario

  users[name] = password

  return jsonify({'success': True})



@app.route('/usuarios')   # en el de ellos es available days
def GetUsuarios():
    return jsonify({'usuarios': users})



if __name__ == '__main__':
    app.run(debug=True, port=5000)