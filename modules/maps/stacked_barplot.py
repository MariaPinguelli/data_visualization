import plotly.graph_objects as go

# Dados de área total por bioma (https://bdiaweb.ibge.gov.br/#/consulta/pesquisa)
AREAS_BIOMAS = {
    'Amazônia': 4_219_210 * 100,
    'Caatinga': 862_960 * 100,
    'Cerrado': 1_984_922 * 100,  
    'Mata Atlântica': 1_109_125 * 100,
    'Pampa': 194_587 * 100,
    'Pantanal': 151_299 * 100,
}

def create_percentage_stacked_bar(table):
    """Versão com cores mais suaves e anotações"""

    table = table[table['bioma'] != 'Área Marinha'].copy()
    
    valid_data = table[
        (table['criado_em'].notna()) & 
        (table['area'] > 0)
    ].copy()
    
    area_protegida = valid_data.groupby('bioma').agg({
        'area': 'sum',
        'id': 'count'
    }).reset_index()
    
    area_protegida['area_total'] = area_protegida['bioma'].map(AREAS_BIOMAS)
    area_protegida['percentual_protegido'] = (area_protegida['area'] / area_protegida['area_total'] * 100).round(1)
    area_protegida['percentual_nao_protegido'] = 100 - area_protegida['percentual_protegido']
    
    area_protegida = area_protegida.sort_values('percentual_protegido', ascending=True)
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Área Protegida',
        y=area_protegida['bioma'],
        x=area_protegida['percentual_protegido'],
        orientation='h',
        marker=dict(color='#1C571F'),
        hovertemplate='<b>%{y}</b><br>Protegida: %{x:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Área Não Protegida',
        y=area_protegida['bioma'],
        x=area_protegida['percentual_nao_protegido'],
        orientation='h',
        marker=dict(color='lightgray'),
        hovertemplate='<b>%{y}</b><br>Não Protegida: %{x:.1f}%<extra></extra>'
    ))
    
    for i, row in area_protegida.iterrows():
        fig.add_annotation(
            x=row['percentual_protegido'] / 2,
            y=row['bioma'],
            text=f"{row['percentual_protegido']}%",
            showarrow=False,
            font=dict(size=10, color='white', weight='bold'),
            xanchor='center'
        )
        
        fig.add_annotation(
            x=row['percentual_protegido'] + (row['percentual_nao_protegido'] / 2),
            y=row['bioma'],
            text=f"{row['percentual_nao_protegido']}%",
            showarrow=False,
            font=dict(size=10, color='black'),
            xanchor='center'
        )
    
    fig.update_layout(
        title='<b>Cobertura de Áreas Protegidas por Bioma</b>',
        xaxis_title='Percentual do Bioma (%)',
        yaxis_title='Bioma',
        barmode='stack',
        height=500,
        showlegend=True,
        xaxis=dict(range=[0, 100]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def stacked_barplot(table):
    """Função principal para o gráfico de percentuais"""
    
    fig = create_percentage_stacked_bar(table)
    
    try:
        fig.write_html('./output_maps/stacked_barplot.html')
        fig.show()
    except Exception as e:
        print(f"Erro: {e}")
    
    return fig