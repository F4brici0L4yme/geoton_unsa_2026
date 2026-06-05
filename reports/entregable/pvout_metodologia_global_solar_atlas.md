# Índice PVOUT — Metodología, Obtención y Relevancia en el Análisis Solar

## 1. ¿Qué es el PVOUT?

**PVOUT** (*Photovoltaic Power Output*) es el indicador central del Global Solar Atlas. Expresa la **producción específica de electricidad fotovoltaica** de un sistema de 1 kWp instalado en condiciones de largo plazo, bajo configuración estándar:

| Atributo | Definición |
|---|---|
| **Unidad** | kWh/kWp/año (o kWh/kWp/día en escala diaria) |
| **Qué mide** | Energía eléctrica real generada por cada kilovatio-pico instalado en un año |
| **Tipo de sistema** | Panel monocristalino (cSi) de alta eficiencia, montaje fijo inclinado al ángulo óptimo hacia el ecuador |
| **Resolución espacial** | ~1 km (30 arco-segundos, raster GeoTIFF global) |
| **Cobertura temporal** | Promedio de largo plazo 1994–2018 (según región geográfica) |
| **Cobertura geográfica** | Todo el territorio entre 60°N y 55°S (en Latinoamérica hasta 45°S) |

A diferencia de GHI (irradiación horizontal global, que es pura radiación solar bruta), **PVOUT ya incorpora todas las pérdidas reales del sistema**: temperatura, pérdidas eléctricas, reflexión angular, disponibilidad del inversor, etc.

---

## 2. Fuentes de datos de entrada (inputs)

El modelo Solargis integra datos de múltiples satélites meteorológicos y centros atmosféricos mundiales:

| Fuente | Organismo | Uso en el modelo | Resolución temporal |
|---|---|---|---|
| Meteosat MSG/MFG (Atlántico) | EUMETSAT | Índice de nubosidad | 15–30 min |
| Meteosat IODC (Océano Índico) | EUMETSAT | Índice de nubosidad | 15–30 min |
| GOES East / West | NOAA | Índice de nubosidad | 30 min |
| Himawari-8 / MTSAT | JMA | Índice de nubosidad Pacífico | 10–30 min |
| MACC-II/CAMS | ECMWF | Profundidad óptica de aerosoles (AOD) | 3 horas |
| MERRA-2 | NASA | Aerosoles 1999–2002 | 1 hora |
| GFS/CFSR | NOAA | Vapor de agua | 1 hora |
| ERA5 | ECMWF | Temperatura del aire (TEMP) | 1 hora |
| SRTM v4.1 | NASA/USGS | Modelo digital de elevación (DEM) 250 m | Estático |

Estos datos se procesan en **pasos de 10, 15 o 30 minutos** para capturar la variabilidad diurna y estacional con alta fidelidad.

## 3. Importancia del PVOUT en el análisis de proyección

El PVOUT es el dato maestro de todo el análisis realizado en el notebook. Su papel en cada cálculo es:

```
E_panel [kWh/año] = (P_panel [kWp]) × PVOUT [kWh/kWp/año] × PR
```

El valor de PVOUT ya incorpora las pérdidas del sistema de referencia (8.9%). Multiplicar por el **Performance Ratio (PR = 0.80)** agrega las pérdidas específicas del sistema real propuesto (tipo de panel, cableado, inversor elegido). Usar PVOUT directamente evita tener que estimar GHI y aplicar un modelo FV completo desde cero y es vital para estimar la energía anual generada por cada panel y la cantidad de paneles necesarios para cubrir la demanda de electricidad.

## 4. Referencias

- ESMAP. 2019. *Global Solar Atlas 2.0 Technical Report*. Washington, DC: World Bank. [PDF](https://documents1.worldbank.org/curated/en/529431592893043403/pdf/Global-Solar-Atlas-2-0-Technical-Report.pdf)
- World Bank / Solargis. *World - Photovoltaic Power Potential (PVOUT) GIS Data*. [Data Catalog](https://datacatalog.worldbank.org/search/dataset/0038641)
- Global Solar Atlas interactive map: [https://globalsolaratlas.info/map](https://globalsolaratlas.info/map)
- Solargis methodology: [https://globalsolaratlas.info/support/methodology](https://globalsolaratlas.info/support/methodology)