"""Representa a estrutura Bucket.
Estrutura responsável pelo mapeamento de
dados de busca em endereços de páginas.
"""

from math import log10
from typing import Dict, List, Union, Any

# pylint: disable=import-error

from structs.Tupla import Tupla
from structs.Tabela import Tabela
from structs.FuncaoHash import FuncaoHash

# FIXME: Testar mais, eu NÃO verifiquei se os Bucket tão armazenando direito.
# FIXME: Ver se os dados ESTÃO SENDO ARMAZENADOS CORRETAMENTE nos Buckets e Overflows.
# FIXME: Ver se a TAXA DE COLISÃO e a QNTD. DE OVERFLOW estão certas.
class Bucket:
    """Representa a estrutura Bucket."""
    # O "Id" do Bucket. (Facilita a contagem de Overflow)
    __id: int
    # As Tuplas armazenadas no Bucket.
    __dados: List[Tupla]
    # Capacidade do Bucket.
    __capacidade_bucket: int
    # Referêcia para o próximo Bucket. (Linked List)
    __proximo_bucket: 'Bucket' = None

    def __init__(self, id_bucket: int, capacidade: int) -> None:
        """Inicializa dados essenciais.

        Args:
            id_bucket (int): O "Id" do Bucket.
            capacidade (int): A capacidade do Bucket.
        """
        self.__id = id_bucket
        self.__dados = []
        self.__capacidade_bucket = capacidade

    def get_bucket_id(self) -> int:
        """Retorna o "Id" do Bucket atual.

        Returns:
            int: O "Id" do Bucket atual.
        """
        return self.__id

    def is_bucket_full(self) -> bool:
        """Verifica se este Bucket está cheio.

        Returns:
            bool: Se o Bucket está cheio ou não.
        """
        return len(self.__dados) == self.__capacidade_bucket

    def get_data_size(self) -> int:
        """Retorna a quantidade de Tuplas armazenadas.

        Returns:
            int: A qntd. de Tuplas armazenadas.
        """
        return len(self.__dados)

    def get_next_bucket(self) -> Union['Bucket', None]:
        """Pega a referência do próximo Bucket (Overflow) caso
        exista, retorna "None" caso contrário.

        Returns:
            Union['Bucket' | None]: Retorna a referência do
            próximo Bucket (Overflow) ou "None" caso contrário.
        """
        return self.__proximo_bucket

    def __create_overflow(self) -> None:
        """Cria um novo Bucket (Overflow) e faz para referência a ele."""
        bucket_overflow: 'Bucket' = Bucket(self.get_bucket_id() + 1, self.__capacidade_bucket)
        self.__proximo_bucket = bucket_overflow

    def __insert_data_into_overflow(self, dado: Tupla) -> None:
        """Insere uma Tupla no próximo Bucket (Overflow).

        Repete os mesmos passos de "self.insert_data()".

        Args:
            dado (Tupla): A Tupla a ser inserida no Bucket (Overflow).
        """
        self.__proximo_bucket.insert_data(dado)

    def insert_data(self, dado: Tupla) -> None:
        """Insere uma Tupla no Bucket, se possível.

        Caso este Bucket esteja cheio, ele procura
        por um Bucket (Overflow) e insere nele, caso não
        existe um Bucket (Overflow) um novo será criado.

        Args:
            dado (Tupla): A Tupla a ser inserida no Bucket.
        """
        if self.is_bucket_full():
            if self.get_next_bucket() is None:
                self.__create_overflow()
            self.__insert_data_into_overflow(dado)
        else:
            self.__dados.append(dado)

    def search_data(self, dado: Any) -> Union[Tupla, None]:
        """Procura por uma determinada Tupla nesse Bucket.

        Args:
            dado (Any): A Tupla a ser procurada.

        Returns:
            Union[Tupla, None]: Retorna a Tupla se a mesma for
            encontrada ou "None" caso contrário.
        """
        for dado_bucket in self.__dados:
            if dado_bucket.get_data() == dado:
                return dado_bucket
        return None


class BucketManager:
    """Responsálve por manipular Buckets."""
    # A quantidade necessária de Buckets para armazenar as Tuplas de uma Tabela.
    __quantidade_buckets: int
    # A capacidade dos Buckets.
    __capacidade_buckets: int
    # O registro de todos os Buckets criados, incluindo os overflows.
    __buckets: Dict[int, Bucket]

    def __init__(self, quantidade_tuplas: int) -> None:
        """Inicializa o Bucket, configurando a quantidade e
        a capacidade de cada Bucket baseado na qntd. de Tuplas.

        Args:
            quantidade_tuplas (int): A qntd. de Tuplas em uma Tabela.
        """
        # Calcula a quantidade de Buckets necessários.
        self.__calculate_bucket_size(quantidade_tuplas)
        # Calcula a capacidade dos Bucket.
        self.__calculate_bucket_capacity(quantidade_tuplas)
        # Inicializa os Buckets.
        self.__init_buckets()

    def insert_data_from_table(self, tabela: Tabela) -> None:
        """Insere TODAS as Tuplas de uma Tabela qualquer.

        Args:
            tabela (Tabela): A Tabela a ser inserido as Tuplas
            nos Buckets.
        """
        if tabela is not None:
            for tupla in tabela.get_tuples():
                self.insert_data(tupla)

    def insert_data(self, dado: Tupla) -> None:
        """Insere uma Tupla em um determinado Bucket,
        o índice do Bucket é definido pela Função Hash.

        Args:
            dado (Tupla): A Tupla a ser inserida no Bucket.
        """
        id_bucket: int = FuncaoHash.hash_function(dado, self.__quantidade_buckets)
        self.get_bucket_by_id(id_bucket).insert_data(dado)

    # FIXME: Tem coisa aqui
    def search_data(self, dado: Tupla | str) -> Union[Union[Tupla, None], int]:
        """Procura por uma Tupla em um Bucket qualquer,
        o Bucket é determinado pela Função Hash.

        Args:
            dado (Tupla | str): A Tupla a ser procurada nos Buckets.

        Returns:
            Union[Union[Tupla, None], int]: Retorna a Tupla se ela
            for encontrada ou 'None' caso contrário e, também o índice
            do bucket em que ela foi encontrada ou '-1' caso contrário.
        """
        id_bucket: int = FuncaoHash.hash_function(dado, self.__quantidade_buckets)
        bucket_alvo: Bucket = self.get_bucket_by_id(id_bucket)
        dado_alvo: Tupla | None = None
        while bucket_alvo is not None:
            dado_alvo = bucket_alvo.search_data(dado)
            if dado_alvo is not None:
                if dado == dado_alvo.get_data():
                    return dado_alvo, id_bucket
            bucket_alvo = bucket_alvo.get_next_bucket()
        return None, -1

    def get_bucket_by_id(self, id_bucket: int) -> Bucket:
        """Retorna um Bucket, procurando-o pelo índice.

        Args:
            id_bucket (int): O índice do Bucket a ser procurado.

        Returns:
            Bucket: Um Bucket em um determinado índice.
        """
        return self.__buckets[id_bucket]

    def get_bucket_count(self) -> int:
        """Retorna a quantidade de Buckets.

        Returns:
            int: A qntd. de Buckets.
        """
        return self.__quantidade_buckets

    def get_bucket_capacity(self) -> int:
        """Retorna a capacidade dos Buckets.

        Returns:
            int: A capacidade dos Buckets.
        """
        return self.__capacidade_buckets

    def get_collision_count(self, id_bucket: int) -> int:
        """Retorna a taxa de colisão de um Bucket.

        Itera sobre todos os Bucket (Overflow) e conta quantas
        Tuplas foram registradas além da capacidade máxima.

        Args:
            id_bucket (int): O índice do Bucket a ser pego
            a taxa de colisão.

        Returns:
            int: A taxa de colisão de um Bucket.
        """
        taxa_colisao: int = 0
        bucket_alvo: Bucket = self.get_bucket_by_id(id_bucket)
        while bucket_alvo.get_next_bucket() is not None:
            bucket_alvo = bucket_alvo.get_next_bucket()
            taxa_colisao += bucket_alvo.get_data_size()
        return taxa_colisao

    def get_overflow_count(self, id_bucket: int) -> int:
        """Retorna a quantidade de overflow de um Bucket.

        Args:
            id_bucket (int): O índice do Bucket a ser pego
            a qntd. de overflow.

        Returns:
            int: A qntd. de overflow de um Bucket.
        """
        quantidade_overflow: int = 0
        bucket_alvo: Bucket = self.get_bucket_by_id(id_bucket)
        while bucket_alvo.get_next_bucket() is not None:
            bucket_alvo = bucket_alvo.get_next_bucket()
            quantidade_overflow = max(quantidade_overflow, bucket_alvo.get_bucket_id())
        return quantidade_overflow

    def __calculate_bucket_size(self, quantidade_tuplas: int) -> None:
        """Calcula a quantidade de Buckets necessários baseado
        na quantidade de Tuplas de uma Tabela.

        Basicamente divide a qntd. de Tuplas por alguma potência
        de 10, em que a potência se dá pela contagem de dígitos
        da qntd. de Tuplas, de uma Tabela, dividido por 2.

        Args:
            quantidade_tuplas (int): A qntd. de Tuplas de uma Tabela.
        """
        quantidade_digitos: int = int(log10(quantidade_tuplas) + 1) // 2
        self.__quantidade_buckets = quantidade_tuplas // pow(10, quantidade_digitos)

    def __calculate_bucket_capacity(self, quantidade_tuplas: int) -> None:
        """Calcula a capacidade dos Buckets.

        Como a qntd. de Buckets é a divisão da qntd. de Tuplas,
        de uma Tabela, por alguma potência de 10, a capacidade
        dos Buckets é simplesmente a divisão entre esses valores.

        Args:
            quantidade_tuplas (int): A qntd. de Tuplas de uma Tabela.
        """
        self.__capacidade_buckets = quantidade_tuplas // self.__quantidade_buckets

    def __init_buckets(self) -> None:
        """Inicializa todos os Buckets."""
        self.__buckets = {
            id_bucket: Bucket(0, self.get_bucket_capacity())
            for id_bucket in range(0, self.get_bucket_count())
        }
