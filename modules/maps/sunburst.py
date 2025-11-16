import plotly.express as px

def prepare_data(table):
    """Prepara dados"""
    
    valid_data = table[
        (table['criado_em'].notna()) & 
        (table['area'] > 0)
    ].copy()
    
    return valid_data

def create_sunburst_chart(table):
    """Cria gráfico sunburst"""
    
    data = prepare_data(table)
    
    fig = px.sunburst(
        data,
        path=['bioma', 'grupo', 'categoria'],
        values='area',
        title='Distribuição de Área Protegida por Bioma, Grupo e Categoria',
        color='bioma',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hover_data={
            'area': ':.0f',
            'id': 'count'
        },
        height=800
    )
    
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>' +
                     'Área: %{value:,.0f} ha<br>' +
                     'Percentual do nível: %{percentParent:.1%}<br>' +
                     '<extra></extra>'
    )
    
    fig.update_layout(
        font_size=12,
        margin=dict(t=50, l=0, r=0, b=0)
    )
    
    return fig

def sunburst(table):
    fig = create_sunburst_chart(table)
    
    try:
        fig.write_html('./output_maps/sunburst.html')
        fig.show()
        
    except Exception as e:
        print(f"Erro ao salvar: {e}")
    
    return fig