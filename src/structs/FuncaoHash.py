"""Representa uma Função Hash.
Mapeia um chave de busca em um endereço Bucket.
"""

# pylint: disable=import-error

from structs.Tupla import Tupla

class FuncaoHash:
    """Representa uma Função Hash."""

    @staticmethod
    def hash_function(dado: Tupla | str, quantidade_buckets: int) -> int:
        """Retorna um índice de algum Bucket.
        A Função Hash utiliza da ideia de índices círculares,
        somando todos os valores Unicode de uma 'chave' e retornando
        o resto da divisão da soma com a a qntd. de buckets.

        Args:
            dado (Tupla | str): Uma Tupla qualquer de uma Tabela.
            quantidade_buckets (int): A qntd. de Buckets.

        Returns:
            int: O índice do Bucket no qual a Tupla pertence.
        """
        chave: str
        if isinstance(dado, Tupla):
            chave = dado.get_data()
        else:
            chave = dado
        return sum(ord(c) for c in chave) % quantidade_buckets
