"""Representa a estrutura Pagina.
Estrutura de dados que representa a divisão
e alocação física da tabela na mídia de armazenamento.
"""

# pylint: disable=import-error

from typing import Dict, List
from structs.Tupla import Tupla
from structs.Tabela import Tabela

# FIXME: Revisar e testar.

class Pagina:
    """Representa a estrutura Pagina."""
    # Tabelas contidas na Pagina.
    __paginas: Dict[int, List[Tupla]] = {}
    # Índice das Paginas, por padrão a primeira é 0.
    __indice_pagina_atual: int = 0
    # Tamanho fixo da Pagina.
    __tamanho_pagina: int

    def __init__(self, tamanho_pagina: int) -> None:
        """Inicializa uma Pagina com tamanho fixo.

        Args:
            tamanho_pagina (int): O tamanho da Pagina.
        """
        # Define o tamanho das Paginas.
        self.__tamanho_pagina = tamanho_pagina
        # Inicializa a primeira Pagina.
        self.__paginas[self.__indice_pagina_atual] = []

    def get_page_fixed_size(self) -> int:
        """Retorna o tamanho fixo das Paginas.

        Returns:
            int: O tamanho fixo das Paginas.
        """
        return self.__tamanho_pagina

    def get_page_size(self, indice_pagina: int) -> int:
        """Retorna a quantidade de Tuplas em uma Pagina.

        Args:
            indice_pagina (int): O índice da Pagina.

        Returns:
            int: A qntd. de Tuplas na Pagina.
        """
        return len(self.__paginas[indice_pagina])

    def get_page_by_index(self, indice_pagina: int) -> List[Tupla]:
        """Busca uma Pagina pelo seu índice e retorna-a.

        Args:
            indice_pagina (int): O índice da Pagina.

        Returns:
            List[Tupla]: O conteúdo (Tuplas) na Pagina.
        """
        return self.__paginas[indice_pagina]

    def insert(self, tabela: Tabela) -> None:
        """Insere todas as Tuplas de uma Tabela
        em Paginas separadas de tamanho fixo, faz,
        também, com que cada Tupla aponte para sua
        respectiva Pagina.

        Args:
            tabela (Tabela): A Tabela a ser obtido
            as tuplas para inserção nas Paginas.
        """
        for tupla in tabela.get_tuples():
            # Passa para a próxima Pagina.
            if len(self.__paginas[self.__indice_pagina_atual]) > self.get_page_fixed_size():
                self.__indice_pagina_atual += 1
                self.__paginas[self.__indice_pagina_atual] = []
            # Adiciona uma Tupla à Pagina atual.
            tupla.set_page_index(self.__indice_pagina_atual)
            self.__paginas[self.__indice_pagina_atual].append(tupla)

    # TODO: Precisa implementar "search" e "remove" ?
            