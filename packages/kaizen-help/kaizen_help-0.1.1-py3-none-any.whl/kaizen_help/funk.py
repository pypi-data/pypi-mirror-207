import typer
from rich import print

app = typer.Typer()

@app.command()
def fun():
    """
    hello
    """
    print('hello from kaizen :boom: :boom:')

@app.command()
def help_me():
    """
    what to help??
    """
    typer.echo("what to help??")
