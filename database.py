import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS dados (valor TEXT)')
    conn.commit()
    conn.close()
    print('banco de dados iniciado')

if __name__ == '__main__':
    init_db