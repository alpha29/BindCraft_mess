import os
import typer

from bindcraft import __version__

app = typer.Typer()

BINDCRAFT_HOME = os.getenv("BINDCRAFT_HOME", os.getcwd())

@app.command()
def run():
    typer.echo("Running...")
    typer.echo("Done.")

@app.command()
def version():
    """
    Show the version and exit.
    """
    typer.echo(f"bindcraft {__version__}")


def main():
    app()
