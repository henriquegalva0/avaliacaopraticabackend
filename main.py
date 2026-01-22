from flask import Flask, render_template, request
from check import Classificador

app = Flask(__name__)
classificador = Classificador(mensagem='')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        mensagem = request.form['mensagem']
        classificador.atualizar_mensagem(mensagem)
        classificacao = classificador.retorno_dicionario()

        return render_template('index.html',classificacao=classificacao)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)