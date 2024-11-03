import os
import typer

from bindcraft import __version__
from bindcraft.runner import main, set_up_pyrosetta

app = typer.Typer()

BINDCRAFT_HOME = os.getenv("BINDCRAFT_HOME", os.getcwd())

@app.command()
def setup_pyrosetta():
    """
    Set up pyrosetta.
    """
    typer.echo("Setting up pyrosetta...")
    set_up_pyrosetta()
    typer.echo("Done.")


@app.command()
def run():
    """
    Run bindcraft-based binder design.
    """
    typer.echo("Running...")
    main()
    typer.echo("Done.")

@app.command()
def version():
    """
    Show the version and exit.
    """
    typer.echo(f"bindcraft {__version__}")


def main():
    app()
