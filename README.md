# 🚀 Sales Data Pipeline & Monitoring Engine

Este projeto simula um cenário real de **Engenharia de Dados**, onde arquivos de vendas diárias são extraídos, tratados e carregados de forma automatizada em um banco de dados estruturado para análise em um dashboard interativo de alta performance.

## 📊 Visual do Dashboard
![Dashboard Preview](./dashboard-preview.png)
> *Interface moderna com visual neon desenvolvida para monitoramento de ingestão de dados.*

## 🛠️ Stack Tecnológica
* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas
* **Banco de Dados:** PostgreSQL 15 (Dockerizado)
* **Conectividade:** SQLAlchemy & Psycopg2
* **Frontend:** React, Tailwind CSS e Recharts (Vite)
* **Infraestrutura:** Docker & Docker Compose

## 🏗️ Arquitetura do Projeto
1. **Extração (Extract):** Leitura de arquivos `.csv` brutos na pasta `/data`.
2. **Transformação (Transform):** Limpeza de nomes de colunas, tratamento de nulos e cálculo automático de impostos (10%).
3. **Carga (Load):** Ingestão automatizada dos dados limpos no PostgreSQL.
4. **Visualização:** Dashboard React que consome as métricas de ingestão e fluxo.

## 🚀 Como Executar o Frontend
1. Entre na pasta: `cd frontend`
2. Instale as dependências: `npm install`
3. Inicie o servidor: `npm run dev`