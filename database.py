import sqlite3

def criar_banco():
    conn = sqlite3.connect('dados_cripto.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT NOT NULL,
            preco_usd REAL NOT NULL,
            data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("BANCO DE DADOS CRIADO")

if __name__ == "__main__":
    criar_banco()