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

import logging
import os
import signal  # <--- Importante para o Ctrl+C no Windows
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

console = Console()

# --- Configurações de Ambiente ---
BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

load_dotenv(BASE_DIR / ".env")

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


# --- Handler com Monitor de Arquivos ---
class MonitorFTPHandler(FTPHandler):
    def on_file_received(self, file):
        console.print(
            f" [bold green]✔ Upload concluído:[/] [white]{os.path.basename(file)}[/]"
        )

    def on_file_sent(self, file):
        console.print(
            f" [bold blue]✔ Download concluído:[/] [white]{os.path.basename(file)}[/]"
        )

    def on_incomplete_file_received(self, file):
        if os.path.exists(file):
            os.remove(file)
        console.print(
            f" [bold red]✘ Transferência incompleta removida:[/] {os.path.basename(file)}"
        )


# --- Função para encerrar o programa (Windows Friendly) ---
def signal_handler(sig, frame):
    console.print("\n[bold yellow]👋 Encerrando servidor com segurança...[/]")
    sys.exit(0)


# Registra o handler para o Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


# ----------------------------------------------------------------------
# Inicialização do Servidor
# ----------------------------------------------------------------------
def start_ftp_server():
    os.system("cls" if os.name == "nt" else "clear")

    banner_raw = pyfiglet.figlet_format("PyFTP - Server", font="slant")
    console.print(f"[bold grey37]{banner_raw}[/]")

    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_row(
        "📂 [bold cyan]Diretório de Dados:[/]", f"[white]{PATH_FTP_DATA}[/]"
    )
    info_table.add_row("👤 [bold cyan]Usuário Ativo:[/]", f"[green]{FTP_USER}[/]")
    info_table.add_row("🔐 [bold cyan]Senha:[/]", "[dim italic]******** (protegida)[/]")
    info_table.add_row(
        "🌐 [bold cyan]Interface de Escuta:[/]",
        "[bold yellow]0.0.0.0:2121[/] [dim](Todos IPv4)[/]",
    )
    info_table.add_row("📝 [bold cyan]Arquivo de Log:[/]", f"[dim]{PATH_FTP_LOG}[/]")

    console.print(
        Panel(
            info_table,
            title="[bold white]Configurações do Servidor[/]",
            border_style="bright_blue",
            expand=False,
        )
    )

    console.print(
        "\n[bold green]🚀 Aguardando conexões...[/] [white on red] CTRL+C para parar [/]\n"
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
    authorizer.add_user(FTP_USER, FTP_PASS, PATH_FTP_DATA, perm="elradfmwMT")

    handler = MonitorFTPHandler
    handler.authorizer = authorizer
    handler.banner = "PyFTP-Server Ready."
    handler.passive_ports = range(60000, 60100)

    try:
        server = FTPServer(("0.0.0.0", 2121), handler)
        server.serve_forever()
    except Exception as e:
        console.print(f"\n[bold red]❌ Erro crítico: {e}[/]")


if __name__ == "__main__":
    start_ftp_server()
