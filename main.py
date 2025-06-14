import markdown
import imgkit

#* Carrega o markdown e converte para HTML
with open("Teste.md", "r", encoding="utf-8") as f:
    texto_md = f.read()

html_body = markdown.markdown(texto_md, extensions=["fenced_code", "codehilite"])

html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            padding: 40px;
            max-width: 900px;
            margin: auto;
            line-height: 1.6;
        }}

        h1, h2, h3 {{
            color: #58a6ff;
        }}

        p {{
            margin-bottom: 16px;
        }}

        ul, ol {{
            padding-left: 20px;
            margin-bottom: 16px;
        }}

        a {{
            color: #58a6ff;
        }}

        code {{
            background-color: #161b22;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
            color: #d2a8ff;
        }}

        pre {{
            background-color: #161b22;
            color: #f8f8f2;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 14px;
        }}

        blockquote {{
            border-left: 4px solid #30363d;
            padding-left: 16px;
            color: #8b949e;
            font-style: italic;
            background-color: #161b22;
        }}

        hr {{
            border: none;
            border-top: 1px solid #30363d;
            margin: 24px 0;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""

#* Salva temporariamente como HTML
with open("temp.html", "w", encoding="utf-8") as f:
    f.write(html)

options = {
    'encoding': "UTF-8",
    'quality': '100',
    'width': '800'
}
imgkit.from_file('temp.html', 'imagem.png', options=options)
