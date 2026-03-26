# ?? Enterprise Sales Data Pipeline: Do Zero ao Big Data

Bem-vindo ao meu projeto de **Engenharia de Dados**! Este repositório é o resultado de um desafio pessoal: construir um ecossistema completo que integra marketing e finanças, saindo do básico e mergulhando de cabeça em tecnologias que as grandes empresas usam hoje.

---

## ?? O Porquê deste Projeto
Muitas vezes, as empresas têm dados espalhados em planilhas e plataformas diferentes. O meu objetivo aqui foi criar uma "ponte" automática: pegar esses dados brutos, processar com inteligência e entregar um dashboard pronto para a tomada de decisão. 

Não é apenas um código que roda; é uma solução pensada para **escala e performance**.

---

## ??? O que tem "debaixo do capô"?

* **Apache Spark (PySpark):** O coração do projeto. Escolhi o Spark porque, no mundo real, os dados crescem rápido. Ele me permite processar milhões de linhas de forma distribuída, algo que o Python comum sofreria para fazer.
* **Docker & PostgreSQL:** Usei Docker para garantir que o banco de dados suba em qualquer máquina sem erro. O Postgres é a nossa "fonte da verdade".
* **Python 3.11+:** A linguagem que orquestra tudo, desde a limpeza dos dados até a carga no banco.
* **React & Tailwind CSS:** Para o monitoramento visual. Porque dados processados precisam ser dados entendidos.

---

## ?? Os Desafios (Onde o filho chora e a mãe não vê!)

Nem tudo foram flores. Durante o desenvolvimento, enfrentei desafios que me ensinaram muito sobre resiliência técnica:

1.  **A briga com o Spark no Windows:** Quem já tentou configurar o Spark sabe o que é o erro do \winutils.exe\ e as variáveis de ambiente. Foram horas ajustando o Hadoop e o JDK 17 até o Spark finalmente "falar" com o meu Windows. Resolver isso me deu uma base sólida de infraestrutura que eu não tinha.
2.  **Lógica de Negócio Real:** Não bastava somar números. Tive que implementar lógica de **ROI (Retorno sobre Investimento)** e cruzamento de metas de vendas. Ver a tabela do Spark calculando que eu bati **116.67% da meta** foi a melhor recompensa do dia!
3.  **Arquitetura de Medalhão:** Organizei os dados em camadas (Bronze, Silver, Gold). Isso garante que o pipeline seja organizado e fácil de debugar se algo der errado no meio do caminho.

---

## ?? Visual do Dashboard
![Visual do Dashboard](./dashboard-preview.jpg)

---

## ?? Como testar na sua máquina

1.  **Prepare o terreno (Docker):**
    \\\powershell
    docker-compose up -d
    \\\
2.  **Ligue os Motores (Spark):**
    \\\powershell
    python scripts/processar_marketing.py
    python scripts/processar_financeiro.py
    \\\
3.  **Veja a Mágica (Frontend):**
    \\\powershell
    cd frontend && npm install && npm run dev
    \\\

---

## ????? Sobre a Desenvolvedora
Sou a **Yasmim Lopes**, estudante de ADS (3º semestre). Sou apaixonada por resolver quebra-cabeças com dados. Este projeto é o meu "cartão de visitas" para mostrar que estou pronta para os desafios reais da Engenharia de Dados. ??
