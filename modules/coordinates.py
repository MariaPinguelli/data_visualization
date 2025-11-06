import pandas as pd
import numpy as np
import unicodedata
import re
import difflib

def add_coordinates(table):
    """ Calcula e adiciona colunas de latitude e longitude ás UCs """
    
    new_columns = table.apply(_process_row, axis=1)
    table_with_coords = pd.concat([table, new_columns], axis=1)

    table_with_coords.to_csv('./data/ucs_com_coordenadas.csv', index=False, sep=';')
    
    return table_with_coords


def _process_row(row):
    print(f"Processando UC - {row['nome']}")
    cities = row['municipios']
    cities_list = cities.split(' - ')

    coords = []
    
    for city in cities_list:
        coordinates = _get_coordinates(city)
        coords.append(coordinates)
    
    if coords:
        centro_lat = np.mean([c['lat'] for c in coords])
        centro_lon = np.mean([c['lon'] for c in coords])
    else:
        centro_lat, centro_lon = None, None
    
    return pd.Series({'latitude': centro_lat, 'longitude': centro_lon})


def _get_coordinates(input):
    db_cities = pd.read_csv("./data/municipios.csv")
    db_states = pd.read_csv("./data/estados.csv")

    input_city, input_state = input.split(' (')
    input_state = input_state.replace(')', '')
    
    codigo_uf = db_states[db_states['uf'] == input_state]['codigo_uf'].item()
    
    input_city_normalized = _normalize_name(input_city)
    
    city = db_cities[
        (db_cities['codigo_uf'] == codigo_uf) & 
        (db_cities['nome'].apply(_normalize_name) == input_city_normalized)
    ]
    
    if not city.empty:
        return {
            'lat': city['latitude'].item(),
            'lon': city['longitude'].item()
        }
    
    city_fallback = _find_similar_city(db_cities, codigo_uf, input_city_normalized)
    if city_fallback is not None and not city_fallback.empty:
        return {
            'lat': city_fallback['latitude'].item(),
            'lon': city_fallback['longitude'].item()
        }
    
    return None


def _normalize_name(name):
    name = str(name).upper()
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
    name = re.sub(r'[-_]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def _find_similar_city(db_cities, codigo_uf, input_city_normalized):
    """Busca por cidades similares usando difflib (built-in)"""
    
    cities_in_state = db_cities[db_cities['codigo_uf'] == codigo_uf]
    city_names = cities_in_state['nome'].apply(_normalize_name).tolist()
    
    matches = difflib.get_close_matches(input_city_normalized, city_names, n=1, cutoff=0.8)
    
    if matches:
        best_match = matches[0]
        matched_city = cities_in_state[
            cities_in_state['nome'].apply(_normalize_name) == best_match
        ].iloc[0]
        
        return matched_city
    
    return None