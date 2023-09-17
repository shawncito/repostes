import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('RPT-RA-18-NotasPeriodoEstudiante (1).xlsx')

# Seleccionar toda la columna 'Nota'
columna_nota = df['F']

# Solicitar al usuario el nombre del nuevo archivo
nombre_archivo = input("Ingrese el nombre del nuevo reporte: ")

# Crear un nuevo DataFrame con solo la columna 'Nota'
df_nueva = pd.DataFrame({'F': columna_nota})

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(nombre_archivo + '.xlsx', index=False)

