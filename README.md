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
    - README.md -> tutorial de execução e construção;
    - check.py -> funções de classificação das mensagens;
    - main.py -> rotas principais e endpoints;
    - templates/index.html -> interface e comunicação direta;
    - **resposta.json** -> retorno de classificação gerado pela API.
- Classificar mensagens nas seguintes categorias:
    - Possui números? _(True/False)_
    - Possui letras? _(True/False)_
    - Possui pontuação? _(True/False)_
    - Possui mais de um alfabeto? _(True/False)_
    - Possui emojis ou símbolos especiais? _(True/False)_
    - Possui url ou links anexados? _(True/False)_
    - Qual o idioma predominante? _({idioma})_
- Submeter validação e projeto.
## Setup (Rascunho)
Para utilizar a API, o primeiro passo é criar um ambiente virtual e instalar as dependências. Para isso, com python instalado em seu sistema operacional, no terminal, escreva:
`git clone https://github.com/henriquegalva0/avaliacaopraticabackend.git`
Depois que todos os arquivos deste projeto forem gerados, escreva:
`python3 -m venv .venv`
Após seu ambiente virtual ser criado, instale todas as dependências dentro dele, executando:
`.\.venv\Scripts\Activate.ps1 && pip install -r requirements.txt`
## Funcionamento
### Checagem
Para desenvolver a classificação das mensagens, a classe *Classificador*, criada dentro do script **[check.py](check.py)**, executa todas as tarefas de checagem até que todas as possíveis informações sobre a mensagem sejam preenchidas.