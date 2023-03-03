"""Representa a estrutura Tupla.
Contém o valor da chave e os dados da linha,
representa uma linha na tabela.
"""

from typing import Any

# FIXME: Revisar e testar.

class Tupla:
    """Representa a estrutura Tupla."""
    # Responsável pelo armazenamento dos registros.
    __dado: str
    # Aponta para o índice da Tabela na Pagina.
    __indice_pagina: int

    def __init__(self, dado: Any) -> None:
        """Cria uma Tupla com um dado qualquer.

        Args:
            dado (Any): O dado a ser armazenado na Tupla.
        """
        self.__dado = str(dado)

    def get_data(self) -> str:
        """Retorna o dado contido em uma Tupla.

        Returns:
            str: O dado contido na Tupla.
        """
        return self.__dado

    def get_page_index(self) -> int:
        """Retorna o índice da Pagina associada
        nesta Tupla.

        Returns:
            int: O índice da Pagina associada a
            esta Tupla.
        """
        return self.__indice_pagina

    def set_page_index(self, indice_pagina: int) -> None:
        """Define a referência ao índice de uma Pagina.

        Args:
            indice_pagina (int): O índice de uma Pagina.
        """
        self.__indice_pagina = indice_pagina

    # TODO: Precisa implementar "set/update_data" ?
