import pyfiglet
import click
from .handlers.download_data import download_data
import pathlib


with open("VERSION", "r") as fh:
    version = fh.read()

pyfiglet.print_figlet("Mangosoft CLI")

@click.group()
@click.version_option(version)
@click.pass_context
def cli(ctx):
    pass



@cli.command(help="Download data from a table")
def download():
    download_data()
