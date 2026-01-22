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