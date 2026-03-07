# 📂 PyFTP-Server (Portátil)

Um servidor FTP leve, seguro e extremamente fácil de rodar em qualquer sistema (macOS, Linux, Windows), baseado na biblioteca `pyftpdlib` e gerenciado pelo **uv**.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![UV](https://img.shields.io/badge/Managed%20by-UV-purple?logo=python)
![Protocol](https://img.shields.io/badge/Protocol-FTP-orange)

<img width="970" height="504" alt="PyFTP-Server" src="https://github.com/user-attachments/assets/b95afad5-7316-4904-aad3-61310d50d652" />

## ✨ Funcionalidades

* **Portabilidade Total:** Não requer instalação global de bibliotecas. O `uv` resolve tudo.
* **Dual-Stack:** Suporte nativo a IPv4 e IPv6 (escuta em `::2121`).
* **Segurança:** Autenticação via variáveis de ambiente (`.env`).
* **Logs Automáticos:** Registros salvos em `/logs/ftp_server.log` e exibidos no terminal.
* **Auto-configuração:** Cria diretórios de logs e dados automaticamente.

---

## 🛠️ Pré-requisitos

Certifique-se de ter o `uv` instalado:

🍎 **macOS /** 🐧 **Linux:**
```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```
Ou via `pip`:

```bash
pip install uv
```

🪟 **Windows (PowerShell):**

```bash
powershell -c "iwr [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
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
