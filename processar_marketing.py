from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

# Inicia a sessão do Spark
spark = SparkSession.builder \
    .appName("AnaliseMarketingROI") \
    .getOrCreate()

# 1. Lendo os dados
try:
    df_marketing = spark.read.csv("data/marketing/campanhas_marketing.csv", header=True, inferSchema=True)

    print("\n" + "="*30)
    print("DADOS BRUTOS DE MARKETING")
    print("="*30)
    df_marketing.show()

    # 2. Transformação: Calculando CPC e Conversão
    df_transformado = df_marketing.withColumn("CPC", round(col("investimento") / col("cliques"), 2)) \
                                   .withColumn("Conversao_%", round((col("vendas") / col("cliques")) * 100, 2))

    print("="*30)
    print("ANÁLISE DE PERFORMANCE (ROI/ENGAJAMENTO)")
    print("="*30)
    df_transformado.select("nome_plataforma", "investimento", "CPC", "Conversao_%").show()

except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

# Finaliza a sessão