#%%
import duckdb
import pandas as pd
from datetime import datetime

#%%

conn = duckdb.connect(database='dados_duckdb.db', read_only=False)
# %%
path_data= '../landing'
arquivo = 'z0019_2'
data_injestao = datetime.now()
#%%
df = pd.read_csv(f'{path_data}/{arquivo}.csv', sep =";", index_col=None)
df['nome_arquivo'] = arquivo
df['data_injestao'] = data_injestao
df.head()
# %%
conn.execute("""
             CREATE TABLE IF NOT EXISTS bronze_produtos(
             NATBR VARCHAR,
             MAKTX VARCHAR,
             WERKS VARCHAR,
             MAINS VARCHAR,
             LABST VARCHAR,
             nome_arquivo VARCHAR,
             data_ingestao TIMESTAMP
             )
             """)
# %%

conn.execute("INSERT INTO bronze_produtos SELECT * FROM df ")

# %%

resultado = conn.execute("SELECT * FROM bronze_produtos").fetchdf()
resultado.head(10)

# %%
conn.close()
# %%
