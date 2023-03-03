"""Representa uma Função Hash.
Mapeia um chave de busca em um endereço Bucket.
"""

# FIXME: Revisar e testar (quando o Bucket estiver pronto).

class FuncaoHash:
    """Representa uma Função Hash."""

    @staticmethod
    def hash_function(dado: str, quantidade_buckets: int) -> int:
        """Retorna um índice de algum Bucket.
        A Função Hash utiliza da ideia de índices círculares,
        somando todos os valores Unicode de um 'dado' e retornando
        o resto da divisão da soma com a a qntd. de buckets.

        Args:
            dado (str): Um dado qualquer de uma Tupla.
            quantidade_buckets (int): A qntd. de Buckets.

        Returns:
            int: O índice do Bucket no qual a Tupla pertence.
        """
        return sum(ord(c) for c in dado) % quantidade_buckets
