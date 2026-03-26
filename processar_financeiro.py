from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, when

# Inicia a sessão do Spark
spark = SparkSession.builder \
    .appName("AnaliseFinanceiraVendas") \
    .getOrCreate()

# 1. Lendo os dados financeiros
try:
    df_financeiro = spark.read.csv("data/financeiro/vendas_metas.csv", header=True, inferSchema=True)

    print("\n" + "="*40)
    print("RELATÓRIO FINANCEIRO: VENDAS VS METAS")
    print("="*40)

    # 2. Transformação: Calculando % da Meta e Status
    df_final = df_financeiro.withColumn(
        "Alcancado_%", 
        round((col("vendas_realizadas") / col("meta_mensal")) * 100, 2)
    ).withColumn(
        "Status",
        when(col("Alcancado_%") >= 100, "✅ META BATIDA").otherwise("❌ ABAIXO DA META")
    )

    # Exibindo o resultado final
    df_final.select("nome_vendedor", "vendas_realizadas", "meta_mensal", "Alcancado_%", "Status").show()

except Exception as e:
    print(f"Erro no processamento: {e}")

# Finaliza a sessão
spark.stop()