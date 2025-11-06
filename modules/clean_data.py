from config import COLUMNS_TO_REMOVE, COLUMN_MAPPING

def clean_data(raw_data):
    """ Limpa colunas sem importância e renomeia as colunas """
    
    empty_columns = raw_data.columns[raw_data.isnull().all()].tolist()
    columns_to_drop = empty_columns + [col for col in COLUMNS_TO_REMOVE if col in raw_data.columns]
    
    cleaned_data = raw_data.drop(columns=columns_to_drop)
    
    existing_columns = {k: v for k, v in COLUMN_MAPPING.items() if k in cleaned_data.columns}
    cleaned_data = cleaned_data.rename(columns=existing_columns)
    
    return cleaned_data