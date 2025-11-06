import pandas as pd
from config import NUMERIC_COLUMNS

def format_data_types(table):
    """ Formatação de dados numéricos """
    
    for col in NUMERIC_COLUMNS:
        table[col] = (
            table[col]
            .astype(str)
            .str.replace(r'\.', '', regex=True)
            .str.replace(r',', '.', regex=True)
            .str.replace(r'[^\d.-]', '', regex=True)
            .pipe(pd.to_numeric, errors='coerce')
            .fillna(0)
        )
    return table
    