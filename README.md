# 🏭 Pipeline ETL — Empregos Formais no Brasil (CAGED)

## 🧾 Descrição do Projeto

Pipeline ETL completo para processamento de dados do **CAGED** (Cadastro Geral de Empregados e Desempregados), fonte oficial do governo brasileiro sobre movimentação do mercado de trabalho formal.

O projeto automatiza a extração direta do site do governo, transformação e carga dos dados em banco relacional — seguindo as etapas reais de um pipeline de dados em produção.

---

## 📈 Por que o CAGED importa

O CAGED é a principal fonte de dados sobre emprego formal no Brasil, publicada mensalmente pelo Ministério do Trabalho. Analisar esses dados permite identificar tendências de contratação, setores em expansão e regiões com maior movimentação no mercado de trabalho.

---

## ⚙️ Arquitetura do Pipeline

```
Fonte: Site do Governo (CAGED)
    ↓ extract.py — download do arquivo Excel
    ↓ transform.py — limpeza, padronização e tratamento de nulos
    ↓ load.py — carga no banco SQLite
Destino: dados/caged.db
```

---

## 📂 Estrutura do Repositório

```
📁 dados/
   ├── caged.db
   └── raw/
       └── caged_abril_2025.xlsx
📁 caged_pipeline/
   ├── etl.py
   ├── extract.py
   ├── transform.py
   ├── load.py
   └── requirements.txt
README.md
```

---

## 🔧 Tecnologias Utilizadas

- **Python 3.8+** — Linguagem principal
- **pandas** — Transformação e limpeza dos dados
- **requests** — Extração direta da fonte oficial
- **openpyxl** — Leitura dos arquivos Excel do governo
- **SQLAlchemy + SQLite** — Armazenamento dos dados tratados

---

## 🚀 Como Executar

**1. Instale as dependências:**
```bash
pip install -r caged_pipeline/requirements.txt
```

**2. Extraia os dados do governo:**
```bash
python caged_pipeline/extract.py
```

**3. Execute o pipeline completo:**
```bash
python caged_pipeline/etl.py
```

O pipeline irá:
- Ler o arquivo Excel baixado da fonte oficial
- Limpar e padronizar os dados (remoção de nulos, tipagem, organização)
- Carregar os dados tratados no banco SQLite (`dados/caged.db`)

---

## 📌 Observações

- Os caminhos estão configurados para Windows — ajuste separadores se rodar em Linux/Mac
- O arquivo de entrada deve estar em `dados/raw/caged_abril_2025.xlsx`
- O banco será criado automaticamente em `dados/caged.db` na primeira execução

---

## 👨‍💻 Autor

**Daniel Caldeirão**
[LinkedIn](https://www.linkedin.com/in/daniel-cauldron/) • [GitHub](https://github.com/DanielCauldron)
