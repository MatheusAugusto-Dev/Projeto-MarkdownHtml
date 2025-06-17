# 🐍 Manual Completo de Selenium e Pandas com Python

Este guia cobre o essencial para dominar **Selenium** (automação web) e **Pandas** (manipulação de dados) em Python. Ideal para desenvolvedores, cientistas de dados ou automadores.

---

## 📦 Instalação

```bash
pip install selenium pandas
```

> Para o Selenium funcionar, é necessário baixar o **WebDriver** correspondente ao navegador (Chrome, Firefox etc.) e colocar no PATH ou informar o caminho no código.

---

## 🧠 Parte 1: Selenium – Automação Web

### 🚀 1.1 Iniciando o Navegador

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicializa o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
```

### 📄 1.2 Selecionando Elementos

```python
from selenium.webdriver.common.by import By

# Pelo nome da tag, classe, id etc.
elemento = driver.find_element(By.NAME, "q")
elemento.send_keys("ChatGPT")
elemento.submit()
```

### 🔁 1.3 Esperando elementos aparecerem

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera até 10 segundos por um elemento com ID 'meu_id'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "meu_id"))
)
```

### ⬇️ 1.4 Lidando com botões, links e inputs

```python
driver.find_element(By.ID, "btnLogin").click()
driver.find_element(By.NAME, "usuario").send_keys("admin")
```

### 🧪 1.5 Verificando existência de elementos

```python
from selenium.common.exceptions import NoSuchElementException

def existe_elemento(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
```

### 📸 1.6 Tirando screenshot

```python
driver.save_screenshot("pagina.png")
```

### 🧹 1.7 Fechando o navegador

```python
driver.quit()
```

---

## 📊 Parte 2: Pandas – Manipulação de Dados

### 📁 2.1 Lendo Arquivos

```python
import pandas as pd

# CSV
df = pd.read_csv("arquivo.csv")

# Excel
df = pd.read_excel("planilha.xlsx")
```

### 🧾 2.2 Explorando Dados

```python
print(df.head())      # Primeiras linhas
print(df.shape)       # Linhas e colunas
print(df.columns)     # Nomes das colunas
print(df.info())      # Tipos e nulos
```

### 🧮 2.3 Operações comuns

```python
# Selecionar coluna
df["nome"]

# Filtrar linhas
df[df["idade"] > 30]

# Criar nova coluna
df["imposto"] = df["salario"] * 0.1

# Remover coluna
df.drop("coluna_excluir", axis=1, inplace=True)

# Ordenar
df.sort_values(by="idade", ascending=False)

# Agrupar
df.groupby("departamento")["salario"].mean()
```

### ❌ 2.4 Lidando com dados ausentes

```python
df.isnull().sum()            # Verifica quantos nulos
df.fillna(0)                 # Substitui nulos por 0
df.dropna()                  # Remove linhas com nulo
```

### 💾 2.5 Salvando arquivos

```python
df.to_csv("novo.csv", index=False)
df.to_excel("novo.xlsx", index=False)
```

---

## 🧪 Exemplo real de integração Selenium + Pandas

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://exemplo.com/tabela")

linhas = driver.find_elements(By.TAG_NAME, "tr")
dados = []

for linha in linhas:
    colunas = linha.find_elements(By.TAG_NAME, "td")
    dados.append([col.text for col in colunas])

driver.quit()

df = pd.DataFrame(dados, columns=["Nome", "Idade", "Email"])
df.to_csv("tabela_extraida.csv", index=False)
```

---

## 🛠️ Dicas e Boas Práticas

| Ferramenta | Boas Práticas                          |
|------------|----------------------------------------|
| Selenium   | Sempre use `WebDriverWait`             |
| Pandas     | Verifique dados nulos com frequência   |
| Ambos      | Use `try/except` para erros críticos   |
| Selenium   | Use headless mode para rodar invisível |
| Pandas     | Use `dtypes` otimizados p/ performance |

---

## 🧱 Recursos Extras

- [Documentação oficial Selenium](https://www.selenium.dev/documentation/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Cheat Sheet Pandas (by DataCamp)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [webdriver-manager para ChromeDriver automático](https://pypi.org/project/webdriver-manager/)

---

## ✅ Conclusão

Com o **Selenium**, você pode automatizar sites, preencher formulários, extrair dados e muito mais. Com **Pandas**, você trata esses dados de forma poderosa e prática.

Juntos, formam uma dupla perfeita para projetos de automação com manipulação de dados 🚀

---
