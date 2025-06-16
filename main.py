import markdown
import imgkit
from utils import *

#* Carrega o markdown e converte para HTML
with open("Teste.md", "r", encoding="utf-8") as f:
    texto_md = f.read()

#* Conversão com suporte a código e tabelas
html_body = markdown.markdown(texto_md, extensions=["fenced_code", "codehilite", "tables"])

#* Variavel para escolher o tema
opc_tema = int(input("Escolha o tema para o README:\n1 - Light\n2 - Dark\nOpção: "))

#* HTML com estilo e suporte a emojis e tabelas
html = retorna_html_completo_md(html_body, 'light' if opc_tema == 1 else 'dark')

#* Salva temporariamente como HTML
with open("temp.html", "w", encoding="utf-8") as f:
    f.write(html)

#* Opções para gerar a imagem
options = {
    'encoding': "UTF-8",
    'quality': '100',
    'width': '1000'
}

#* Converte HTML para imagem
imgkit.from_file('temp.html', 'imagem.png', options=options)

#* Apaga o arquivo temporário
apaga_arquivo('temp.html')
