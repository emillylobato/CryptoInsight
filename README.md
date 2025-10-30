
# CryptoInsight #

Pipeline completo de engenharia de dados para coleta, armazenamento e análise de criptomoedas em tempo real.

## Sobre o Projeto

Sistema que simula um fluxo real de engenharia de dados, consumindo API externa, processando informações e disponibilizando através de API própria e dashboard interativo.

**Moedas monitoradas:** Bitcoin, Ethereum, Cardano, Solana, Binance Coin, Dogecoin

## Tecnologias

- **Python** + **FastAPI** + **Streamlit**
- **SQLite** (banco de dados)
- **Pandas** (processamento)
- **Plotly** (gráficos)
- **CoinGecko API** (fonte de dados publica)

## Como Executar

### Pré-requisitos:
```bash
pip install requests pandas / fastapi / uvicorn / streamlit plotly /

--- Após baixar "todas" as dependencias informadas e com o diretorio de arquivos correto, abra 3 terminais e execute separadamente:

python coletor.py -> coleta os dados a cada 1min e armazena no sqlite 

python api.py -> disponibiliza os dados via Rest

streamlit run dashboard.py -> gera a interface visual com as estmativas

(OBS: a cada 20 registros é feita uma "limpeza", visando manter apenas os registros mais recentes).