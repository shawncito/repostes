import pandas as pd
df = pd.read_excel('RPT-RA-18-NotasPeriodoEstudiante (1).xlsx')  # Cambia 'archivo.xlsx' al nombre de tu archivo Excelhol

#hola = input("Ingrese el nombre del archivo: ")

df.to_excel('pepe.xlsx', index=False)  # Cambia 'nuevo_archivo.xlsx' al nombre que desees
