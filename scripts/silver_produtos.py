#%% 
import duckdb

#%%
conn = duckdb.connect(database='dados_duckdb.db',read_only=False)

#%%
df = conn.execute("""
    WITH bronze_produtos AS (
             SELECT *, ROW_NUMBER() OVER (PARTITION BY NATBR ORDER BY data_ingestao DESC) AS row
             FROM bronze_produtos
             WHERE data_ingestao >= '2025-11-25'
)
    SELECT * FROM bronze_produtos WHERE row = 1;
""").fetchdf()

df.head()

#%%
df_final = df.drop(columns=['nome_arquivo', 'data_ingestao', 'row'])

df_final.head()
#%%
df_final = df_final.rename(
    columns={
        "NATBR":"id",
        "MAKTX":"nome_produto",
        "WERKS": "id_categoria",
        "MAINS":"id_fornecedor",
        "LABST":"preco_produto"
        }
    
)

df_final.head()

#%%

df2 = df_final

df2 = df2.astype(
    {
        "id": int,
        "nome_produto": str,
        "id_categoria": str,
        "id_fornecedor": int,
        "preco_produto": float
    }
)

df2.dtypes

#%%

conn.execute("""
    CREATE OR REPLACE TABLE silver_produtos (
             id BIGINT,
             nome_produto TEXT,
             id_categoria TEXT,
             id_fornecedor BIGINT,
             preco_produto FLOAT
)
""")
#%%

conn.execute("INSERT INTO silver_produtos SELECT * FROM df2")

# %%
resultado = conn.execute("SELECT * FROM silver_produtos;").fetchdf()

resultado.head(6)
# %%
