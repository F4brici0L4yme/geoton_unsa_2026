import requests
import geopandas as gpd

# URL del endpoint de consulta de Osinergmin
url = "https://gisem.osinergmin.gob.pe/serverch/rest/services/Electricidad/Electricidad/MapServer/22/query"

# Parámetros para solicitar TODOS los registros con su geometría de líneas
params = {
    'where': '1=1',           # Traer todos los registros
    'outFields': '*',          # Traer todas las columnas de la tabla de atributos
    'returnGeometry': 'true',  # Sí queremos las coordenadas espaciales
    'f': 'geojson'             # Formato de salida ideal para análisis
}

response = requests.get(url, params=params)

if response.status_code == 200:
    # Convertir la respuesta directamente en un GeoDataFrame
    gdf = gpd.read_file(response.text)
    
    # Exportar a tu computadora
    gdf.to_file("redes_media_tension_peru.geojson", driver="GeoJSON")
    print("¡Dataset descargado con éxito!")
else:
    print("Error al conectar con el servidor.")
