import requests
import sqlite3

def coletar_dados():
    # Buscar dados da API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    resposta = requests.get(url)
    dados = resposta.json()
    
    # Conectar ao banco
    conn = sqlite3.connect('dados_cripto.db')
    cursor = conn.cursor()
    
    # Inserir dados
    for moeda, info in dados.items():
        cursor.execute(
            "INSERT INTO precos (moeda, preco_usd) VALUES (?, ?)",
            (moeda.capitalize(), info['usd'])
        )
        print(f"✅ {moeda}: U$ {info['usd']}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    coletar_dados()