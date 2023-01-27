import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

destination = 'postgresql://postgres:postgres@localhost:5455/analytics'

conn_string = destination
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

query = "SELECT * FROM racerdata;"
df = pd.read_sql_query(query, conn)
df_max = df.sort_values(by=['views'])
print(df_max)

top10 = df_max.tail(10)
ax = top10.plot.bar(x="titel", y="views", figsize=(12,8), fontsize=14)
plt.show()