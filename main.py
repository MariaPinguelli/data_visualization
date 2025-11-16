from modules.read_data import read_data
from modules.clean_data import clean_data
from modules.format_data import format_data_types
from modules.maps.bubble_map import bubble_map
from modules.maps.tree_map import tree_map
from modules.maps.stackplot import stackplot
from modules.maps.sunburst import sunburst
from modules.maps.stacked_barplot import stacked_barplot

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

    print('6. Visualização Stackplot')
    stackplot(table)

    print('7. Visualização Sunburst')
    sunburst(table)

    print('8. Visualização barplot')
    stacked_barplot(table)

    print('\nFim!\n')

if __name__ == '__main__':
    main()