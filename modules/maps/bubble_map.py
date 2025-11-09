import numpy as np
import folium
from modules.coordinates import add_coordinates
from modules.read_data import read_data
from config import DATASET_COORDS

def bubble_map(table):
    """ 
        UC centralizada entre os municipios do qual faz parte, 
        seu tamanho é referente a sua área, 
        e ao passar o mouse pode visualizar a lista de municipios daquela UC e outros dados
    """
    
    saved_table = read_data(DATASET_COORDS)

    if saved_table is None or saved_table.empty:
        print('     Adicionando coordenadas')
        table = add_coordinates(table)
    else:
        table = saved_table

    map = folium.Map(
        location=[-10, -55],
        zoom_start=4,
        tiles='cartodb positron'
    )
    
    print('     Adicionando pontos no mapa...')
    for i, row in table.iterrows():
        square_meter = row['area'] * 10000
        radius = np.round(np.sqrt(square_meter / np.pi), 2)
        
        cities_list = row['municipios'].split(' - ')
        
        tooltip_string = f"""
            🌳 <b>{row['nome']}</b><br>
            📏 <b>Área:</b> {row['area']:,.0f} ha<br>
            🏷️ <b>Categoria:</b> {row['categoria']}<br>
            📍 <b>Estado:</b> {row['uf']}<br>
            🏙️ <b>Municípios ({len(cities_list)}):</b> {'<br>• ' + '<br>• '.join(cities_list)}
        """

        folium.Circle(
            location=[row['latitude'], row['longitude']],
            radius=radius,
            color='#0a9396',
            fill=True,
            fill_color='#0a9396',
            fill_opacity=0.5,
            weight=1,
            tooltip=folium.Tooltip(tooltip_string, sticky=True)
        ).add_to(map)

    print('     Mapa gerado!')
    map.save('./output_maps/bubble_map.html')
