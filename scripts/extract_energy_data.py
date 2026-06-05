import os
import pandas as pd
from dbfread import DBF
import numpy as np

def read_dbf(path):
    print(f"Leyendo {path}...")
    try:
        table = DBF(path, encoding='latin1', load=True)
        df = pd.DataFrame(iter(table))
        return df
    except Exception as e:
        print(f"Error leyendo {path}: {e}")
        return pd.DataFrame()

def main():
    path_escuelas_primaria = '../data/cleaned/listado_escuelas_primaria_y_secundaria_arequipa.csv'
    path_matricula = '../../Matricula_01.dbf'
    path_equipamiento = '../../Equipamiento.dbf'
    
    print("Cargando lista de escuelas primarias...")
    df_escuelas = pd.read_csv(path_escuelas_primaria)
    
    # Extraer también P124B_NO que contiene el indicador proxy (1 = Falta de internet/electricidad)
    cols_base = ['COD_MOD', 'CEN_EDU', 'DISTRITO', 'LOCALIDAD', 'AREA_CENSO', 'GES_DEP', 'NIV_MOD', 'P124B_NO']
    cols_to_keep = [c for c in cols_base if c in df_escuelas.columns]
    df_escuelas = df_escuelas[cols_to_keep]
    df_escuelas['COD_MOD'] = df_escuelas['COD_MOD'].astype(str).str.zfill(7)

    # 3. Matrícula (Impacto)
    df_matricula = read_dbf(path_matricula)
    if not df_matricula.empty and 'COD_MOD' in df_matricula.columns:
        df_matricula['COD_MOD'] = df_matricula['COD_MOD'].astype(str).str.zfill(7)
        cols_d = [f'D{str(i).zfill(2)}' for i in range(1, 15)]
        cols_d_exist = [c for c in cols_d if c in df_matricula.columns]
        for c in cols_d_exist:
            df_matricula[c] = pd.to_numeric(df_matricula[c], errors='coerce').fillna(0)
        if cols_d_exist:
            df_matricula['TOTAL_ALUMNOS'] = df_matricula[cols_d_exist].sum(axis=1)
            df_mat_agg = df_matricula.groupby('COD_MOD')['TOTAL_ALUMNOS'].sum().reset_index()
            df_escuelas = pd.merge(df_escuelas, df_mat_agg, on='COD_MOD', how='left')
    
    # 4. Equipamiento (Carga Tecnológica)
    df_equip = read_dbf(path_equipamiento)
    if not df_equip.empty and 'COD_MOD' in df_equip.columns and 'TIPDATO' in df_equip.columns:
        df_equip['COD_MOD'] = df_equip['COD_MOD'].astype(str).str.zfill(7)
        df_equip['TIPDATO'] = df_equip['TIPDATO'].astype(str).str.zfill(2)
        tipos_validos = ['01', '02', '03', '06']
        df_equip = df_equip[df_equip['TIPDATO'].isin(tipos_validos)]
        if 'D01' in df_equip.columns:
            df_equip['D01'] = pd.to_numeric(df_equip['D01'], errors='coerce').fillna(0)
        if 'D02' in df_equip.columns:
            df_equip['D02'] = pd.to_numeric(df_equip['D02'], errors='coerce').fillna(0)
        df_eq_agg = df_equip.groupby('COD_MOD').agg(
            TOTAL_EQUIPOS_D01=('D01', 'sum'),
            EQUIPOS_OPERATIVOS_D02=('D02', 'sum')
        ).reset_index()
        df_escuelas = pd.merge(df_escuelas, df_eq_agg, on='COD_MOD', how='left')

    # LLenar nulos con 0 para cálculos
    df_escuelas['TOTAL_ALUMNOS'] = df_escuelas['TOTAL_ALUMNOS'].fillna(0)
    df_escuelas['TOTAL_EQUIPOS_D01'] = df_escuelas['TOTAL_EQUIPOS_D01'].fillna(0)

    # Definir clusters o puntajes de prioridad
    # P124B_NO == 1.0 (Falta de internet proxy para electricidad)
    # AREA_CENSO == 2 (Rural)
    
    # Puntuación de Necesidad de Infraestructura (0 a 2)
    # +1 si es Rural
    # +1 si falta internet (P124B_NO == 1)
    df_escuelas['SCORE_CARECIA'] = 0
    if 'AREA_CENSO' in df_escuelas.columns:
        df_escuelas.loc[df_escuelas['AREA_CENSO'] == 2, 'SCORE_CARECIA'] += 1
    if 'P124B_NO' in df_escuelas.columns:
        df_escuelas.loc[df_escuelas['P124B_NO'] == 1.0, 'SCORE_CARECIA'] += 1

    # Puntuación de Impacto (Alumnos y equipos)
    # Normalizamos el numero de alumnos de 0 a 1 (con min-max o percentiles para evitar outliers altos)
    pct_alumnos = df_escuelas['TOTAL_ALUMNOS'].rank(pct=True)
    pct_equipos = df_escuelas['TOTAL_EQUIPOS_D01'].rank(pct=True)
    df_escuelas['SCORE_IMPACTO'] = (pct_alumnos + pct_equipos) / 2.0

    # Clusterización heurística:
    # URGENTE: SCORE_CARECIA > 0 y SCORE_IMPACTO > 0.6 (alta necesidad, muchos alumnos/equipos)
    # MEDIA: SCORE_CARECIA > 0 y SCORE_IMPACTO <= 0.6
    # BAJA: SCORE_CARECIA == 0 
    
    condiciones = [
        (df_escuelas['SCORE_CARECIA'] > 0) & (df_escuelas['SCORE_IMPACTO'] > 0.6),
        (df_escuelas['SCORE_CARECIA'] > 0) & (df_escuelas['SCORE_IMPACTO'] <= 0.6),
        (df_escuelas['SCORE_CARECIA'] == 0)
    ]
    valores = ['ALTA/URGENTE', 'MEDIA', 'BAJA']
    df_escuelas['PRIORIDAD_PANEL_SOLAR'] = np.select(condiciones, valores, default='BAJA')

    # Guardar
    out_path = '../data/cleaned/escuelas_con_energia_y_equipos.csv'
    df_escuelas.to_csv(out_path, index=False)
    print(f"\\nProceso terminado. Datos guardados en: {out_path}")
    
    print("\\nDistribución de Prioridades:")
    print(df_escuelas['PRIORIDAD_PANEL_SOLAR'].value_counts())

if __name__ == '__main__':
    main()
