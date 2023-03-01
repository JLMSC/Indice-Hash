"""Representa a estrutura Tupla.
Contém o valor da chave e os dados da linha,
representa uma linha na tabela.
"""

from typing import Any, TypeVar

# TODO: Implementar a classe Tupla.
class Tupla:
    """Representa a estrutura Tupla."""
    # Responsável pelo armazenamento dos registros.
    dado: Any
    # Aponta para o próximo elemento da lista (Linked List).
    proxima_tupla: TypeVar("Tupla")
    # Aponta para o índice da Tabela na Pagina.
    indice_tabela: int

    # TODO: Indice Tabela, alterar o indice da tabela quando a tabela for adicionado à pagina.

    def __init__(self, dado: Any) -> None:
        self.dado = dado
