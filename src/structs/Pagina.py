"""Representa a estrutura Pagina.
Estrutura de dados que representa a divisão
e alocação física da tabela na mídia de armazenamento.
"""

from typing import Dict, List
from structs.Tabela import Tabela # pylint: disable=import-error

# TODO: Implementar a classe Pagina.
class Pagina:
    """Representa a estrutura Pagina."""
    # Tabelas contidas na Pagina.
    tabelas: Dict[int, List[Tabela]] = {}
    # Índice das Paginas, por padrão a primeira é 0.
    indice_tabela_atual: int = 0
    # Tamanho fixo da Pagina.
    tamanho_pagina: int

    # TODO: O TableScan é aqui? ele faz em uma determinada Pagina ou na Tabela toda?

    def __init__(self, tamanho_pagina: int) -> None:
        """Inicializa uma Pagina com tamanho fixo.

        Args:
            tamanho_pagina (int): O tamanho da Pagina.
        """
        # Define o tamanho das Paginas.
        self.tamanho_pagina = tamanho_pagina
        # Inicializa a primeira Pagina.
        self.tabelas[self.indice_tabela_atual] = []

    def insert(self, tabela: Tabela) -> None:
        """Insere todas as Tuplas de uma Tabela
        em Paginas separadas de tamanho fixo, faz,
        também, com que cada Tupla aponte para sua
        respectiva Pagina.

        Args:
            tabela (Tabela): A Tabela a ser obtido
            as tuplas.
        """
        for tupla in tabela.tuplas:
            if len(self.tabelas[self.indice_tabela_atual]) > self.tamanho_pagina:
                self.indice_tabela_atual += 1
                self.tabelas[self.indice_tabela_atual] = []
            tupla.indice_tabela = self.indice_tabela_atual
            self.tabelas[self.indice_tabela_atual].append(tupla)
            