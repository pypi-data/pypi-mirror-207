import typer
import os
from rich import print
from rich.console import Console
from rich.table import Table


app = typer.Typer()
console = Console()


@app.command()
def ls(f: bool = False, l: int = None):
    """
    ls
    """
    # Get list of all files only in the given directory
    files_list = os.listdir()
    is_files = [os.path.isfile(x) for x in files_list]
    sizes = [os.stat(is_file).st_size if x else -float('inf') for is_file, x in zip(files_list, is_files)]
    data = [x for x in zip(files_list, is_files, sizes)]
    data.sort(key=lambda x: -x[2])

    table = Table("type", "name", "size")

    count = 0
    for n, is_file, s in data:
        if l is not None and count >= l: break
        if f and not is_file: continue

        if not is_file:
            size = ""
        elif s/(1024*1024) > 1024:
            size = str(round(s/(1024**3), 3)) + "GB"
        else:
            size = str(round(s/(1024*1024), 3)) + "MB"
        file_type = "is_file" if is_file else "d"
        # print(is_file'[red]{file_type}[/red] [orange]{n}[/orange] {size}')
        table.add_row(file_type, n, size)
        count+=1
    console.print(table)

@app.command()
def help_me():
    """
    what to help??
    """
    typer.echo("what to help??")
