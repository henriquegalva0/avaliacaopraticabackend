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
import re
from langdetect import detect

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