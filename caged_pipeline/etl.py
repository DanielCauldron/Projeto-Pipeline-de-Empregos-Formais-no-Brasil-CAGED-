# %%
import pandas as pd
# %%
from sqlalchemy import create_engine
# %%
def extrair(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo, engine='openpyxl')
        print(f"✅ Extração concluída! Linhas: {len(df)}")
        return df
    except Exception as e:
        print(f"❌ Erro ao ler o Excel: {e}")
        raise

# %%
def transformar(df):
    """Limpa e organiza os dados."""
    df = df.dropna(how='all')          # Remove linhas vazias
    df = df.dropna(axis=1, how='all')  # Remove colunas vazias
    df = df.fillna(0)                  # Preenche valores nulos com zero
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()  # Remove espaços extras em texto
    print(f"✅ Transformação concluída! Linhas: {len(df)}")
    return df
# %%
def carregar(df, caminho_banco):
    """Salva o DataFrame limpo em uma tabela no banco SQLite."""
    engine = create_engine(f"sqlite:///{caminho_banco}")
    df.to_sql("caged_abril_2025", engine, index=False, if_exists="replace")
    print(f"✅ Dados carregados no banco: {caminho_banco}")
# %%
if __name__ == "__main__":
    caminho_excel = r"E:\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED-\dados\raw\caged_abril_2025.xlsx"  # Ajuste o caminho se precisar
    caminho_banco = r"E:\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED\Projeto-Pipeline-de-Empregos-Formais-no-Brasil-CAGED-\dados\caged.db"
    
    df_bruto = extrair(caminho_excel)
    df_limpo = transformar(df_bruto)
    carregar(df_limpo, caminho_banco)

