import csv

def read_data():
    """ Versão simples usando apenas biblioteca padrão """

    file_path = './data/cnuc_2025_08.csv'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            data = list(reader)
            
            print(f"Dados carregados: {len(data)} registros")
            print(f"Colunas: {reader.fieldnames}")
            
            return data, reader.fieldnames
            
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None, None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None, None