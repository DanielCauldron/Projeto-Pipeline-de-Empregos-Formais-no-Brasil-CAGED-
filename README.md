# Projeto Pipeline de Empregos Formais no Brasil - CAGED

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para processar dados do CAGED (Cadastro Geral de Empregados e Desempregados) do Brasil, utilizando Python, pandas e SQLite.

## Estrutura do Projeto

```
dados/
    caged.db
    raw/
        caged_abril_2025.xlsx
caged_pipeline/
    etl.py
    extract.py
    load.py
    trasform.py
    requirements .txt
```

## Funcionalidades

- **Extração:** Baixa arquivos de dados do CAGED diretamente do site do governo ([`extract.py`](caged_pipeline/extract.py)).
- **Transformação:** Limpa e organiza os dados, removendo linhas/colunas vazias e preenchendo valores nulos ([`etl.py`](caged_pipeline/etl.py)).
- **Carga:** Salva os dados tratados em um banco de dados SQLite ([`etl.py`](caged_pipeline/etl.py), [`load.py`](caged_pipeline/load.py), [`trasform.py`](caged_pipeline/trasform.py)).

## Como Executar

1. **Instale as dependências:**

   ```
   pip install -r caged_pipeline/requirements\ .txt
   ```

2. **Extraia os dados:**

   Execute o script de extração para baixar o arquivo Excel do CAGED:

   ```
   python caged_pipeline/extract.py
   ```

3. **Execute o pipeline ETL completo:**

   ```
   python caged_pipeline/etl.py
   ```

   Isso irá:
   - Ler o arquivo Excel baixado
   - Limpar e transformar os dados
   - Carregar os dados no banco SQLite (`dados/caged.db`)

## Observações

- Os caminhos dos arquivos estão configurados para rodar no Windows. Ajuste os caminhos se necessário.
- O arquivo Excel de entrada deve estar em `dados/raw/caged_abril_2025.xlsx`.
- O banco de dados SQLite será criado/atualizado em `dados/caged.db`.

## Requisitos

- Python 3.8+
- pandas
- requests
- openpyxl
- sqlalchemy

Veja o arquivo [`requirements .txt`](caged_pipeline/requirements%20.txt) para detalhes.

## Créditos

Desenvolvido para análise de dados do CAGED no Brasil.
