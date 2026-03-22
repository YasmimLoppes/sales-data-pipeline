import pandas as pd
from sqlalchemy import create_engine

def run_pipeline():
    print("🚀 Iniciando Pipeline de Vendas...")
    
    try:
        # Lendo o arquivo exato que vi no seu VS Code
        df = pd.read_csv('data/vendas_dia_01.csv')
        df.columns = df.columns.str.strip() # Remove espaços bobos nos nomes
        print(f"✅ Colunas encontradas: {list(df.columns)}")
    except Exception as e:
        print(f"❌ Erro ao abrir o arquivo: {e}")
        return

    print("🧹 Transformando dados...")
    # Ajustando para usar a coluna 'valor' que vi na sua foto
    if 'valor' in df.columns:
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce').fillna(0)
        
        # Criando as colunas necessárias para o dashboard
        df['quantidade'] = 1 # Como não tem a coluna quantidade no CSV, cada linha vale 1
        df['valor_unitario'] = df['valor']
        df['imposto'] = df['valor'] * 0.10
        df['receita_total'] = df['valor']
        df['data_processamento'] = pd.Timestamp.now()
    else:
        print("❌ Erro: Coluna 'valor' não encontrada no CSV!")
        return

    print("📥 Carregando no PostgreSQL...")
    try:
        # Conexão direta (vi no seu docker-compose que a porta interna é 5432)
        engine = create_engine('postgresql://postgres:postgres@localhost:5433/vendas_db')
        df.to_sql('vendas_limpas', engine, if_exists='replace', index=False)
        print("✅ Dados carregados com sucesso!")
    except Exception as e:
        print(f"❌ Erro na carga: {e}")

if __name__ == "__main__":
    run_pipeline()