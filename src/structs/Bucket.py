# TODO: Implementar a classe Bucket.
class Bucket:
    """Representa a estrutura Bucket."""
    # FIXME: Arrumar isso aqui (removi o commit sem querer.)
    # Taxa de colisões em um Bucket, i.e. qntd. de tuplas
    # adicionadas que excedem o limite de tamanho do Bucket.
    colisoes: int
    # Qntd. de Buckets extras criados ao tentar
    # adicionar elementos em um Bucket cheio.
    overflows: int

    def __init__(self) -> None:
        pass

    # TODO: O insert só pode ser implementado depois que a Função Hash estiver pronta.
