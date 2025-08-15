from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_db_connection

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        valor_do_input = request.form.get('meu_input')
        conn = get_db_connection()
        conn.execute('INSERT INTO dados (valor) VALUES (?)', (valor_do_input,))
        conn.commit()
        conn.close()

        print(f"O usuário digitou: {valor_do_input}")

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)