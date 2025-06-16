# 🖼️ Markdown to Image Converter (Windows Friendly)

Este projeto converte arquivos Markdown (`.md`) em imagens (`.png`), útil para criar conteúdo visual de posts, tutoriais, slides, documentação ou redes sociais.

Compatível com **Windows** e fácil de configurar com Python.

---

## ✅ Funcionalidades

- 📄 Converte `.md` para `.html`
- 🖼️ Transforma o HTML em imagem (`.png`)
- ⚙️ 100% offline (usando Python + wkhtmltopdf)
- 🎨 Suporte a tabelas, emojis e blocos de código com destaque de sintaxe
- 🔍 Ideal para automação de conteúdo técnico
- 🧼 Limpeza automática do HTML temporário após a conversão

---

## 🚀 Requisitos

- Python 3.x
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

> ⚠️ No Windows, é necessário instalar manualmente o `wkhtmltopdf` e adicionar o executável à variável de ambiente `PATH`.

---

## 📦 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/MatheusAugusto-Dev/markdown-to-image
   cd markdown-to-image
   ```

2. Instale as dependências:
   ```bash
   pip install markdown imgkit
   ```

---

## 🧠 Como funciona

1. O script lê um arquivo Markdown (`Teste.md`)
2. Converte o conteúdo para HTML com suporte a:
   - Blocos de código (`fenced_code`)
   - Destaque de sintaxe (`codehilite`)
   - Tabelas (`tables`)
3. Aplica um template HTML com estilos visuais
4. Gera uma imagem `imagem.png` com qualidade configurável
5. Remove o arquivo `temp.html` após a geração

---

## 🧩 Estrutura do Projeto

```
📁 markdown-to-image/
├── Teste.md               # Arquivo de entrada
├── imagem.png             # Imagem gerada
├── script.py              # Código principal
├── utils.py               # Funções auxiliares
└── README.md              # Este arquivo
```

---

## 🖥️ Exemplo de Execução

```bash
python script.py
```

---

## ⚙️ Opções de Configuração

Você pode customizar a saída modificando o dicionário `options`:

```python
options = {
    'encoding': "UTF-8",
    'quality': '100',
    'width': '1000'
}
```

---

## 🔧 Personalização do Estilo

O estilo do HTML é controlado pela função `retorna_html_completo_md(html_body)` no `utils.py`. Personalize cores, fontes, tabelas, tamanhos de código, emojis, etc.

---

## 📌 Dica de Uso

Use este projeto para:

- Criar banners de conteúdo técnico
- Publicar partes de documentação como imagem
- Compartilhar trechos de código nas redes sociais com bom visual
- Automatizar posts com GitHub Actions (com modificações)

---

## 🧼 Observações

> Certifique-se de que o `wkhtmltoimage` esteja funcional no terminal. Teste com `wkhtmltoimage --version` após a instalação.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## ✨ Contribuições

Pull requests são bem-vindos! Se tiver ideias para melhorias ou novos recursos, fique à vontade para abrir uma issue.

---

## 🤝 Autor

Desenvolvido por Matheus Augusto (https://github.com/MatheusAugusto-Dev)
