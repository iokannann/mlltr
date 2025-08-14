from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        valor_do_input = request.form.get('meu_input')

        print(f"O usuário digitou: {valor_do_input}")

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)