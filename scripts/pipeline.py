import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Configurações de Ambiente (Segurança)
load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def run_pipeline():
    print("🚀 Iniciando Pipeline de Vendas...")
    
    # --- EXTRAÇÃO ---
    # Lendo o arquivo CSV que geramos na pasta data/
    path_input = 'data/vendas_dia_01.csv'
    df = pd.read_csv(path_input)
    
    # --- TRANSFORMAÇÃO ---
    print("🧹 Transformando dados...")
    # 1. Remover linhas sem nome de produto
    df = df.dropna(subset=['produto'])
    
    # 2. Padronizar nomes (Primeira letra Maiúscula)
    df['produto'] = df['produto'].str.capitalize()
    
    # 3. Criar coluna de Imposto (10% do valor)
    df['imposto'] = df['valor'] * 0.10
    
    # --- CARGA ---
    print("📥 Carregando no PostgreSQL...")
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    # Salva no banco de dados (se a tabela já existir, ele substitui)
    df.to_sql('vendas_limpas', engine, if_exists='replace', index=False)
    
    print("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()