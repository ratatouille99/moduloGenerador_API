import streamlit as st
import pandas as pd
import requests  # Importar la biblioteca requests para hacer solicitudes HTTP

def cargar_datos_desde_api(informe):
    # URL de la API FastAPI
    url_api = f"http://127.0.0.1:8000/{informe}"  # Reemplazar espacios por guiones bajos

    # Hacer la solicitud GET a la API
    response = requests.get(url_api)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Convertir la respuesta JSON a un DataFrame de pandas
        datos = pd.DataFrame(response.json())
        return datos
    else:
        st.error(f"Error al cargar datos desde la API. Código de estado: {response.status_code}")
        st.markdown(url_api)
        return None

def generar_informe(data):
    # Puedes personalizar esta función según tus necesidades
    st.title('Reporte generado')
    st.write('A continuación se presenta un resumen del reporte seleccionado:')
    st.write(data)

# Crear botones en Streamlit para los informes
st.title("MENU PRINCIPAL")
col1, col2 = st.columns(2)

# Establecer el ancho deseado para los contenedores
ancho_contenedores = 200

# Crear botones con contenedores de ancho fijo en cada columna
with col1:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_1 = st.button("Detalle estado producto")

with col2:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_2 = st.button("Quejas con respuesta")

col3, col4 = st.columns(2)
with col3:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_3 = st.button("Quejas mas frecuentes")

with col4:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_4 = st.button("Quejas por producto")

col5, col6 = st.columns(2)
with col5:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_5 = st.button("Resumen empresa estado")

with col6:
    st.markdown("<style>div.Widget.row-widget.stButton {width: 100%;}</style>", unsafe_allow_html=True)
    boton_6 = st.button("Resumen producto empresa")


informe_seleccionado = ''
# Verificar cuál de los botones de informes fue presionado
if boton_1:
    informe_seleccionado = "detalle_estado_producto"
elif boton_2:
    informe_seleccionado = "quejas_con_respuesta"
elif boton_3:
    informe_seleccionado = "quejas_mas_frecuentes"
elif boton_4:
    informe_seleccionado = "quejas_por_producto"
elif boton_5:
    informe_seleccionado = "resumen_empresa_estado"
elif boton_6:
    informe_seleccionado = "resumen_producto_empresa"

# Verificar si se seleccionó algún informe
if informe_seleccionado != '':
    # Cargar datos desde la API según el informe seleccionado
    datos_api = cargar_datos_desde_api(informe_seleccionado)

    # Generar informe si los datos fueron cargados correctamente
    if datos_api is not None:
        generar_informe(datos_api)
