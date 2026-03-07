# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyftpdlib",
#     "python-dotenv",
#     "pyfiglet",
#     "rich",
#     "setuptools",
# ]
# ///

"""
PyFTP-Server Professional
Servidor FTP portátil com interface Rich, caminhos absolutos e gerenciamento por UV.
"""

import logging
import os
import sys
from pathlib import Path

import pyfiglet
from dotenv import load_dotenv
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Instância do Console Rich
console = Console()

# ----------------------------------------------------------------------
# Configuração de Caminhos e Ambiente
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

ENV_FILE = BASE_DIR / ".env"
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    console.print(f"[yellow]⚠️  Aviso: Arquivo .env não encontrado em {BASE_DIR}[/]")

FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")

raw_path_data = os.getenv("PATH_FTP_DATA", "ftp_data")
PATH_FTP_DATA = (
    str(Path(raw_path_data).expanduser().resolve())
    if os.path.isabs(raw_path_data)
    else str((BASE_DIR / raw_path_data).resolve())
)
PATH_FTP_LOG = str((LOGS_DIR / "ftp_server.log").resolve())

Path(PATH_FTP_DATA).mkdir(parents=True, exist_ok=True)

if not FTP_USER or not FTP_PASS:
    console.print("[bold red]❌ Erro: FTP_USER ou FTP_PASS não definidos no .env[/]")
    sys.exit(1)


# ----------------------------------------------------------------------
# Inicialização do Servidor
# ----------------------------------------------------------------------
def start_ftp_server():
    # Limpa o terminal
    os.system("cls" if os.name == "nt" else "clear")

    # 1. Banner estilizado com Pyfiglet em DARK_GRAY (Cinza Escuro) via Rich
    banner_raw = pyfiglet.figlet_format("PyFTP-Server", font="slant")
    # Usamos o Rich para aplicar a cor "grey37" que equivale ao Dark Gray
    console.print(f"[bold grey37]{banner_raw}[/]")

    # 2. Tabela de Informações
    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_row(
        "📂 [bold cyan]Diretório de Dados:[/]", f"[white]{PATH_FTP_DATA}[/]"
    )
    info_table.add_row("👤 [bold cyan]Usuário (Default):[/]", f"[green]{FTP_USER}[/]")
    info_table.add_row("🔐 [bold cyan]Senha (Default):[/]", f"[green]{FTP_PASS}[/]")
    info_table.add_row(
        "🌐 [bold cyan]Endereço Local:[/]", "[bold yellow][::]:2121 (IPv4/IPv6)[/]"
    )
    info_table.add_row("📝 [bold cyan]Arquivo de Log:[/]", f"[dim]{PATH_FTP_LOG}[/]")

    # 3. Exibe o Painel
    console.print(
        Panel(
            info_table,
            title="[bold white]Configurações do Servidor[/]",
            border_style="bright_blue",
            expand=False,
        )
    )

    console.print(
        "\n[bold green]🚀 Servidor em execução...[/] [white on red] CTRL+C para parar [/]\n"
    )

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(PATH_FTP_LOG, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )

    authorizer = DummyAuthorizer()
    authorizer.add_user(
        FTP_USER,
        FTP_PASS,
        PATH_FTP_DATA,
        perm="elradfmwMT",
        msg_login="Login bem-sucedido!",
        msg_quit="Até logo!",
    )

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "PyFTP-Server Ready."

    try:
        server = FTPServer(("0.0.0.0", 2121), handler)
        server.serve_forever()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]👋 Encerrando servidor FTP...[/]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Falha crítica: {e}[/]")


if __name__ == "__main__":
    start_ftp_server()
