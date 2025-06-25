import shutil
import markdown
import imgkit
import os
from utils import *
from weasyprint import HTML
from credenciais import *

while True:
#*Menu
    print("Escolha qual arquivo MD voce deseja transformar em Imagem e PDF:")
    print("Digite a opcao numerica correspondente ao arquivo desejado!!!")
    arquivos_md_para_gerar = lista_arquivos_md_gerar(CAMINHO_PASTAS['pasta_md_para_gerar'])
    for i, nome_arquivo in enumerate(arquivos_md_para_gerar):
        print(f"{i} - {nome_arquivo}")

    #* Captura o nome do arquivo selecionado para o usuario
    opcao_usr = int(input("Digite a opção desejada: "))
    nome_arquivo_md_selecionado = arquivos_md_para_gerar[opcao_usr]
    nome_arquivo_md_selecionado_sem_extensao = nome_arquivo_md_selecionado.split(".")[0]

    #* Defini a string de caminho completa do arquivo
    caminho_pasta_arquivo_md_gerar = os.path.join(CAMINHO_PASTAS['pasta_md_para_gerar'], nome_arquivo_md_selecionado)

    #* Carrega o markdown e converte para HTML
    with open(caminho_pasta_arquivo_md_gerar, "r", encoding="utf-8") as f:
        texto_md = f.read()

    #* Conversão com suporte a código e tabelas
    html_body = markdown.markdown(texto_md, extensions=["fenced_code", "codehilite", "tables"])

    #* Variavel para escolher o tema
    opc_tema = int(input("Escolha o tema para o README:\n1 - Light\n2 - Dark\nOpção: "))

    #* HTML com estilo e suporte a emojis e tabelas
    html = retorna_html_completo_md(html_body, 'light' if opc_tema == 1 else 'dark')

    #* Salva temporariamente como HTML
    with open(f"{nome_arquivo_md_selecionado_sem_extensao}.html", "w", encoding="utf-8") as f:
        f.write(html)

    #* Opções para gerar a imagem
    options = {
        'encoding': "UTF-8",
        'quality': '100',
        'width': '1000'
    }

    #* Converte HTML para imagem
    imgkit.from_file(f"{nome_arquivo_md_selecionado_sem_extensao}.html", f"{nome_arquivo_md_selecionado_sem_extensao}.png", options=options)

    #*Converte HTML para PDF
    HTML(string=html).write_pdf(f"{nome_arquivo_md_selecionado_sem_extensao}.pdf")

    #* Apaga o arquivo temporário
    apaga_arquivo(f"{nome_arquivo_md_selecionado_sem_extensao}.html")

    #* Move arquivos gerados para a pasta de destino dos md
    shutil.move(caminho_pasta_arquivo_md_gerar, CAMINHO_PASTAS['pasta_md_gerados'])
    shutil.move(f"{nome_arquivo_md_selecionado_sem_extensao}.pdf", CAMINHO_PASTAS['pasta_md_gerados'])
    shutil.move(f"{nome_arquivo_md_selecionado_sem_extensao}.png", CAMINHO_PASTAS['pasta_md_gerados'])

    opc_continuar_programa = int(input("Deseja continuar? (1 - Sim, 2 - Não): "))
    if opc_continuar_programa == 2:
        break

print("Codigo executado com sucesso!\n\n\n\n\n")
