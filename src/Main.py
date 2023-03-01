"""
Ideias da aplicação:
    1. Os registros serão armazenados em Tuplas.
    2. As Tuplas serão armazenadas em Tabelas.
    3. As Tabelas serão armazenadas em Paginas.
    4. Os Bucket armazenarão Tuplas, i.e. seus 
        registros, junto com um ponteiro para a 
        Tabela da Pagina que a mesma se encontra. (Map)
        Ex:. Bucket 1 -> "Fulano": 1
    5. A Função Hash determinará, dado uma chave
        qualquer, exemplo: "Fulano", em qual Bucket
        ela se encontrando, retornando então seu
        índice.
        Ex:. FHash("Fulano") -> 1 / "Fulano" em Bucket 1.
    6. Depois de obtido o índice do Bucket de uma
        chave qualquer, pegar o ponteiro da Pagina
        registrado com a chave.
        Ex:. FHash("Fulano") -> 1 / "Fulano" em Bucket 1
             Bucket1("Fulano") -> 1 (Ponteiro para a Tabela 1 da Pagina)
    7. Depois de obtido o ponteiro/referência para a Tabela da Pagina,
        Buscar na Tabela da Pagina a chave alvo, e então retornar a Tupla.

    - Tabelas apontam para Tuplas
    - Tuplas apontam entre si (Linked List), será útil para um Table Scan (busca ordenada).
    - Tuplas apontem para o índice das Tabelas nas Paginas (Informação contida/exibida no Bucket).
    - Bucket tem tamanhos fixos (valor calculado).
    - Paginas tem tamanhos fixos (usuário que define).
    - Função Hash deve ter baixa dispersão.
"""

from structs.Tupla import Tupla # pylint: disable=import-error
from structs.Tabela import Tabela # pylint: disable=import-error

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
    # Pega a Tabela com todas as Tuplas registradas.
    tabela: Tabela = read_input(path="input.txt")
    print("T")

if __name__ == "__main__":
    main()
