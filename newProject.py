from rich.prompt import Prompt, Confirm
from rich import print

print("[bold red]alert![/bold red] Something happened")

name = Prompt.ask("Enter your name")
name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
like_hockey = Confirm.ask("Do you like hockey?")