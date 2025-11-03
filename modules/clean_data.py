def clean_data(raw_data, raw_fields):
    """ Limpa colunas sem importância e dados fora do padrão"""
    print("Iniciando limpeza dos dados...")
    
    print(f"Dados brutos: {len(raw_data)} registros, {len(raw_fields)} colunas")
    
    COLUNAS_PARA_REMOVER = [
        'coluna1', 'coluna2', 'codigo', 'id',
        'observacoes', 'notes', 'comentarios'
    ]
    
    # 1. Identificar colunas vazias ou com poucos dados
    colunas_vazias = []
    colunas_poucos_dados = []
    
    for field in raw_fields:
        # Conta valores não vazios
        valores_nao_vazios = sum(1 for row in raw_data if row.get(field) and str(row.get(field)).strip())
        vazios = len(raw_data) - valores_nao_vazios
        
        if valores_nao_vazios == 0:
            colunas_vazias.append(field)
        elif vazios / len(raw_data) > 0.8:  # Mais de 80% vazios
            colunas_poucos_dados.append((field, valores_nao_vazios, vazios))
    
    print(f"\n🔍 Análise de colunas:")
    print(f"Colunas completamente vazias: {len(colunas_vazias)}")
    print(f"Colunas com muitos dados faltantes: {len(colunas_poucos_dados)}")
    
    # 2. Definir colunas para manter
    colunas_para_manter = []
    
    for field in raw_fields:
        # Remove colunas vazias
        if field in colunas_vazias:
            continue
            
        # Remove colunas da lista personalizada
        if any(coluna.lower() in field.lower() for coluna in COLUNAS_PARA_REMOVER):
            continue
            
        # Remove colunas com muitos dados faltantes (opcional)
        # if field in [col[0] for col in colunas_poucos_dados]:
        #     continue
            
        colunas_para_manter.append(field)
    
    print(f"Colunas mantidas: {len(colunas_para_manter)}")
    
    # 3. Filtrar os dados mantendo apenas as colunas selecionadas
    cleaned_data = []
    for row in raw_data:
        cleaned_row = {}
        for field in colunas_para_manter:
            cleaned_row[field] = row.get(field, '')
        cleaned_data.append(cleaned_row)
    
    print(f"✅ Limpeza concluída: {len(cleaned_data)} registros, {len(colunas_para_manter)} colunas")
    
    return cleaned_data, colunas_para_manter