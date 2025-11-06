"""Configurações do projeto - Constantes e mapeamentos"""
DATASET = './data/cnuc_2025_08.csv'
DATASET_COORDS = './data/ucs_com_coordenadas.csv'

COLUMNS_TO_REMOVE = [
    'ID_UC', 
    'Outros atos legais', 
    'Categoria IUCN',
    'Plano de Manejo',
    'Conselho Gestor',
    'Órgão Gestor',
    'Fonte da Área: (1 = SHP, 0 = Ato legal)',
    'Área soma Biomas Continental',
    'Área Ato Legal de Criação',
    '% Além da linha de costa',
    'PI',
    'US',
    'Recortes (ha)',
    'Mar Territorial',
    'Município Costeiro',
    'Município Costeiro + Área Marinha',
    'Programa/Projeto',
    'Sítios do Patrimônio Mundial',
    'Sítios Ramsar',
    'Mosaico',
    'Código WDPA'
]

COLUMN_MAPPING = {
    'Código UC': 'id',
    'Nome da UC': 'nome',
    'Esfera Administrativa': 'esfera',
    'Grupo': 'grupo',
    'Categoria de Manejo': 'categoria',
    'UF': 'uf',
    'Ano de Criação': 'criado_em',
    'Municípios Abrangidos': 'municipios',
    'Área soma biomas': 'area',
    'Amazônia': 'amazonia',
    'Caatinga': 'caatinga',
    'Cerrado': 'cerrado',
    'Mata Atlântica': 'mata',
    'Pampa': 'pampa',
    'Pantanal': 'pantanal',
    'Área Marinha': 'mar',
    'Bioma declarado': 'bioma'
}

NUMERIC_COLUMNS = [
    'criado_em',
    'area',
    'amazonia',
    'caatinga',
    'cerrado',
    'mata',
    'pampa',
    'pantanal',
    'mar'
]