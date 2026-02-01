import typer

from .searchbooru import searchbooru

app = typer.Typer()
app.command()(searchbooru)

if __name__ == "__main__":
    app()