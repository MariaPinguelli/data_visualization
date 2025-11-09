from modules.read_data import read_data
from modules.clean_data import clean_data
from modules.format_data import format_data_types
from modules.maps.bubble_map import bubble_map
from modules.maps.tree_map import tree_map

def main():
    print('\nIniciando ...\n')
    print('1. Leitura de dados')
    raw_data = read_data('./data/cnuc_2025_08.csv')

    print('2. Limpeza de dados')
    table = clean_data(raw_data)

    print('3. Formatação de dados')
    table = format_data_types(table)

    print('4. Visualização de Bubble Map')
    bubble_map(table)

    print('5. Visualização de Tree Map')
    tree_map(table)

    print('\nFim!\n')

if __name__ == '__main__':
    main()