import os
import httpx
from playwright.sync_api import sync_playwright

def ejecutar_script():
    # 1. Crear la carpeta destino en la misma ruta donde se ejecuta el script
    carpeta_destino = os.path.join(os.getcwd(), "archivos_zip_escale")
    os.makedirs(carpeta_destino, exist_ok=True)
    
    url_inicial = (
        "https://escale.minedu.gob.pe/censo-escolar/-/document_library_display/oJ44/view/10632985"
        "?_110_INSTANCE_oJ44_topLink=documents-home"
        "&_110_INSTANCE_oJ44_cur1=1"
        "&_110_INSTANCE_oJ44_delta1=20"
        "&_110_INSTANCE_oJ44_keywords="
        "&_110_INSTANCE_oJ44_advancedSearch=false"
        "&_110_INSTANCE_oJ44_andOperator=true"
        "&_110_INSTANCE_oJ44_delta2=20"
        "&cur2=1"
    )
    
    enlaces_detalle = []
    
    print("Iniciando navegador virtual...")
    with sync_playwright() as p:
        # Lanzamos el navegador en modo "headless" (invisible) para ahorrar recursos
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # OPTIMIZACIÓN: Bloqueamos imágenes y estilos para que las páginas carguen instantáneamente
        def bloquear_recursos(route):
            if route.request.resource_type in ["image", "stylesheet", "font", "media"]:
                route.abort()
            else:
                route.continue_()
        
        page.route("**/*", bloquear_recursos)
        
        url_actual = url_inicial
        num_pagina = 1
        
        print("\n=== FASE 1: Recolectando enlaces de cada página ===")
        while url_actual:
            print(f"Analizando listado de la página {num_pagina}...")
            page.goto(url_actual, wait_until="domcontentloaded")
            
            # Aseguramos que carguen los textos de los archivos
            page.wait_for_selector("span.taglib-text")
            
            # Buscamos todos los enlaces en la página
            enlaces = page.query_selector_all("a")
            for enlace in enlaces:
                span_texto = enlace.query_selector("span.taglib-text")
                if span_texto:
                    nombre_archivo = span_texto.inner_text().strip()
                    # Validamos que termine en .zip
                    if nombre_archivo.lower().endswith('.zip'):
                        href = enlace.get_attribute("href")
                        # Evitamos duplicados
                        if href and not any(d['url_detalle'] == href for d in enlaces_detalle):
                            enlaces_detalle.append({
                                "nombre": nombre_archivo,
                                "url_detalle": href
                            })
            
            # Verificar si existe el botón "Siguiente" para continuar la paginación
            boton_siguiente = page.query_selector("a.next")
            if boton_siguiente:
                url_actual = boton_siguiente.get_attribute("href")
                num_pagina += 1
            else:
                url_actual = None
        
        total_archivos = len(enlaces_detalle)
        print(f"\nSe detectaron un total de {total_archivos} archivos ZIP en las páginas.")
        
        print("\n=== FASE 2: Extrayendo URLs de descarga directa ===")
        items_a_descargar = []
        for index, item in enumerate(enlaces_detalle, start=1):
            print(f"[{index}/{total_archivos}] Entrando a página de: {item['nombre']}")
            try:
                page.goto(item['url_detalle'], wait_until="domcontentloaded")
                # Buscamos el input con la clase 'form-text' que guarda la URL final de descarga
                input_descarga = page.wait_for_selector("input.form-text", timeout=5000)
                if input_descarga:
                    url_descarga_directa = input_descarga.get_attribute("value")
                    if url_descarga_directa:
                        item["url_descarga"] = url_descarga_directa
                        items_a_descargar.append(item)
            except Exception as e:
                print(f"  -> Error al extraer link de {item['nombre']}: {e}")
        
        # Guardamos cookies por si el portal exige mantener la sesión activa durante las descargas
        cookies_sesion = {c['name']: c['value'] for c in context.cookies()}
        browser.close()
    
    print("\n=== FASE 3: Descarga rápida de archivos ZIP ===")
    # Usamos httpx Client por ser sumamente veloz manejando streams de datos
    with httpx.Client(cookies=cookies_sesion, timeout=60.0) as cliente:
        for index, item in enumerate(items_a_descargar, start=1):
            nombre = item["nombre"]
            url_final = item["url_descarga"]
            ruta_guardado = os.path.join(carpeta_destino, nombre)
            
            print(f"[{index}/{len(items_a_descargar)}] Descargando {nombre}... ", end="", flush=True)
            try:
                respuesta = cliente.get(url_final)
                if respuesta.status_code == 200:
                    with open(ruta_guardado, "wb") as f:
                        f.write(respuesta.content)
                    print("¡Completado! ✔")
                else:
                    print(f"Error (Código HTTP: {respuesta.status_code}) ❌")
            except Exception as e:
                print(f"Error inesperado: {e} ❌")
                
    print(f"\nProceso terminado con éxito. Los archivos están en:\n👉 {carpeta_destino}")

if __name__ == "__main__":
    ejecutar_script()