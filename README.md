# Prova Backend - Projeto Ultimatum (UFG)
-----
## Missão
### Objetivo
Desenvolver uma API backend simples e funcional para classificar mensagens textuais, acompanhada de um tutorial técnico explicando a solução.
### Contexto
Uma equipe precisa de uma API para classificar mensagens curtas enviadas por usuários em categorias simples.
### Requisitos
- API REST funcional
- Endpoint POST que receba um texto
- Retorno JSON com a categoria atribuída
- Validação básica de entrada
- Código executável localmente
-----
## Solução
### Roadmap
- Elaborar projeto utilizando a biblioteca **Flask** em python (endpoint, json, API) e **HTML** (validação e interface).
- Organizar arquivos em:
    - [README.md](README.md) -> progresso e tutorial de execução;
    - [requirements.txt](requirements.txt) -> frameworks requisitadas para executar projeto;
    - [check.py](check.py) -> funções de classificação das mensagens;
    - [main.py](main.py) -> rotas principais e endpoints;
    - [index.html](templates/index.html) -> interface e comunicação direta com a API;
    - **resposta.json** -> retorno de classificação gerado pela API (só é gerado após a execução).
- Classificar mensagens nas seguintes categorias:
    - Possui números? _(True/False)_
    - Possui letras? _(True/False)_
    - Possui pontuação? _(True/False)_
    - Possui mais de um alfabeto? _(True/False)_
    - Possui emojis ou símbolos especiais? _(True/False)_
    - Possui url ou links anexados? _(True/False)_
    - Qual o idioma predominante? _({idioma})_
- Submeter validação e projeto.
## Funcionamento
### Checagem
Para desenvolver a classificação das mensagens, a classe *Classificador*, criada dentro do script **[check.py](check.py)**, executa todas as tarefas de checagem até que todas as possíveis informações sobre a mensagem sejam preenchidas.
### Interface HTML
Para que a equipe possa submeter a mensagem e obtêr feedback ativo, o script **[index.html](templates/index.html)** desenvolve a conexão da API e do usuário pelo método POST em um formulário.
```
    <form method="POST">
        Mensagem: <input type="text" id="mensagem" name="mensagem"><br>
        <input type="submit" value="Classificar">
    </form>
```
Após isso, para que o usuário saiba o retorno em json, o dicionário gerado pela classe *Classificador* é exposto na própria página em forma de lista por um operador looping "_for_".
```
    {% if classificacao %}
        <h2>Resultado da Classificação:</h2>
        {% for item, classe in classificacao.items() %}
            <li><strong>{{ item }}:</strong> {{ classe }}</li>
        {% endfor %}
    {% endif %}
```
### API Flask
A API funciona somente após a inicialização do objeto **Flask** por "app" juntamente à classe *Classificador* feita previamente em [check.py](check.py).
```
    app = Flask(__name__)
    classificador = Classificador(mensagem='')
```
Em seguida, declara-se a rota principal com o método GET e POST para submissão da mensagem na caixa de input da **Interface HTML**.
```
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':

            mensagem = request.form['mensagem']
            classificador.atualizar_mensagem(mensagem)
            classificacao = classificador.retorno_dicionario()

            return render_template('index.html',classificacao=classificacao)
        else:
            return render_template('index.html')
```
A função principal é composta pela inicialização do classificador com atualização da mensagem toda vez que uma submissão é feita. Além disso, a função _render_template()_ gerencia a conexão do HTML com a própria API.

-----
## Setup (Rascunho)
Para utilizar a API, o primeiro passo é criar um ambiente virtual e instalar as dependências. Para isso, com python instalado em seu sistema operacional, no terminal, escreva:
`git clone https://github.com/henriquegalva0/avaliacaopraticabackend.git`
Depois que todos os arquivos deste projeto forem gerados, escreva:
`python3 -m venv .venv`
Após seu ambiente virtual ser criado, instale todas as dependências dentro dele, executando:
`.\.venv\Scripts\Activate.ps1 && pip install -r requirements.txt`
Por fim, apenas execute o script [main.py](main.py) com:
`python3 main.py`