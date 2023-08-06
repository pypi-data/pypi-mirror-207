import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    kaizen will help
    """
    typer.echo('kaizen will help you!!')

@app.command()
def hello():
    """
    hello
    """
    typer.echo('hello from kaizen')

@app.command()
def help_me():
    """
    what to help??
    """
    typer.echo("what to help??")
