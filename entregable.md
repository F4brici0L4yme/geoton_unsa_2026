# 🗺️ Registro Completo de Propuestas - Geotón Perú 2026

Este documento contiene la estructura completa y oficial del formulario de inscripción para la **Geotón Perú 2026** (Plataforma Facilita), expandido con las secciones de contexto, datos, solución y entrega. Está diseñado en Markdown para facilitar el borrador colaborativo en su repositorio de GitHub.

---

## SECCIÓN 1: IDENTIFICACIÓN DEL PARTICIPANTE O EQUIPO

Esto se llena en el link de GeoPeru: https://facilita.gob.pe/t/52313

---

## SECCIÓN 2: TÍTULO Y ENFOQUE

### 2. Título de la propuesta
*Escribe un título claro, innovador y descriptivo para tu proyecto.*

```text
Análisis Geoespacial de Viabilidad Fotovoltaica en Escuelas de Educación Básica con Brecha Eléctrica en la Región Arequipa
```

### 3. Problema territorial que abordas

```text
La brecha de infraestructura educativa y de conectividad en el Perú afecta desproporcionadamente a las escuelas rurales y periurbanas, limitando el acceso equitativo a la educación de calidad y las oportunidades socioeconómicas para miles de estudiantes.

En la región Arequipa, el análisis del Censo Educativo (ESCALE-MINEDU) cruzado con datos del Global Solar Atlas revela que 530 escuelas (de un universo de 2,029 analizadas) operan sin acceso confiable a electricidad (497 con carencia eléctrica confirmada + 33 en situación crítica extrema). Esto se agrava por el hecho de que el 12.9% de los equipos informáticos registrados en las escuelas se encuentran inoperativos, lo que sugiere que la falta de energía estable daña el equipamiento existente. Al mismo tiempo, la región Arequipa posee un PVOUT (producción fotovoltaica) promedio de 1,911 kWh/kWp/año, con distritos que alcanzan hasta 2,079 kWh/kWp/año (San Antonio de Chuca), lo que la convierte en una zona de altísimo potencial solar desaprovechado.
```

---

## SECCIÓN 3: CONTEXTO TERRITORIAL

### 4. Ubicación geográfica del análisis
- Regional — Arequipa

### 5. ¿Por qué es importante este problema?

```text
La brecha de infraestructura educativa y de conectividad en el Perú limita el acceso equitativo a la educación de calidad, el desarrollo de capacidades de los estudiantes y compromete su futuro.

Los niños y jóvenes de zonas rurales y periurbanas se ven obligados a asistir a escuelas con infraestructura inadecuada, sin acceso a internet ni laboratorios funcionales, lo que limita su capacidad para desarrollar las competencias necesarias para el siglo XXI.

En Arequipa, el análisis identificó que 52 distritos están clasificados como "Crítico (Off-Grid Aislado)" en términos de brecha eléctrica residencial, con el distrito de Tisco encabezando la lista con 71.83% de viviendas sin acceso a electricidad. En total, más de 38,212 viviendas en los 109 distritos analizados no tienen acceso a luz eléctrica. Las escuelas rurales dentro de estos distritos son las más afectadas.

Sin embargo, la misma geografía que genera aislamiento también genera una oportunidad: Arequipa tiene un potencial solar excepcional, con valores PVOUT entre 1,480 y 2,079 kWh/kWp/año, lo que hace técnica y económicamente viable la instalación de sistemas fotovoltaicos con períodos de retorno de inversión (payback) de tan solo 4.5 a 7.8 años según el distrito y el tamaño del sistema.
```

---

## SECCIÓN 4: USO DE DATOS

### 6. Dataset(s) utilizados de GEO Perú

```text
    1.
    Capa: Educación
    Subcapa: Locales de servicios educativos escolarizados
    Página Web: https://www.gob.pe/minedu
    Enlace al metadato: https://catalogo.geoidep.gob.pe/metadatos/srv/api/records/dd13e4bb-ed3d-465f-b12b-3fc2c6454a2f?language=all
    Mapa de Escuelas accedido: https://sigmed.minedu.gob.pe/mapaeducativo/
    Descripción del uso: Se obtuvo el listado completo de escuelas de nivel primario y secundario
    en la región Arequipa (2,029 instituciones). Incluye código modular (COD_MOD), nombre,
    distrito y localidad. Se usó para cruzar con el Censo Educativo y obtener datos de
    infraestructura y equipamiento.

```

### 7. ¿Cómo utilizaste los datos?

```text
El análisis se desarrolló en Python (Jupyter Notebooks) siguiendo un pipeline de 4 etapas:

ETAPA 1 — Construcción del universo de escuelas:
Se descargó el listado de Locales Educativos Escolarizados de ESCALE-MINEDU filtrado para
Arequipa (primaria y secundaria). Se obtuvo el padrón de 2,029 instituciones educativas con
su código modular (COD_MOD), nivel educativo, distrito y localidad.

ETAPA 2 — Enriquecimiento con datos de infraestructura y equipamiento:
Usando el COD_MOD como llave primaria, se cruzó el padrón con el Censo Educativo 2024 para
obtener: (a) si la escuela cuenta con electricidad (SCORE_CARENCIA = 0/1/2), (b) total de
equipos informáticos (TOTAL_EQUIPOS_D01), (c) equipos operativos (EQUIPOS_OPERATIVOS_D02),
y (d) matrícula total (TOTAL_ALUMNOS). Con estos datos se calculó un SCORE_IMPACTO ponderado
(0–1) y se clasificó cada escuela en prioridad BAJA, MEDIA o ALTA/URGENTE para instalación
de paneles solares.

ETAPA 3 — Cruce con potencial solar PVOUT y brecha eléctrica distrital:
Para cada distrito de Arequipa se obtuvo el valor PVOUT del Global Solar Atlas (kWh/kWp/año).
Luego se calculó, para 4 escenarios de demanda (15, 20, 30 y 35 PCs por laboratorio), las
proyecciones de: número de paneles requeridos, área de instalación (m²), potencia instalada
(kWp), energía generada anual (kWh/año), energía demandada (kWh/año), excedente (%),
CAPEX en USD y PEN, O&M anual, costo total a 25 años, LCOE (USD/kWh), payback (años) y
CO2 evitado (kg/año). Paralelamente, se calculó la brecha eléctrica residencial por distrito
(% de viviendas sin luz) para clasificar el tipo de intervención sugerida en 4 categorías.

ETAPA 4 — Priorización y visualización:
Se cruzaron las 125 escuelas ALTA/URGENTE (con carencia eléctrica y alto impacto) con los
datos de PVOUT de su distrito, la brecha eléctrica distrital y la matrícula, generando un
ranking de priorización territorial. Los resultados se visualizaron con mapas interactivos
(Folium) mostrando la distribución geográfica de escuelas por prioridad y el potencial solar
disponible en cada distrito.
```

### 8. Principales hallazgos del análisis

```text
HALLAZGO 1 — Magnitud del problema energético en escuelas arequipeñas:
De las 2,029 escuelas primarias y secundarias analizadas en Arequipa:
  • 125 escuelas (6.2%) son clasificadas como ALTA/URGENTE: no tienen acceso confiable
    a electricidad Y tienen alta matrícula o alto número de equipos inoperativos.
  • 405 escuelas (20.0%) son PRIORIDAD MEDIA: presentan carencia eléctrica o equipamiento
    deficiente pero con menor impacto inmediato.
  • 497 escuelas registran SCORE_CARENCIA = 1 (sin electricidad de red).
  • 33 escuelas presentan SCORE_CARENCIA = 2 (situación crítica extrema: sin electricidad
    y con equipos completamente inoperativos).
  • Las 125 escuelas ALTA/URGENTE concentran un total de 18,126 estudiantes directamente
    afectados distribuidos en 51 distritos.

HALLAZGO 2 — Inequidad territorial concentrada en zonas rurales:
Los distritos con mayor concentración de escuelas ALTA/URGENTE son:
  • Majes: 20 escuelas urgentes (distrito de alta expansión demográfica)
  • La Joya: 14 escuelas urgentes
  • Yanaquihua: 8 escuelas urgentes
  • Ocoña: 5 escuelas urgentes
  • Alca: 4 escuelas urgentes
Estos distritos coinciden con zonas de alta brecha eléctrica residencial, confirmando que
la carencia energética escolar refleja la precariedad estructural del territorio.

HALLAZGO 3 — Equipamiento TIC deteriorado por falta de energía estable:
Del universo total de 71,701 equipos informáticos registrados en las escuelas de Arequipa,
9,261 (12.9%) están inoperativos. En las escuelas ALTA/URGENTE, la proporción de equipos
dañados es significativamente mayor, lo que indica que la inestabilidad energética es una
causa directa del deterioro del equipamiento.

HALLAZGO 4 — Potencial solar excepcional en todos los distritos:
Los 109 distritos de Arequipa con datos PVOUT muestran un potencial fotovoltaico sobresaliente:
  • PVOUT promedio regional: 1,911 kWh/kWp/año
  • PVOUT mínimo: 1,480 kWh/kWp/año (Mejía — zona costera con mayor cobertura nubosa)
  • PVOUT máximo: 2,079 kWh/kWp/año (San Antonio de Chuca — zona altoandina)
  • Incluso el distrito con menor potencial solar (Mejía) supera ampliamente el umbral
    de viabilidad técnica para sistemas FV (>1,200 kWh/kWp/año).
  • Los 52 distritos clasificados como "Crítico Off-Grid" (mayor brecha eléctrica) tienen
    en promedio un PVOUT de ~1,980 kWh/kWp/año, lo que los convierte en los candidatos
    más atractivos para soluciones off-grid fotovoltaicas.

HALLAZGO 5 — Viabilidad económica confirmada para todos los escenarios:
Las proyecciones financieras para los 4 escenarios de laboratorio evaluados muestran:

  Escenario 15 PCs (≈4 paneles, 2.18 kWp, 8.7 m²):
    CAPEX promedio: USD 927 (S/ 3,478) | Payback: ~6.0 años | CO2 evitado: 1,661 kg/año

  Escenario 20 PCs (≈5 paneles, 2.76 kWp, 11.1 m²):
    CAPEX promedio: USD 1,174 (S/ 4,404) | Payback: ~5.7 años | CO2 evitado: 2,101 kg/año

  Escenario 30 PCs (≈7 paneles, 3.93 kWp, 15.8 m²):
    CAPEX promedio: USD 1,670 (S/ 6,263) | Payback: ~5.4 años | CO2 evitado: 2,984 kg/año

  Escenario 35 PCs (≈8 paneles, 4.50 kWp, 18.1 m²):
    CAPEX promedio: USD 1,913 (S/ 7,173) | Payback: ~5.3 años | CO2 evitado: 3,418 kg/año

  El LCOE promedio oscila entre USD 0.013 y USD 0.018/kWh, muy por debajo de la tarifa
  eléctrica rural en Perú, confirmando la viabilidad económica a largo plazo. En los
  distritos con mayor PVOUT, el payback puede bajar hasta 4.5 años.

HALLAZGO 6 — Brecha eléctrica residencial correlaciona con carencia escolar:
De los 109 distritos analizados:
  • 52 distritos son "Crítico (Off-Grid Aislado)": brecha >15% de viviendas sin luz
  • 46 distritos son "Prioridad Media (Evaluación mixta)": brecha entre 5–15%
  • 10 distritos son "Inestabilidad Urbana (On-Grid con Backup)": brecha <5% pero
    con interrupciones frecuentes
  • 1 distrito es "Cobertura Óptima": Mejía (<3% de viviendas sin luz)
  El distrito de Tisco lidera la brecha con 71.83% de viviendas sin electricidad,
  seguido por San Juan de Tarucani (68.52%) y San Antonio de Chuca (61.59%).
  En total, más de 38,212 viviendas en Arequipa carecen de electricidad.
```

### 9. Evidencia visual (Opcional)

```text

```

---

## SECCIÓN 5: PROPUESTA DE SOLUCIÓN

### 10. Describe tu propuesta de solución

```text
Proponemos un modelo de priorización geoespacial para la instalación de sistemas
fotovoltaicos en escuelas de Arequipa que carecen de electricidad confiable. Cruzando
datos del Censo Educativo (ESCALE-MINEDU), el Global Solar Atlas (PVOUT por distrito)
y la brecha eléctrica distrital (INEI), identificamos 125 escuelas ALTA/URGENTE que
concentran 18,126 estudiantes y el mayor potencial de impacto por sol invertido. Para
cada escuela se proyectan: número de paneles, área (m²), CAPEX (USD/PEN), payback y CO2
evitado en 4 escenarios (15–35 PCs). Tras recuperar la inversión (4.5–7.8 años), el
ahorro en factura eléctrica se reinvierte en conectividad: el modelo propone destinar
esos fondos liberados a servicios de internet satelital (Starlink, Amazon Kuiper u otros
proveedores disponibles por distrito), atacando la segunda gran brecha educativa. Es una
herramienta de decisión para MINEDU, gobiernos regionales y cooperantes, escalable a
todo el Perú.
```

### 11. ¿Qué impacto tendría tu propuesta?

```text
Impacto directo inmediato: 18,126 estudiantes en 125 escuelas ALTA/URGENTE accederían a
electricidad confiable para sus laboratorios, con CAPEX desde USD 927/escuela y payback
de 4.5–7.8 años.

Impacto en conectividad (segunda fase): Una vez amortizado el sistema solar, el ahorro
en factura eléctrica (~USD 100–300/año/escuela) se reinvierte en contratar internet
satelital. Starlink ofrece cobertura en zonas rurales de Arequipa por ~USD 50/mes con
hardware único ~USD 499; opciones como Amazon Kuiper o proveedores regionales amplían
la competencia. Electrificar primero es el prerequisito: sin energía estable, el router
no funciona. El modelo identifica qué escuelas están listas para la segunda brecha.

Impacto ambiental: 207–427 toneladas de CO2 evitadas anualmente para las 125 escuelas.

Impacto en política pública: Ranking territorializado y financieramente fundamentado
para eliminar la subjetividad en asignación de recursos. Escalable a 24 regiones.
```

### 12. ¿Tu propuesta podría implementarse? ¿Cómo?

```text
Sí. La factibilidad está respaldada por los datos:

Técnica: Los 109 distritos tienen PVOUT >1,480 kWh/kWp/año. Sistemas de 2–5 kWp con
8–20 m² de techo, instalables con tecnología disponible en el mercado local peruano.

Económica — Fase 1 (Solar): CAPEX desde USD 927/escuela, payback 4.5–7.8 años, LCOE
USD 0.013–0.018/kWh. Financiable vía FONIE, BID, BM, GEF o RSE minera.

Económica — Fase 2 (Internet): Tras el payback, el ahorro eléctrico cubre la suscripción
a internet satelital. Starlink (~USD 50/mes + USD 499 hardware único) es viable en zonas
rurales sin infraestructura de fibra. Amazon Kuiper y operadores regionales ofrecen
alternativas competitivas. El modelo identifica qué escuelas alcanzan excedente suficiente
para autofinanciar la conectividad.

Actores clave: MINEDU, MINEM/OSINERGMIN, Gobierno Regional de Arequipa, municipios
distritales, proveedores de internet satelital y sector minero (RSE).

Replicabilidad: Pipeline 100% reproducible con datos públicos para las 24 regiones.
```

---

## SECCIÓN 6: FORMATO DE ENTREGA

### 13. Tipo de solución presentada


### 14. Enlace o archivo de la propuesta final

```text
[Escribe aquí el enlace de tu propuesta o el nombre exacto del archivo que vas a subir...]
```

### 15. Comparte tu propuesta en redes

```text
[Escribe aquí los enlaces de tus publicaciones en redes sociales...]
```
