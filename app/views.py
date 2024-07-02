#from flask import Flask, jsonify
from flask import Flask, jsonify
from app.models import Inmueble

def index():
   return jsonify(
         {
            'mensaje': 'hola mundo esto es un ejemplo'
        }
    )


def create_inmueble():
    data = request.json
    new_inmueble = inmueble(
        inmueble_id=data['inmueble_id'],  
        propietario=data['propietario_id'],
        direccion=data['direccion'],
        tipo_inmueble=data['tipo_inmueble'],
        habitaciones=data['habitaciones'],
        baños=data['baños'],
        precio_alquiler=data['precio_alquiler'],
        metros_cuadrados=data['metros_cuadrados'],
        estado=data['estado'],
    )
    new_inmueble.save()
    return jsonify({'message': 'Task created successfully'}), 201

    return jsonify(inmueble)