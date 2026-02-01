import requests
from bs4 import BeautifulSoup
import typer
from typing_extensions import Annotated

def searchbooru(
    tags: Annotated[str, typer.Argument(help="Tags to search. Each tag should be separated by commas.")] == ""
):
    print(test)