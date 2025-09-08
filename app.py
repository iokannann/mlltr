import os
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
             valor_do_input = request.form['meu_input']
             NOME_SECRETO = os.environ.get('NOME_SECRETO', 'ikn')
             if valor_do_input == NOME_SECRETO:
                  return redirect(url_for('secret', nome=valor_do_input))
             else:
                    return redirect(url_for('second', nome=valor_do_input))
        print(f"O usuário digitou: {valor_do_input}")

        return redirect(url_for('index'))
    
@app.route("/secret")
def secret():
    nome = request.args.get('nome')
    return render_template("secret.html", nome=nome)

@app.route("/second")
def second():
    nome = request.args.get('nome')
    return render_template("second.html", nome=nome)

@app.route('/dados')
def ver_dados():
    conn = get_db_connection()
    dados = conn.execute('SELECT * FROM dados').fetchall()
    conn.close()
    return render_template('dados.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)