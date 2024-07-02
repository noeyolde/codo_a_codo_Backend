from app.database import get_db

class Inmueble:
    def __init__(self, inmueble_id=None, propietario_id=None, direccion=None, tipo_inmueble=None, habitaciones=None, baños=None, precios=None, metros_cuadrados=None, estado=None):
        self.inmueble_id = inmueble_id
        self.propietario_id = propietario_id
        self.direccion = direccion
        self.tipo_inmueble = tipo_inmueble
        self.habitaciones = habitaciones
        self.baños = baños
        self.precio_alquiler = precio_alquiler
        self.metros_cuadrados = metros_cuadrados
        self.estado = estado

    
@staticmethod
def __get_inmueble_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        inmueble = []
        for row in rows:
            inmuble.append(
                Inmueble(
                    inmueble_id=row[0],
                    propietario_id=row[1],
                    direccion=row[2],
                    tipo_inmueble=row[3],
                    habitaciones=row[4],
                    baños=row[5],
                    precio_alquiler=row[6],
                    metros_cuadrados=row[7],
                    estado=row[8]
                )
            )
        cursor.close()
        return inmueble