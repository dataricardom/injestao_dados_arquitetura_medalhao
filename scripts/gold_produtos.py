#%%

import duckdb
# %%
conn= duckdb.connect(database="dados_duckdb.db", read_only=False)
# %%

df = conn.execute("SELECT * FROM silver_produtos;").fetchdf()

df.head()
# %%

df2 = df.drop(columns=["id_categoria", "id_fornecedor"])

df2.head()

#%%

conn.execute("""
        CREATE TABLE IF NOT EXISTS dim_produtos (
            id_produto BIGINT,
            nome_produto TEXT,
            preco_produto FLOAT
    )
""")
#%%

conn.execute("INSERT INTO dim_produtos SELECT * FROM df2")
#%%

df_dim_produtos = conn.execute("SELECT * FROM dim_produtos;").fetchdf()

df_dim_produtos.head()

#%%
conn.close()
# %%
