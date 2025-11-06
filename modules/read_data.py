import pandas as pd

def read_data(file_path):
    """ Leitura de Dados """
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = pd.read_csv(file, delimiter=';')
            
            return data
            
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None