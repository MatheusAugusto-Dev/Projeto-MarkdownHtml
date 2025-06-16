import os

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
            font-family: 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', 'Apple Color Emoji', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            padding: 40px;
            max-width: 900px;
            margin: auto;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #58a6ff;
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
            color: #d2a8ff;
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
            color: #d2a8ff;
        }
        pre {
            background-color: #161b22;
            color: #f8f8f2;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 14px;
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
            font-family: 'Segoe UI', 'Segoe UI Emoji', 'Noto Color Emoji', 'Apple Color Emoji', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #fff;
            color: #24292e;
            padding: 40px;
            max-width: 900px;
            margin: auto;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #0969da;
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
            color: #8250df;
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
            color: #8250df;
        }
        pre {
            background-color: #f6f8fa;
            color: #24292e;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 14px;
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