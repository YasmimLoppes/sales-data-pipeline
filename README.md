# sales-data-pipeline
Pipeline de dados ETL (Extract, Transform, Load) automatizado com Python, Pandas e PostgreSQL via Docker, focado em tratamento de dados brutos de vendas e segurança de credenciais. 🚀☁️


# 📊 Sales Data Pipeline: ETL com Docker & PostgreSQL

Este projeto simula um cenário real de **Engenharia de Dados**, onde arquivos de vendas diárias são extraídos, tratados e carregados de forma automatizada em um banco de dados estruturado para análise em um dashboard interativo.

## 🚀 Stack Tecnológica
- **Linguagem:** Python 3.x
- **Manipulação de Dados:** Pandas
- **Banco de Dados:** PostgreSQL 15 (Dockerizado)
- **Conectividade:** SQLAlchemy & Psycopg2
- **Dashboard:** Streamlit
- **Infraestrutura:** Docker & Docker Compose

## 🛠️ Arquitetura do Projeto
O pipeline foi estruturado seguindo as melhores práticas de **DataOps**:

1.  **Extração (Extract):** Leitura de arquivos `.csv` brutos (ex: `vendas_dia_01.csv`) na pasta `/data`.
2.  **Transformação (Transform):** - Limpeza de nomes de colunas e tratamento de valores nulos (NaN).
    - Conversão de tipos de dados.
    - **Feature Engineering:** Cálculo automático de impostos (10%) e receita total.
3.  **Carga (Load):** Ingestão automatizada dos dados limpos no **PostgreSQL** rodando em container.

## ⚙️ Como Executar

### 1. Preparar o Ambiente
Certifique-se de que o **Docker Desktop** está rodando. No terminal, suba o banco de dados:
```bash
docker-compose up -d
