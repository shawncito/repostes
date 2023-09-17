import pandas as pd 



def eliminar_columnas(df):
    # Leer el archivo de datos
    df = pd.read_csv("RPT-RA-18-Notas_Periodo_Estudiante.xlsx")

    columna_nota = df['F']
    
