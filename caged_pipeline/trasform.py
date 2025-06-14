# %%
import pandas as pd
# %%
from sqlalchemy import create_engine 
import os
#%%
def carregar_no_banco(caminho_excel, banco):#função para carregar dados do Excel para o banco de dados SQLite
    df = pd.read_excel(caminho_excel)
    engine = create_engine(f"sqlite:///{banco}")
    df.to_sql("caged_abril_2025", engine, index=False, if_exists="replace")
    print(f"✅ Dados carregados no banco '{banco}' com sucesso!")
carregar_no_banco(r"E:\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED-\dados\raw\caged_abril_2025.xlsx", "dados/caged.db")   

# %%
caminho_arquivo = r"E:\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED-\dados\raw\caged_abril_2025.xlsx"
caminho_banco = "dados/caged.db"

carregar_no_banco(caminho_arquivo, caminho_banco)