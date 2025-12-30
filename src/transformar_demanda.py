# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 11:42:45 2025

@author: USER
"""
import pandas as pd

def transform_demanda():
    path =(r"D:\DOCUMENTOS\PERSONAL\Documents\DOCUMENTOS\Desktop\sergio\DATACAMP\proenerg\data\rawdat\demanda_raw.csv")
    df = pd.read_csv(path, sep = ',')
    
    print("Columnas disponibles:")
    print(df.columns)
    
    df['fecha'] = pd.to_datetime(df['FechaHora'])
    df['consumo_kWh'] = df['Valor'].astype(float)
    df['region'] = df['MercadoComercializacion']    
    consumo_region = (df.groupby(['fecha','region'])['consumo_kWh'].sum().reset_index())
    consumo_region['fecha'] = consumo_region['fecha'].dt.date
    
    
    return consumo_region


consumo_region = transform_demanda()
print(consumo_region.head(10))

if __name__ == "__main__":
    df = transform_demanda()
    df.to_csv(r"D:\DOCUMENTOS\PERSONAL\Documents\DOCUMENTOS\Desktop\sergio\DATACAMP\proenerg\data\processed\consumo_region.csv", index = False)