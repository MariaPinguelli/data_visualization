from modules.read_data import read_data
from modules.clean_data import clean_data

def main():
    # ler dados de entrada
    raw_data, raw_fieldnames = read_data()

    # Tratar dados de entrada
    data, fields = clean_data(raw_data, raw_fieldnames)

    print(f"\n🎉 DADOS PRONTOS PARA ANÁLISE:")
    print(f"   • Registros: {len(data)}")
    print(f"   • Colunas: {len(fields)}")
    print(f"   • Colunas disponíveis: {fields}")

    # manipular para as visualizações

    # visualização 1
    # visualização 2

if __name__ == '__main__':
    main()