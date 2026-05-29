import re
import html

def extraer_geoperu(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dividimos el HTML por cada bloque de categoría
    parts = re.split(r'<div id="div_category_\d+" class="category">', content)
    
    resultados = []

    for part in parts[1:]:
        # Extraer nombre de la Categoría
        cat_match = re.search(r'<label class="category__label"[^>]*>(.*?)</label>', part, re.DOTALL)
        if cat_match:
            category_name = html.unescape(cat_match.group(1).strip())
            
            # Extraer todas las capas (subcategorías) dentro de este bloque
            # Buscamos los labels que tienen un ID que empieza con "label_"
            sub_labels = re.findall(r'<label[^>]*id="label_\d+"[^>]*>(.*?)</label>', part, re.DOTALL)
            subcategories = [html.unescape(s.strip()) for s in sub_labels]
            
            resultados.append((category_name, subcategories))

    # Guardar en un archivo de texto estructurado
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("LISTA DE CATEGORÍAS Y CAPAS - GEO PERÚ\n")
        f.write("="*40 + "\n\n")
        for cat, subs in resultados:
            f.write(f"CATEGORÍA: {cat} ({len(subs)} capas)\n")
            for sub in subs:
                f.write(f"  - {sub}\n")
            f.write("-" * 40 + "\n")

    print(f"Proceso terminado. Se han extraído {len(resultados)} categorías en '{archivo_salida}'.")

# Uso: Asegúrate de que el archivo .html esté en la misma carpeta
extraer_geoperu('Geo Perú.html', 'lista_datos_geoperu.txt')