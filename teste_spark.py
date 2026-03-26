import os
import sys
from pyspark.sql import SparkSession

# Garante que o Spark use o executável do Python que você está rodando
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Configuração de REDE LOCAL para evitar o erro de host.docker
spark = SparkSession.builder \
    .appName("Resolvendo-Rede-Local") \
    .master("local[1]") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "false") \
    .getOrCreate()

try:
    print("\n" + "="*30)
    print("INICIANDO TESTE DE DADOS...")
    print("="*30)
    
    # Criando um DataFrame simples para testar o processamento
    dados = [("Yasmin", "Data Engineering"), ("Status", "Testando Spark")]
    df = spark.createDataFrame(dados, ["Nome", "Materia"])
    
    # O comando .show() é o que costuma dar erro se o worker estiver quebrado
    df.show()
    
    print("\n✅ SUCESSO! O Spark processou os dados no Windows.")
except Exception as e:
    print(f"\n❌ O ERRO PERSISTE:\n{e}")
finally:
    spark.stop()