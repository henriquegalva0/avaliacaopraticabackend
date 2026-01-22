"""
Classificações-alvo do projeto

- Possui números? _(True/False)_
- Possui letras? _(True/False)_
- Possui pontuação? _(True/False)_
- Possui mais de um alfabeto? _(True/False)_
- Possui emojis ou símbolos especiais? _(True/False)_
- Possui url ou links anexados? _(True/False)_
- Qual o idioma predominante? _({idioma})_
"""

import string
import unicodedata
import emoji

mensagem_teste="Olá Usuário123, tudo bem com você 😄😁?"
nova_mensagem_teste="oi"


class Classificador():
    def __init__(self,mensagem):
        self.mensagem = mensagem
        pass

    def atualizar_mensagem(self,nova_mensagem):
        self.mensagem = nova_mensagem

    def checar_numeros(self):
        return any(char.isdigit() for char in self.mensagem)
    def checar_letras(self):
        return any(char.isalpha() for char in self.mensagem)
    def checar_pontuacao(self):
        return any(char in string.punctuation for char in self.mensagem)
    def checar_emoji(self):
        return emoji.emoji_count(self.mensagem) > 0
    
    def retorno_dicionario(self):
        return {
            'numeros':self.checar_emoji(),
            'letras':self.checar_letras(),
            'pontuacao':self.checar_pontuacao(),
            'emojis':self.checar_emoji()
        }

classificador = Classificador(mensagem_teste)
print(classificador.retorno_dicionario())

classificador.atualizar_mensagem(nova_mensagem_teste)
print(classificador.retorno_dicionario())