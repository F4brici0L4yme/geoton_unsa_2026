import os
import pandas as pd
from dbfread import DBF
import unicodedata

def clean_string(s):
    if pd.isnull(s): return s
    # Convert to string, upper, strip
    s = str(s).upper().strip()
    # Remove accents
    s = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return s

def main():
    path_dbf = '../data/external/data_pob_servicios_alumbrado_elect_/data_pob_servicios_alumbrado_elect_.dbf'
    path_csv_dist = '../data/external/congreso_del_peru/distritos_arequipa.csv'
    
    print("Leyendo datos de alumbrado de INEI...")
    # Read DBF
    table = DBF(path_dbf, encoding='latin1', load=True)
    df_elec = pd.DataFrame(iter(table))
    
    # Filter Arequipa
    df_elec = df_elec[df_elec['NOM_DPTO'].apply(clean_string) == 'AREQUIPA'].copy()
    
    # Rename and select columns
    # 'COD_DIST', 'NOM_DIST', 'NUM_VIV_OP', 'VS_AELEC', 'PVS_AELEC'
    df_elec = df_elec[['COD_DIST', 'NOM_PROV', 'NOM_DIST', 'NUM_VIV_OP', 'VS_AELEC', 'PVS_AELEC']].copy()
    df_elec.rename(columns={
        'COD_DIST': 'UBIGEO',
        'NOM_PROV': 'PROVINCIA',
        'NOM_DIST': 'DISTRITO',
        'NUM_VIV_OP': 'TOTAL_VIVIENDAS',
        'VS_AELEC': 'VIVIENDAS_SIN_LUZ',
        'PVS_AELEC': 'BRECHA_PORCENTAJE'
    }, inplace=True)
    
    # Clean numeric strings (like '6,706' -> 6706)
    for col in ['TOTAL_VIVIENDAS', 'VIVIENDAS_SIN_LUZ']:
        df_elec[col] = df_elec[col].astype(str).str.replace(',', '').astype(float)
    df_elec['BRECHA_PORCENTAJE'] = df_elec['BRECHA_PORCENTAJE'].astype(float)
    
    # Clean district names for merge
    df_elec['DISTRITO_CLEAN'] = df_elec['DISTRITO'].apply(clean_string)
    
    # Read lat/lon
    print("Leyendo distritos seleccionados...")
    df_geo = pd.read_csv(path_csv_dist)
    df_geo['DISTRITO_CLEAN'] = df_geo['DISTRITO'].apply(clean_string)
    
    # Merge
    # We will do a left join from df_geo so we only keep the ones in the CSV, or maybe all Arequipa?
    # User said "primero ver la coincidencia con los distritos ... que deberian ser los de arequipa"
    # It might be better to output all districts of Arequipa from DBF, and just attach lat/lon if available.
    
    df_final = pd.merge(df_elec, df_geo[['DISTRITO_CLEAN', 'LATITUD', 'LONGITUD']], on='DISTRITO_CLEAN', how='left')
    
    # Drop temp col
    df_final.drop(columns=['DISTRITO_CLEAN'], inplace=True)
    
    # Clasificación sugerida
    # Distritos Críticos (Brecha > 15%) -> Sistemas Off-Grid
    # Distritos de Inestabilidad Urbana (Brecha < 5% pero con alta densidad -> Total Viviendas alto) -> Sistemas On-Grid con Inyección o Backup
    
    # Definimos "alta densidad" como distritos con viviendas por encima de la mediana
    mediana_viviendas = df_final['TOTAL_VIVIENDAS'].median()
    
    def clasificar(row):
        brecha = row['BRECHA_PORCENTAJE']
        viviendas = row['TOTAL_VIVIENDAS']
        
        if brecha > 15:
            return 'Crítico (Off-Grid Aislado)'
        elif brecha < 5 and viviendas > mediana_viviendas:
            return 'Inestabilidad Urbana (On-Grid con Backup)'
        elif brecha < 5:
            return 'Cobertura Óptima (Sin prioridad actual)'
        else:
            return 'Prioridad Media (Evaluación mixta)'
            
    df_final['TIPO_INTERVENCION_SUGERIDA'] = df_final.apply(clasificar, axis=1)
    
    # Sort
    df_final = df_final.sort_values('BRECHA_PORCENTAJE', ascending=False)
    
    out_path = '../data/cleaned/brecha_electrica_distritos_arequipa.csv'
    df_final.to_csv(out_path, index=False)
    print(f"\\nProceso terminado. Datos guardados en: {out_path}")
    
    print("\\nResumen de Tipos de Intervención:")
    print(df_final['TIPO_INTERVENCION_SUGERIDA'].value_counts())
    
    # Report matching
    matched = df_final['LATITUD'].notna().sum()
    print(f"\\nDistritos con coordenadas enlazadas: {matched} de {len(df_final)}")

if __name__ == '__main__':
    main()
