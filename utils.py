import os

def lista_arquivos_md_gerar(caminho_pasta):
    arquivos_md_para_gerar = os.listdir(caminho_pasta)
    return arquivos_md_para_gerar

def apaga_arquivo(caminho_arquivo):
    """
    Função para apagar um arquivo específico.
    """
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("Arquivo deletado com sucesso.")
    else:
        print("Arquivo não encontrado.")

def retorna_html_completo_md(html_body, theme='dark'):
    dark_css = """
         body {
            font-family: 'Segoe UI Emoji', 'Segoe UI', Arial, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            padding: 40px;
            margin: 0;
            line-height: 1.6;
        }
        h1, h2, h3, h4, h5 {
            color: #0969da;
            font-family: 'Segoe UI Emoji', 'Segoe UI', Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #30363d;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #161b22;
            color: #167A1E;
        }
        td {
            background-color: #0d1117;
        }
        p {
            margin-bottom: 16px;
        }
        ul, ol {
            padding-left: 20px;
            margin-bottom: 16px;
        }
        a {
            color: #58a6ff;
        }
        code {
            background-color: #161b22;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
            color: #167A1E;
        }
        pre {
            background-color: #161b22;
            color: #f8f8f2;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 14px;
        }
        pre, code {
            white-space: pre-wrap;   /* Permite quebras dentro de blocos de código */
            word-break: break-all;   /* Quebra palavras longas/sequências */
            overflow-wrap: break-word;
        }
        blockquote {
            border-left: 4px solid #30363d;
            padding-left: 16px;
            color: #8b949e;
            font-style: italic;
            background-color: #161b22;
        }
        hr {
            border: none;
            border-top: 1px solid #30363d;
            margin: 24px 0;
        }
    """

    light_css = """
         body {
            font-family: 'Segoe UI Emoji', 'Segoe UI', Arial, sans-serif;
            background-color: #fff;
            color: #24292e;
            padding: 40px;
            /* Remova max-width */
            margin: 0; /* Remova ou zere o margin */
            line-height: 1.6;
        }
        h1, h2, h3, h4, h5 {
            color: #054288;
            font-family: 'Segoe UI Emoji', 'Segoe UI', Arial, sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #d0d7de;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f6f8fa;
            color: #167A1E;
        }
        td {
            background-color: #fff;
        }
        p {
            margin-bottom: 16px;
        }
        ul, ol {
            padding-left: 20px;
            margin-bottom: 16px;
        }
        a {
            color: #0969da;
        }

        code {
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
            color: #167A1E;
        }
        pre {
            background-color: #f6f8fa;
            color: #24292e;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 14px;
        }
        pre, code {
            white-space: pre-wrap;   /* Permite quebras dentro de blocos de código */
            word-break: break-all;   /* Quebra palavras longas/sequências */
            overflow-wrap: break-word;
        }
        blockquote {
            border-left: 4px solid #d0d7de;
            padding-left: 16px;
            color: #57606a;
            font-style: italic;
            background-color: #f6f8fa;
        }
        hr {
            border: none;
            border-top: 1px solid #d0d7de;
            margin: 24px 0;
        }
    """

    css = dark_css if theme == 'dark' else light_css

    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
        {css}
        </style>
    </head>
    <body>
    {html_body}
    </body>
    </html>"""
    return html
