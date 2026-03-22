import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Sales Insights - Yasmim", page_icon="📊", layout="wide")

st.title("📊 Dashboard de Vendas - Pipeline ETL")
st.markdown("---")

# Mesma conexão do pipeline (Porta 5433 conforme seu Docker)
DB_URL = "postgresql://postgres:postgres@localhost:5433/vendas_db"

@st.cache_data
def carregar_dados():
    try:
        engine = create_engine(DB_URL)
        return pd.read_sql("SELECT * FROM vendas_limpas", engine)
    except:
        return None

df = carregar_dados()

if df is not None:
    # Métricas calculadas
    receita = df['receita_total'].sum()
    impostos = df['imposto'].sum()
    vendas = len(df)

    m1, m2, m3 = st.columns(3)
    m1.metric("Total de Vendas", f"{vendas} pedidos")
    m2.metric("Faturamento", f"R$ {receita:,.2f}")
    m3.metric("Impostos (10%)", f"R$ {impostos:,.2f}")

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Vendas por Produto")
        # Gráfico usando a coluna 'produto' e 'valor'
        vendas_prod = df.groupby('produto')['valor'].sum().sort_values(ascending=False)
        st.bar_chart(vendas_prod)
    
    with col2:
        st.subheader("Visualização dos Dados")
        st.dataframe(df[['id_venda', 'produto', 'valor', 'data_venda']], use_container_width=True)
else:
    st.error("Aguardando carga de dados... Rode o pipeline.py primeiro!")