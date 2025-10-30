import requests
import sqlite3
import time

def coletar_dados():
    #buscar dados da API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano,solana,binancecoin,dogecoin&vs_currencies=usd"
    resposta = requests.get(url)
    dados = resposta.json()
    
    #conectar ao banco
    conn = sqlite3.connect('dados_cripto.db')
    cursor = conn.cursor()
    
    #inserir dados
    for moeda, info in dados.items():
        cursor.execute(
            "INSERT INTO precos (moeda, preco_usd) VALUES (?, ?)",
            (moeda.capitalize(), info['usd'])
        )
        print(f"✅ {moeda}: U$ {info['usd']}")
    
    #manter  so os ultimos 20 regstros
    cursor.execute ("DELETE FROM pecos WHERE id NOT IN (SELECT id FROM precos ORDER BY id DESC LIMIT 20)")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    while True:
        coletar_dados()
        print("Aguardando 1 minuto...")
        time.sleep(60)  #60 segundos = 1min

