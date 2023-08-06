import typer
from kaizen_help import files
from kaizen_help import funk

app = typer.Typer()

app.add_typer(files.app, name="files")
app.add_typer(funk.app, name="funk")
