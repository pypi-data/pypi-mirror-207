import requests
import rich
import rich_click as click
from rich.panel import Panel

url = "https://tinkoff.dan.tatar"


@click.group()
def cli():
    pass


@cli.command()
@click.argument('word')
def term(word):
    """Get term definition"""
    response = requests.get(url + "/term/" + word)
    console = rich.get_console()
    if response.status_code == 404:
        console.print("[bold]Not found[/bold]")
        return
    r = response.json()
    console.print(Panel(r["result"]["definition"], title=r["result"]["key"]))


@cli.command()
@click.argument('text')
def detect_slang(text):
    """Detect slang in text"""
    payload = {"text": text}
    response = requests.post(url + "/detect_slang", json=payload)
    words = text.split()
    highlight_words_indexes = map(lambda x: x.split("_")[0], response.json()["result"]["highlight"].keys())
    for word_index in highlight_words_indexes:
        words[int(word_index)] = f"[yellow]{words[int(word_index)]}[/yellow]"

    text = " ".join(words)
    console = rich.get_console()
    console.print(Panel(text, title="Биржевой Сленг"))


@cli.command()
def ping():
    """Ping the server"""
    response = requests.get(url + "/")
    click.echo(response.json())
