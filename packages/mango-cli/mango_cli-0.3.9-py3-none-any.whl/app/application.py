import pyfiglet
import click
from .handlers.download_data import download_data

pyfiglet.print_figlet("Mangosoft CLI")

@click.group()
@click.version_option("0.3.9")
@click.pass_context
def cli(ctx):
    pass



@cli.command(help="Download data from a table")
def download():
    download_data()
