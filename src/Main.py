"""Função Principal."""

from tkinter import Tk

# pylint: disable=import-error

from structs.Tupla import Tupla
from structs.Tabela import Tabela
from GUI.Application import Application

def read_input(path: str) -> Tabela:
    """Faz a leitura de dados de um arquivo,
    criando Tuplas e armazenando-as em Tabelas.

    Args:
        path (str): O caminho do arquivo.

    Returns:
        Tabela: A Tabela com todas as Tuplas
        registradas.
    """
    # Cria uma Tabela temporária.
    _tabela: Tabela = Tabela()
    # Lê o arquivo de entrada.
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            # Remove espaços no começo e final da linha.
            line = line.strip()
            # Insere uma nova Tupla na Tabela.
            _tabela.insert(Tupla(dado=line))
    # Retorna a Tabela com todas as Tuplas registradas.
    return _tabela

def main() -> None:
    """Função Principal."""
    # Inicializa a aplicação.
    root = Tk()
    Application(root, read_input("input.txt"))
    root.mainloop()

if __name__ == "__main__":
    main()
