"""Representa a estrutura Tabela.
Contém todas as Tuplas construídas a partir do
carregamento de algum arquivo de dados.
"""

from typing import List
from structs.Tupla import Tupla # pylint: disable=import-error

# TODO: Implementar a classe Tabela.
class Tabela:
    """Representa a estrutura Tabela."""
    # Responsável pelo armazenamento das tuplas.
    tuplas: List[Tupla] = []

    # TODO: Remover?
    def __init__(self) -> None:
        pass

    def insert(self, tupla: Tupla) -> None:
        """Insere um novo elemento na Tabela
        e, também, faz com que a Tupla anterior
        aponte para a nova Tupla inserida.

        Args:
            tupla (Tupla): A Tupla a ser registrada
            na Tabela.
        """
        if len(self.tuplas) > 1:
            # FIXME: Realmente precisa disso? Se o TableScan é uma busca ordenada, não faz mais sentido só percorrer a lista?
            self.tuplas[-1].proxima_tupla = tupla
        self.tuplas.append(tupla)
