import altair as alt
import pandas as pd

AREA_BRASIL_HA = 851_600_000

def process_data(table):
    """Prepara dados"""
    
    valid_data = table[
        (table['criado_em'].notna()) & 
        (table['criado_em'] > 0) &
        (table['area'] > 0)
    ].copy()

    valid_data['data_criacao'] = pd.to_datetime(
        valid_data['criado_em'].astype(int).astype(str) + '-01-01'
    )

    yearly_data = valid_data.groupby(['data_criacao', 'grupo']).agg({
        'id': 'count',
        'area': 'sum'
    }).reset_index()

    yearly_data = yearly_data.sort_values(['grupo', 'data_criacao'])
    
    yearly_data['id_acumulado'] = yearly_data.groupby('grupo')['id'].cumsum()
    yearly_data['area_acumulada'] = yearly_data.groupby('grupo')['area'].cumsum()

    goal_area = AREA_BRASIL_HA * 0.3
    yearly_data['area_percent'] = yearly_data['area_acumulada'] / goal_area
    
    return yearly_data

def create_simple_stackplot(table):
    """Stackplot com todos os grupos inicialmente selecionados"""
    
    data = process_data(table)
    
    grupos_unicos = data['grupo'].unique().tolist()

    legend_data = pd.DataFrame({'grupo': grupos_unicos})
    
    selection = alt.selection_point(
        fields=['grupo'],
        bind='legend',
        value=[{"grupo": grupo} for grupo in grupos_unicos]
    )
    
    chart = alt.Chart(data).mark_area(
        opacity=1,
        stroke='white',
        strokeWidth=0.5
    ).encode(
        x=alt.X('yearmonth(data_criacao):T')
            .axis(format='%Y', title='Ano de Criação'),
        
        y=alt.Y('area_percent:Q', title='Progresso em Relação à Meta 30%', stack=True, scale=alt.Scale(domain=[0, 1.05]))
            .axis(format='%'),
        
        color=alt.Color('grupo:N', title='Clique para Remover/Adicionar:')
            .legend(orient='right').scale(domain=grupos_unicos),
        
        tooltip=[
            alt.Tooltip('data_criacao:T', title='Ano', format='%Y'),
            alt.Tooltip('grupo:N', title='Grupo'), 
            alt.Tooltip('area_percent:Q', title='Progresso da Meta', format='.1%'),
            alt.Tooltip('area_acumulada:Q', title='Área Acumulada (ha)', format=',.0f'),
            alt.Tooltip('id_acumulado:Q', title='UCs Acumuladas')
        ]
    ).transform_filter(
        selection
    ).properties(
        title={
            "text": "Área Protegida por Grupo de Manejo",
            "subtitle": "Clique na legenda para remover/readicionar grupos completamente"
        },
        width=1300,
        height=750
    ).add_params(
        selection
    ).interactive()
    
    return chart

def stackplot(table):
    chart = create_simple_stackplot(table)
    
    try:
        chart.save('./output_maps/stackplot.html')
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        print("Retornando chart para visualização...")
    
    return chart