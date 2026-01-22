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
```
class Classificador():
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def atualizar_mensagem(self, nova_mensagem):
        self.mensagem = nova_mensagem

    def checar_numeros(self):
        return any(char.isdigit() for char in self.mensagem)

    def checar_letras(self):
        return any(char.isalpha() for char in self.mensagem)

    def checar_pontuacao(self):
        return any(char in string.punctuation for char in self.mensagem)

    def checar_emoji(self):
        return emoji.emoji_count(self.mensagem) > 0

    def checar_alfabetos(self):
        scripts = {unicodedata.name(c).split()[0] for c in self.mensagem if c.isalpha()}
        return len(scripts) > 1

    def checar_links(self):
        regex = r'(https?://\S+|www\.\S+)'
        return bool(re.search(regex, self.mensagem))

    def detectar_idioma(self):
        try:
            return detect(self.mensagem)
        except:
            return "indeterminado"

    def retorno_dicionario(self):
        return {
            'numeros': self.checar_numeros(),
            'letras': self.checar_letras(),
            'pontuacao': self.checar_pontuacao(),
            'multiplos_alfabetos': self.checar_alfabetos(),
            'emojis': self.checar_emoji(),
            'links': self.checar_links(),
            'idioma': self.detectar_idioma(),
        }
```
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
#### Criar JSON
Dentro de [check.py](check.py), na função de rota, há um pequeno código que será responsável pela completa transformação do dicionário previamente feito em JSON.
```
    dados = []
    if os.path.exists('resposta.json') and os.path.getsize('resposta.json') > 0:
        with open('resposta.json', 'r') as f:
            dados = json.load(f)
    
    dados.append(classificacao)
    
    with open('resposta.json', 'w') as f:
        json.dump(dados, f, indent=4)
```
O primeiro passo é procurar o arquivo **resposta.json** que, caso não esteja presente, será criado e carregado com a lista _dados_ - desenvolvida para que a biblioteca json possa enviar os dados para o arquivo.

-----
## Setup
Para utilizar a API, o primeiro passo é criar um ambiente virtual e instalar as dependências. Para isso, com python instalado em seu sistema operacional, no terminal, escreva:
```
git clone https://github.com/henriquegalva0/avaliacaopraticabackend.git
cd avaliacaopraticabackend
```
Depois que todos os arquivos deste projeto forem gerados, escreva:
```
python -m venv .venv
```
Após seu ambiente virtual ser criado, instale todas as dependências dentro dele, executando:
- Windows
```
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
```
- Linux
```
    source .venv/bin/activate && pip install -r requirements.txt
```
Por fim, apenas execute o script [main.py](main.py) com:
```
python main.py
```
## Sobre as Bibliotecas
Para esclarecer a necessidade de cada biblioteca, esta seção explica cada uma delas.

### string

Utilizada para ter acesso à constante punctuation, que contém um conjunto de caracteres de pontuação pré-definidos (como !, ?, ., etc.), permitindo verificar se a mensagem contém esses símbolos.

### unicodedata

Utilizada para identificar a origem técnica de cada caractere. No código, a função unicodedata.name() é usada para extrair o "nome" do caractere no padrão Unicode e identificar a qual alfabeto (script) ele pertence, permitindo detectar se há mais de um alfabeto presente (ex: Latim e Grego).

### emoji

Fornece ferramentas para manipular e analisar caracteres de emoji. No projeto, é utilizada a função emoji_count() para contar quantos emojis existem na mensagem e retornar se ela possui ou não esses símbolos.

### re (Regular Expressions)

Biblioteca de Expressões Regulares do Python. É utilizada para definir um padrão de busca (regex) que identifica estruturas de URLs e links (como http:// ou www.) dentro do texto da mensagem.

### langdetect

Utilizada para identificar automaticamente em qual idioma um texto foi escrito. A função detect() analisa a frequência e o padrão das palavras para retornar o código do idioma predominante (ex: 'pt', 'en').

### json

Responsável por manipular arquivos no formato JSON. No código, ela é usada para converter os resultados da classificação (dicionários Python) em texto formatado para salvar no arquivo resposta.json (json.dump) e também para ler dados existentes (json.load).

### os

Utilizada para interagir com o sistema operacional. No projeto, serve para verificar se o arquivo resposta.json já existe no computador (os.path.exists) e se ele possui conteúdo (os.path.getsize) antes de tentar ler os dados.

### flask

- Flask: O micro-framework usado para criar a aplicação web e gerenciar as rotas.
- render_template: Função que carrega e exibe o arquivo HTML (index.html) para o usuário, permitindo enviar variáveis do Python para a página.
- request: Objeto que captura os dados enviados pelo usuário através do formulário (o método POST), permitindo que o servidor receba a mensagem digitada.
