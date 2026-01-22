import json
import os
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

        dados = []
        if os.path.exists('resposta.json') and os.path.getsize('resposta.json') > 0:
            with open('resposta.json', 'r') as f:
                dados = json.load(f)
        
        dados.append(classificacao)
        
        with open('resposta.json', 'w') as f:
            json.dump(dados, f, indent=4)

        return render_template('index.html',classificacao=classificacao)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)