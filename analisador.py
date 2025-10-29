import sqlite3
import pandas as pd

def analisar_dados():
    conn = sqlite3.connect('dados_cripto.db')
    
    #ler dados
    df = pd.read_sql_query("SELECT * FROM precos", conn)
    conn.close()
    
    print("\n" + "="*50)
    print(" Relatório de Análise")
    print("="*50)
    
    #estatiticas por moeda
    for moeda in df['moeda'].unique():
        dados_moeda = df[df['moeda'] == moeda]
        
        print(f"\n {moeda}:")
        print(f"   • Preço atual: U$ {dados_moeda['preco_usd'].iloc[-1]:.2f}")
        print(f"   • Média: U$ {dados_moeda['preco_usd'].mean():.2f}")
        print(f"   • Mínima: U$ {dados_moeda['preco_usd'].min():.2f}")
        print(f"   • Máxima: U$ {dados_moeda['preco_usd'].max():.2f}")
        print(f"   • Volatilidade: ±U$ {dados_moeda['preco_usd'].std():.2f}")
        print(f"   • Total de registros: {len(dados_moeda)}")
    
    print(f"\n Total geral: {len(df)} registros coletados")
    print("="*50)

if __name__ == "__main__":
    analisar_dados()