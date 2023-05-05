#IMPORTAR PAQUETES
import numpy as np
import pandas as pd


#Función para hacer un pequeño reporte de los datos que muestre su dimensión, formato de cada vcolumna, nulos, duplicados,
# variables númericas, variables No númericas y sus categorias y información en general acerca del dataframe.

def report_data(data): 
    df=data.copy()
    print('Dimensiones')
    print(df.shape)
    print('-------------------------------------------------')
    print('Formatos de variables')
    print(df.dtypes)
    print('-------------------------------------------------')
    print('Nulos')
    print(df.isnull().sum())
    print('-------------------------------------------------')
    print('Duplicados')
    print(df.duplicated().sum())
    print('-------------------------------------------------')
    print('Variables Númericas')
    print(df.describe())
    print('-------------------------------------------------')
    print('Variables NO Númericas')
    print(df.describe(include = 'object'))
    print('-------------------------------------------------')
    print('Información General de la tabla')
    print(df.info())

#Función para volver columnas binarias.
def get_binary(data,column,field1,field2):
    data[column]=data[column].replace([field1], 1)
    data[column]=data[column].replace([field2], 0)
    return print('Ya es una columna binaria')




