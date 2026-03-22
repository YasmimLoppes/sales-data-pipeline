# sales-data-pipeline
Pipeline de dados ETL (Extract, Transform, Load) automatizado com Python, Pandas e PostgreSQL via Docker, focado em tratamento de dados brutos de vendas e segurança de credenciais. 🚀☁️


# 🚀 Sales Data Pipeline: Processamento ETL com Docker

Este projeto simula um cenário real de **Engenharia de Dados**, onde arquivos de vendas diárias são recepcionados, tratados e carregados de forma automatizada em um banco de dados estruturado para análise.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.x
- **Manipulação de Dados:** Pandas
- **Banco de Dados:** PostgreSQL 15
- **Infraestrutura:** Docker & Docker Compose (Containerização)
- **Conectividade:** SQLAlchemy & Psycopg2
- **Segurança:** Gestão de credenciais via variáveis de ambiente (`.env`)

## ⚙️ Arquitetura do Projeto
O pipeline foi estruturado seguindo as melhores práticas de **DataOps**:

1.  **Extração (Extract):** Leitura de arquivos `.csv` brutos localizados na pasta `/data`.
2.  **Transformação (Transform):** * Tratamento de valores ausentes (NaN).
    * Padronização de strings (Capitalização de nomes de produtos).
    * Feature Engineering: Cálculo automático de impostos (10% sobre o valor).
3.  **Carga (Load):** Ingestão automatizada dos dados limpos no **PostgreSQL** rodando em container.

## 🚀 Como Executar
1. Clone o repositório.
2. Certifique-se de que o **Docker Desktop** está rodando.
3. Suba o banco de dados:
   ```bash
   docker-compose up -d
