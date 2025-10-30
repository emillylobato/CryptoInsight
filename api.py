from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI(tittle= "CryptoInsight API")

@app.get("/analytics")
def get_analytics():
    conn = sqlite3.connect ('dados_cripto.db')
    df = pd.read_sql_query("SELECT*FROM precos", conn)
    conn.close()
    analytics = {}
    for moeda in df['moeda'].unique():
        dados_moeda = df[df['moeda'] == moeda]
        analytics[moeda] = {
            "preco_atual": float(dados_moeda['preco_usd'].iloc[-1]),
            "media": float(dados_moeda['preco_usd'].mean()),
            "minima": float(dados_moeda['preco_usd'].min()),
            "maxima": float(dados_moeda['preco_usd'].max()),
            "volatilidade": float(dados_moeda['preco_usd'].std()),
            "registros": len(dados_moeda)
        }
    
    return analytics

@app.get("/")
def home():
    return {"message": "CryptoInsight API - Acesse /analytics"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)    