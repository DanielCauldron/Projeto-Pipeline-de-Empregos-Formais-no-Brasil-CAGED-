# Coleta dos Dados (Extract)

# %% 
import requests
import os 
#%%
def baixar_arquivo(url, destino):# função para baixar o arquivo
    resposta = requests.get(url)
    with open(destino, 'wb') as f:
        f.write(resposta.content)
    print(f"Arquivo salvo em: {destino}")

# %% 
url = "https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/estatisticas-trabalho/caged/4-tabelas.xls"  # Substituir pela URL real
destino = "dados/raw/caged_abril_2025.xlsx"
os.makedirs("dados/raw", exist_ok=True)# Cria o diretório se não existir
baixar_arquivo(url, destino)