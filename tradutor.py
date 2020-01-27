from os import chdir
from pathlib import Path
import re

import click


@click.group()
def main():
    pass


@main.command('bin')
@click.argument('binario', type=click.STRING)
def binario(binario):
    """
    Transforma um texto em ascii para binário.
    Use aspas no seu texto, exemplo: tradutor.py bin 'ola mundo' ou
    python3 tradutor.py bin 'ola mundo'.
    """
    texto = ", ".join((format(bin(ord(a))[2:], '>08') for a in binario))
    click.echo(f'\nbin: {texto}\n')


@main.command('ascii')
@click.argument('ascii', type=click.STRING)
def texto(ascii):
    """
    Transforma um texto em binário para ascii.
    Use aspas no seu texto, exemplo: tradutor.py ascii '01101111 01101100' ou
    python3 tradutor.py ascii '01101111 01101100'.
    """
    ascii = re.findall(r'\d+', ascii, re.M)
    click.echo(f'\nascii: {"".join((chr(int(a, 2)) for a in ascii))}\n')


if __name__ == '__main__':
    local_deste_arquivo = Path(__file__).parent
    chdir(local_deste_arquivo)
    main()
