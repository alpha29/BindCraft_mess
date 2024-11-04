import os
from pathlib import Path

import typer

from bindcraft import __version__
from bindcraft.io import download_af_params as dafp
from bindcraft.runner import main as bc_main
from bindcraft.runner import set_up_pyrosetta

app = typer.Typer()

BINDCRAFT_HOME = os.getenv("BINDCRAFT_HOME", os.getcwd())
PARAMS_DIR = Path(BINDCRAFT_HOME) / "params"


@app.command()
def setup_pyrosetta():
    """
    Set up pyrosetta.
    """
    typer.echo("Setting up pyrosetta...")
    set_up_pyrosetta()
    typer.echo("Done.")


@app.command()
def download_af_params(params_dir: str = PARAMS_DIR):
    """
    Download and extract Alphafold params.
    """
    typer.echo("Downloading and extracting...")
    dafp(params_dir=params_dir)
    typer.echo("Done.")


@app.command()
def run():
    """
    Run bindcraft-based binder design.
    """
    typer.echo("Running...")
    bc_main()
    typer.echo("Done.")


@app.command()
def version():
    """
    Show the version and exit.
    """
    typer.echo(f"bindcraft {__version__}")


def main():
    app()
