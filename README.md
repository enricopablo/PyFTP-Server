# 📂 PyFTP-Server (Portátil)

Um servidor FTP leve, seguro e extremamente fácil de rodar em qualquer sistema (macOS, Linux, Windows), baseado na biblioteca `pyftpdlib` e gerenciado pelo **uv**.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![UV](https://img.shields.io/badge/Managed%20by-UV-purple?logo=python)
![Protocol](https://img.shields.io/badge/Protocol-FTP-orange)

<img width="1130" height="545" alt="PyFTP-Server-Print" src="https://github.com/user-attachments/assets/e6cc8c64-a2c6-4cd8-858e-3e836dfa9e37" />

## ✨ Funcionalidades

* **Portabilidade Total:** Não requer instalação global de bibliotecas. O `uv` resolve tudo.
* **Conectividade:** Suporte nativo a IPv4 (escuta na porta `:2121`).
* **Segurança:** Autenticação via variáveis de ambiente (`.env`).
* **Logs Automáticos:** Registros salvos em `/logs/ftp_server.log` e exibidos no terminal.
* **Auto-configuração:** Cria diretórios de logs e dados automaticamente.

---

## 🛠️ Pré-requisitos

Certifique-se de ter o `uv` instalado:

🍎 **macOS /** 🐧 **Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh \| sh
```
Ou via `pip`:

```bash
pip install uv
```

🪟 **Windows (PowerShell):**

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"
```

Ou via `pip`:

```bash
pip install uv
```

## 📝 Configuração do Ambiente
Crie um arquivo `.env` na raiz do projeto:

```bash
FTP_USER=usuario_ftp
FTP_PASS=senha_ftp
```

## 🚀 Como Executar
Basta rodar o script com o `uv`:

```bash
uv run main.py
```

## ⚡ Configurando o Atalho (pyftp)

Para rodar de qualquer lugar do terminal apenas digitando `pyftp`:

🍎 macOS e 🐧 Linux (Zsh/Bash)
Adicione ao seu `~/.zshrc` ou `~/.bashrc`:

```bash
alias pyftp='uv run /CAMINHO/COMPLETO/PARA/main.py'
```

🪟 Windows (PowerShell)
Adicione ao seu `$PROFILE`:

1. Abra o terminal do `PowerShell` e force um novo `$PROFILE`:
```bash
New-Item $PROFILE -Force
```

2. Ainda no temrinal do `PowerShell` digite:
```bash
notepad $PROFILE
```
3. No aquivo que for aberto crie o `alias`:
```bash
function pyftp { uv run "C:\CAMINHO\PARA\main.py" @args }
```

## 📂 Estrutura de Pastas

```bash
PyFTP-Server/
├── main.py          # Script principal
├── .env.example     # Modelo de configuração
├── logs/            # Histórico de conexões (gerado automaticamente)
└── ftp_data/        # Pasta padrão de arquivos (gerada automaticamente)
```

## 📝 Licença
>Desenvolvido para uso pessoal e profissional em fluxos DevOps.

---

<p align="center">Obviamente feito com 🤖, engenhosidade humana 🤷🏻‍♂️ e uma quantidade suspeita de tokens 🔥.</p>

<p align="center">Obviously made with 🤖, human ingenuity 🤷🏻‍♂️, and a suspicious amount of tokens 🔥.</p>
