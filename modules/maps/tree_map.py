import plotly.express as px

def tree_map(table):
    """Treemap só com categorias, cores indicam o grupo"""
    
    counts = table.groupby(['grupo', 'categoria']).size().reset_index(name='count')
    total_ucs = len(table)
    
    counts['percent_total'] = (counts['count'] / total_ucs * 100).round(2)
    
    fig = px.treemap(
        counts, 
        path=['categoria'],
        values='count', 
        color='grupo',
        color_discrete_map={
            'Uso Sustentável': '#005EAB',
            'Proteção Integral': '#1C571F'
        },
        title=f'Unidades de Conservação por Categoria<br><sub>Total: {total_ucs} UCs</sub>'
    )

    fig.update_traces(
        textinfo="label+value",
        hovertemplate=(
            '<b>%{label}</b><br>'
            'Grupo: %{customdata[1]}<br>'
            'Quantidade: %{value} UCs<br>'
            'Porcentagem do total: %{customdata[0]:.2f}%<br>'
            '<extra></extra>'
        ),
        customdata=counts[['percent_total', 'grupo']].values
    )

    fig.update_layout(
        annotations=[
            dict(
                x=0.25, y=1.1,
                xref="paper", yref="paper",
                text="<b>Legenda:</b><br>🟦 Uso Sustentável<br>🟩 Proteção Integral",
                showarrow=False,
                bgcolor="white",
                bordercolor="black",
                borderwidth=1,
                borderpad=10,
                align="left"
            )
        ]
    )
    
    print('     Mapa gerado!')
    fig.show()
    fig.write_html('./output_maps/tree_map.html')