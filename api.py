from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import pandas as pd
import json

app = FastAPI()

# Configuración para permitir CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes de origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras HTTP
)

def conectar_mysql():
    # Establecer la conexión a MySQL
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='prueba4'
    )

def ejecutar_consulta_to_json(consulta):
    # Conectar a MySQL
    try:
        with conectar_mysql() as conexion_mysql:
            # Ejecutar la consulta
            with conexion_mysql.cursor(dictionary=True) as cursor:
                cursor.execute(consulta)
                # Obtener los resultados como un DataFrame
                resultado_df = pd.DataFrame(cursor.fetchall())

    except mysql.connector.Error as err:
        # Manejar el error de MySQL de manera específica
        raise HTTPException(status_code=500, detail=f"Error de base de datos MySQL: {err}")

    # Convertir el DataFrame a JSON
    resultado_json = resultado_df.to_json(orient='records')

    return json.loads(resultado_json)

@app.get("/")
def ruta_base():
    return {"mensaje": "¡Bienvenido a la API!"}

@app.get("/detalle_estado_producto")
def detalle_estado_producto():
    consulta = "SELECT * FROM vista_detalle_estado_producto"
    return ejecutar_consulta_to_json(consulta)

@app.get("/quejas_con_respuesta")
def quejas_con_respuesta():
    consulta = "SELECT * FROM vista_quejas_con_respuesta"
    return ejecutar_consulta_to_json(consulta)

@app.get("/quejas_mas_frecuentes")
def quejas_mas_frecuentes():
    consulta = "SELECT * FROM vista_quejas_mas_frecuentes"
    return ejecutar_consulta_to_json(consulta)

@app.get("/quejas_por_producto")
def quejas_por_producto():
    consulta = "SELECT * FROM vista_quejas_por_producto"
    return ejecutar_consulta_to_json(consulta)

@app.get("/resumen_empresa_estado")
def resumen_empresa_estado():
    consulta = "SELECT * FROM vista_resumen_empresa_estado"
    return ejecutar_consulta_to_json(consulta)

@app.get("/resumen_producto_empresa")
def resumen_producto_empresa():
    consulta = "SELECT * FROM vista_resumen_producto_empresa"
    return ejecutar_consulta_to_json(consulta)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
