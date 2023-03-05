"""Representa a estrutura Tabela.
Contém todas as Tuplas construídas a partir do
carregamento de algum arquivo de dados.
"""

# pylint: disable=import-error

from typing import List, Optional, Union
from structs.Tupla import Tupla

# FIXME: Revisar e testar, principalmente o Table Scan.

class Tabela:
    """Representa a estrutura Tabela."""
    # Responsável pelo armazenamento das tuplas.
    __tuplas: List[Tupla] = []

    def get_size(self) -> int:
        """Retorna a quantidade de Tuplas na
        Tabela.

        Returns:
            int: A qntd. de Tuplas na Tabela
        """
        return len(self.__tuplas)

    def get_tuples(self) -> List[Tupla]:
        """Retorna TODAS as Tuplas armazenadas
        nesta Tabela.

        Returns:
            List[Tupla]: As Tuplas armazenadas
            nesta Tabela.
        """
        return self.__tuplas

    def insert(self, tupla: Tupla) -> None:
        """Insere uma Tupla na Tabela.

        Args:
            tupla (Tupla): A Tupla a ser inserida
            na Tabela.
        """
        self.__tuplas.append(tupla)

    def table_scan(self, dado: str, quantidade_busca: Optional[int] = None) -> Union[Tupla, None]:
        """Realiza uma busca (Table Scan) de um dado.

        Args:
            dado (str): O dado a ser procurado na Tabela.
            quantidade_busca (int, optional): A quantidade de Tuplas
            a serem procuradas na Tabela, caso esse valor seja ultrapassado
            a busca para.
            Valor padrão é o tamanho da Tabela: get_size().

        Returns:
            Union[Tupla, None]: Retorna o dado, caso seja encontrado ou nada.
        """
        # Qntd. de busca será a qntd. de Tuplas se nenhum valor for informado.
        if quantidade_busca is None:
            quantidade_busca = self.get_size()
        # Qntd. inválida. (valores menores que 0 ou maiores que a qntd. de tuplas)
        if 0 > quantidade_busca > self.get_size():
            raise ValueError("Qntd. de busca inválido no Table Scan.")
        # Itera de 0 à N, buscando por 'dado'
        tupla_atual: Tupla | None
        for i in range(0, quantidade_busca, 1):
            tupla_atual = self.__tuplas[i]
            if tupla_atual.get_data() == dado:
                return tupla_atual
        return None

    # TODO: Precisa implementar "remove" ?
