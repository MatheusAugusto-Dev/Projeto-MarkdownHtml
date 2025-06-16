# 🐧 Manual Básico de Comandos do Linux (CMD)

Este manual contém os **comandos essenciais do terminal Linux**, com exemplos práticos e anotações úteis para uso diário. Ideal para desenvolvedores, administradores de sistema ou entusiastas de Linux.

---

## 📁 Navegação entre diretórios

| Comando | Descrição |
|--------|-----------|
| `pwd` | Mostra o caminho do diretório atual. |
| `ls` | Lista os arquivos e pastas no diretório atual. |
| `ls -la` | Lista tudo, incluindo arquivos ocultos e permissões. |
| `cd nome_da_pasta` | Entra em um diretório. |
| `cd ..` | Volta um nível no diretório. |
| `cd /` | Vai para o diretório raiz. |
| `cd ~` | Vai para o diretório pessoal do usuário. |

---

## 📦 Gerenciamento de arquivos

| Comando | Descrição |
|--------|-----------|
| `touch arquivo.txt` | Cria um novo arquivo vazio. |
| `mkdir pasta` | Cria uma nova pasta. |
| `rm arquivo.txt` | Remove um arquivo. ⚠️ Sem aviso. |
| `rm -rf pasta` | Remove pasta e conteúdo recursivamente. ⚠️ PERIGOSO! |
| `cp arquivo destino/` | Copia arquivo para outro diretório. |
| `mv arquivo destino/` | Move ou renomeia arquivos. |
| `cat arquivo.txt` | Mostra conteúdo de arquivos pequenos. |
| `less arquivo.txt` | Lê arquivos longos de forma interativa. |

---

## 🔍 Pesquisa e busca

| Comando | Descrição |
|--------|-----------|
| `find . -name "*.txt"` | Busca por arquivos .txt no diretório atual e subpastas. |
| `grep "termo" arquivo.txt` | Busca por um termo dentro de um arquivo. |
| `grep -rnw . -e "palavra"` | Busca recursivamente com número da linha. |

---

## 🔧 Permissões e execução

| Comando | Descrição |
|--------|-----------|
| `chmod +x script.sh` | Dá permissão de execução a um script. |
| `chmod 755 arquivo` | Define permissões (proprietário rwx, grupo rx, outros rx). |
| `chown usuario:grupo arquivo` | Muda o dono de um arquivo. |

---

## 🌐 Rede

| Comando | Descrição |
|--------|-----------|
| `ping google.com` | Testa conexão com um host. |
| `ifconfig` ou `ip a` | Mostra interfaces de rede. |
| `curl https://site.com` | Requisição HTTP simples. |
| `wget https://site.com/arquivo` | Baixa arquivos da internet. |

---

## 📂 Compactação e descompactação

| Comando | Descrição |
|--------|-----------|
| `tar -czvf arquivo.tar.gz pasta/` | Compacta pasta em tar.gz. |
| `tar -xzvf arquivo.tar.gz` | Descompacta tar.gz. |
| `zip -r arquivo.zip pasta/` | Compacta em ZIP. |
| `unzip arquivo.zip` | Extrai um arquivo ZIP. |

---

## 🧠 Sistema e processos

| Comando | Descrição |
|--------|-----------|
| `top` | Mostra processos em tempo real. |
| `htop` | Versão melhorada do `top` (precisa instalar). |
| `ps aux` | Lista todos os processos. |
| `kill PID` | Finaliza processo pelo ID. |
| `df -h` | Mostra uso do disco. |
| `du -sh pasta/` | Tamanho total de uma pasta. |
| `free -h` | Mostra uso de memória RAM. |
| `uptime` | Mostra há quanto tempo o sistema está ligado. |

---

## 📦 Gerenciamento de pacotes

### Debian/Ubuntu:

```bash
sudo apt update
sudo apt upgrade
sudo apt install nome-do-pacote
sudo apt remove nome-do-pacote
```

### Arch Linux:

```bash
sudo pacman -Syu
sudo pacman -S nome-do-pacote
sudo pacman -R nome-do-pacote
```

---

## 🔐 Usuários e sudo

| Comando | Descrição |
|--------|-----------|
| `sudo comando` | Executa com privilégios de administrador. |
| `su` | Troca para o superusuário. |
| `adduser nome` | Cria novo usuário. |
| `passwd nome` | Altera senha do usuário. |

---

## 💡 Extras úteis

| Comando | Descrição |
|--------|-----------|
| `history` | Lista histórico de comandos. |
| `!!` | Executa o último comando novamente. |
| `alias gs='git status'` | Cria atalhos de comando. |
| `echo "Texto"` | Imprime na tela. |
| `man comando` | Abre o manual do comando. |

---

## ⚠️ Comandos perigosos (use com extrema cautela)

| Comando | O que faz |
|--------|-----------|
| `rm -rf /` | Apaga TODO o sistema (NUNCA USE!). |
| `:(){ :|:& };:` | Cria fork bomb, trava o sistema. |
| `mkfs.ext4 /dev/sdX` | Formata um disco inteiro. |

---

## 📚 Dica final

Para aprender mais:
```bash
man nome-do-comando
```
Use o manual! Ele é seu melhor amigo no terminal.

---

> 🧠 *Dominar o terminal é como ganhar superpoderes no mundo Linux. Use com sabedoria!*

