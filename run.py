from flask import Flask
from app.views import *
from app.database import *
from flask_cors import CORS


app = Flask(__name__)



#rutas de API-rest


app.route('/', methods=['GET'])(index)
# CRUD GET
app.route('/inmueble', methods=['GET'])(get_inmueble)

#Conexión a BDD
init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#Cracion de tabla
create_table_inmueble()

if __name__ == '__main__':
    app.run(debug=True)


