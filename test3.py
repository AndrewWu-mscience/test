# Databricks notebook source
import pandas as pd

# COMMAND ----------

'''some text'''

# COMMAND ----------

'''other text'''

# COMMAND ----------

df = pd.DataFrame(columns=['a', 'b', 'c'])
df['a'], df['b'], df['c'] = range(10), range(10), range(10)
df = spark.createDataFrame(df)
display(df)

# COMMAND ----------

df.rdd.getNumPartitions()