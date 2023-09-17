import pandas as pd

# Leer el archivo Excel
df = pd.read_excel('RPT-RA-18-NotasPeriodoEstudiante (1).xlsx')

# Verificar si 'F' está en la primera fila de cada columna
mascara = df.iloc[0] == 'F'

# Filtrar el DataFrame utilizando la máscara
df_filtrado = df.loc[:, mascara]

# Solicitar al usuario el nombre del nuevo archivo
nombre_archivo = input("Ingrese el nombre del nuevo reporte: ")

# Guardar el DataFrame filtrado en un nuevo archivo de Excel
df_filtrado.to_excel(nombre_archivo + '.xlsx', index=False)
print(mascara)
print("aaaaaaaaaa")
print(df_filtrado)
