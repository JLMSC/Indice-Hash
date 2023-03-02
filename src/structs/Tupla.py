"""Representa a estrutura Tupla.
Contém o valor da chave e os dados da linha,
representa uma linha na tabela.
"""

from typing import Any, TypeVar

class Tupla:
    """Representa a estrutura Tupla."""
    # Responsável pelo armazenamento dos registros.
    dado: Any
    # Aponta para o próximo elemento da lista (Linked List).
    proxima_tupla: TypeVar("Tupla") # FIXME: Precisa disso aqui?
    # Aponta para o índice da Tabela na Pagina.
    indice_tabela: int

    def __init__(self, dado: Any) -> None:
        """Cria uma Tupla com um dado qualquer.

        Args:
            dado (Any): O dado a ser armazenado na Tupla.
        """
        self.dado = dado
