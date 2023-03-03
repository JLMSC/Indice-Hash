"""Representa a estrutura Bucket.
Estrutura responsável pelo mapeamento de
dados de busca em endereços de páginas.
"""

"""FIXME: Falta Implementar
    [ ] Calcular a quantidade de Buckets.
    [ ] Calcular a capacidade dos Buckets (Mesma capacidade para todos os Buckets).
    [ ] Implementar a estrutura para os Buckets (Linked List?).
    [ ] Contagem de colisões.
    [ ] Criação de overflows.
    [ ] Contagem de overflows.
"""

# TODO: Implementar a classe Bucket.
class Bucket:
    """Representa a estrutura Bucket."""
    # FIXME: Deixar as variáveis privadas.

    # Taxa de colisões em um Bucket, i.e. qntd. de tuplas
    # adicionadas que excedem o limite de tamanho do Bucket.
    colisoes: int
    # Qntd. de Buckets extras criados ao tentar
    # adicionar elementos em um Bucket cheio.
    overflows: int

    # TODO: Calcular esses valores aqui. (Se basear na qntd de Tuplas)
    quantidade_buckets: int
    capacidade_buckets: int

    # FIXME: Arrumar isso aqui, os valores DEVEM ser calculados DURANTE A INICIALIZAÇÃO.
    def __init__(self, quantidade_tuplas: int) -> None:
        # TODO: O cálculo da qntd. de buckets DEVE se basear na qntd. de tuplas
        self.quantidade_buckets = 0
        # TODO: A capacidade dos buckets pode ser fixa??
