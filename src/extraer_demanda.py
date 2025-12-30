# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 11:25:42 2025

@author: USER
"""

from pydataxm.pydatasimem import ReadSIMEM
import pandas as pd

def extract_demanda():
    dataset_id = 'c1b851'  # se reemplaza
    fecha_inicio = '2024-01-01'
    fecha_fin = '2024-01-31'

    reader = ReadSIMEM(dataset_id, fecha_inicio, fecha_fin)
    df = reader.main(filter=False)

    return df

if __name__ == "__main__":
    extract_demanda()
    df.to_csv(r"D:\DOCUMENTOS\PERSONAL\Documents\DOCUMENTOS\Desktop\sergio\DATACAMP\proenerg\data\rawdat\demanda_raw.csv", index=False)


