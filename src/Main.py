"""
Ideias da aplicação:
    [X] Os registros serão armazenados em Tuplas.
    [X] As Tuplas serão armazenadas em Tabelas.
    [X] As Tabelas serão armazenadas em Paginas.
    [X] TableScan !
    [ ] Os Bucket armazenarão Tuplas, i.e. seus
        registros, junto com um ponteiro para a
        Tabela (índice) da Pagina que a mesma se encontra. (Map)
        Ex:. Bucket 1 -> "Fulano": 1 (Índice da Pagina)
        ! O armazenamento nas Bucket deve ser feito, também,
        pela Função Hash.
    [X] A Função Hash determinará, dado uma chave
        qualquer, exemplo: "Fulano", em qual Bucket
        ela se encontrando, retornando então seu
        índice.
        Ex:. FHash("Fulano") -> 1 / "Fulano" em Bucket 1.
    [ ] Depois de obtido o índice do Bucket de uma
        chave qualquer, pegar o ponteiro da Pagina
        registrado com a chave.
        Ex:. FHash("Fulano") -> 1 / "Fulano" em Bucket 1
             Bucket1("Fulano") -> 1 (Ponteiro para a Tabela 1 da Pagina)
    [ ] Depois de obtido o ponteiro/referência para a Tabela (índice) da Pagina,
        Buscar na Tabela da Pagina a chave alvo, e então retornar a Tupla.
    [ ] Interface Gráfica!!!! (Biblioteca tkinter)

    - Tabelas apontam para Tuplas
    - Tuplas apontam entre si (Linked List), será útil para um Table Scan (busca ordenada).
    - Tuplas apontam para o índice das Tabelas nas Paginas (Informação contida/exibida no Bucket).
    - Bucket tem tamanhos fixos (valor calculado pela Função Hash).
    - Paginas tem tamanhos fixos (usuário que define).
    - Função Hash deve ter baixa dispersão.
"""

# pylint: disable=import-error

from structs.Tupla import Tupla
from structs.Tabela import Tabela
from structs.Pagina import Pagina
from structs.Bucket import Bucket

def read_input(path: str) -> Tabela:
    """Faz a leitura de dados de um arquivo,
    criando Tuplas e armazenando-as em Tabelas.

    Args:
        path (str): O caminho do arquivo.

    Returns:
        Tabela: A Tabela com todas as Tuplas
        registradas.
    """
    # Cria uma Tabela temporária.
    _tabela: Tabela = Tabela()
    # Lê o arquivo de entrada.
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            # Remove espaços no começo e final da linha.
            line = line.strip()
            # Insere uma nova Tupla na Tabela.
            _tabela.insert(Tupla(dado=line))
    # Retorna a Tabela com todas as Tuplas registradas.
    return _tabela

# FIXME: Não esquecer da INTERFACE GRÁFICA!!!

def main() -> None:
    """Função Principal."""
    # FIXME: Tabela, Tupla, Bucket, Pagina DEVEM ser variáveis globais (Facilitar o acesso na interface gráfica).

    # FIXME: TODAS AS ESTRUTURAS DEVEM TER AS VARIÁVEIS PRIVADAS.

    # FIXME: Usar o método hash_function de FuncaoHash quando for fazer uma busca/inserção nos Buckets.

    # FIXME: Tamanho da Pagina DEVE ser passado DURANTE A INSTANCIAÇÃO DE PAGINA.

    # Pega a Tabela com todas as Tuplas registradas.
    tabela: Tabela = read_input(path="input.txt")

    # Divide as Tuplas da Tabela em Paginas de tamanhos fixos.
    pagina: Pagina = Pagina(tamanho_pagina=100)
    pagina.insert(tabela)

    # # TODO: Exemplo de uma Table Scan (sem limite)
    # result = tabela.table_scan("house")
    # print(result)
    # # TODO: Exemplo de uma Table Scan (com limite)
    # result = tabela.table_scan("house", 31_415)
    # print(result)

    # TODO: Tem que fazer o Bucket ainda.
    # bucket: Bucket = Bucket(len(tabela.get_size()))
    print("T")

if __name__ == "__main__":
    main()
