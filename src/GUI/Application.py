"""Representa um GUI."""

from tkinter.ttk import Style
from tkinter import Tk, PhotoImage

# pylint: disable=import-error

from structs.Pagina import Pagina
from structs.Tabela import Tabela
from structs.Bucket import BucketManager
from GUI.containers.Master import Master

class Application(Tk):
    """Representa uma aplicação.

    Args:
        Tk (Tk): Aplicação top-level.
    """
    # Comprimento e Largura da aplicação.
    width: int
    height: int
    # O tema da aplicação.
    theme: Style
    # Os contêineres da aplicação.
    master_container: Master
    # Variáveis referentes ao funcionamento do índice hash.
    page: Pagina
    table: Tabela
    bucket: BucketManager

    def __init__(self, title: str, table: Tabela, width: int = 800, height: int = 600) -> None:
        super().__init__()
        # Configura as variáveis do índice hash.
        self.table = table
        self.bucket = BucketManager(self.table.get_size())
        self.bucket.insert_data_from_table(self.table)
        # Define o título da aplicação.
        self.title(title)
        # Define a resolução da aplicação.
        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")
        # Desabilita o redimensionamento da aplicação.
        self.resizable(False, False)
        # Define um ícone para a aplicação.
        self.iconphoto(True, PhotoImage(file="src/GUI/assets/icon.png"))
        # Define um tema para a aplicação.
        self.apply_theme("plastik")
        # Configura o contêiner principal da aplicação.
        self.__configure_master_container()
        # Faz a aplicação rodar indefinidamente.
        self.mainloop()

    def apply_theme(self, theme: str) -> None:
        """Define um tema para a aplicação.

        Args:
            theme (str): O tema a ser usado na aplicação.
        """
        self.theme = Style(self)
        self.call("source", f"src/GUI/themes/{theme}/{theme}.tcl")
        self.theme.theme_use(theme)

    def __configure_master_container(self) -> None:
        """Configura o contêiner principal da aplicação."""
        # Configura o grid da aplicação.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Inicializa o contêiner principal.
        self.master_container = Master(self)

        # Desenha o contêiner principal.
        self.master_container.frame_grid(column=0, row=0, padx=0, pady=0)

        # Configura o grid do contêiner principal dentro da aplicação.
        self.master_container.configure_column(column_id=0, weight=1)
        self.master_container.configure_row(row_id=0, weight=0)
        self.master_container.configure_row(row_id=1, weight=1)
        self.master_container.configure_row(row_id=2, weight=0)

        # Renderiza os demais contêineres da aplicação no contêiner principal.
        self.master_container.draw_body(padx=0.01 * self.width, pady=0.01 * self.height)

        # Atualiza as informações no rodapé (Buckets).
        self.master_container.render_to_footer(
            bs=self.bucket.get_bucket_capacity(),
            bc=self.bucket.get_bucket_count()
        )

    def adjust_page(self, new_page_size: int) -> None:
        """Ajusta o tamanho das Páginas.

        Args:
            new_page_size (int): O novo tamanho das Páginas.
        """
        self.page = Pagina(new_page_size)
        self.page.insert(self.table)
        # Exibe na saída a quantidade de páginas criadas e o tamanho fixo.
        self.master_container.render_to_output(
            "1. O tamanho das páginas foi modificado!\n" +
            f"2. Foram criadas '{self.page.get_page_count()}' novas " +
            f"páginas de tamanho '{self.page.get_page_fixed_size()}'!"
        )
        # Deixar os demais contêineres (corpo e rodapé) visíveis.
        self.master_container.unlock_containers(padx=0.01 * self.width, pady=0.01 * self.height)
        # Atualiza o texto do rodapé.
        self.master_container.render_to_footer(
            ps=self.page.get_page_fixed_size(),
            pc=self.page.get_page_count()
        )

    def table_scan(self, key: str, count: int = None) -> None:
        """Lista os 'N' primeiros registros até o registro desejado.

        Args:
            key (str): A chave a ser buscada na tabela.
            count (int, optional): A quantidade de registros a serem
            listados.
            Valor padrão é o tamanho da tabela.
        """
        # Faz o Table Scan nos 'N' primeiros registros.
        tuples_range = self.table.table_scan(key, count)
        if tuples_range:
            self.master_container.render_to_output(
                f"1. O registro com a chave '{key}' foi encontrado!\n" +
                f"2. Estimativa de custo de acesso é de '{tuples_range[-1].get_page_index()}'\n" +
                "3. Listagem das chaves do Table Scan:\n" +
                '\n'.join(f"Chave: '{k.get_data()}'" for k in tuples_range)
            )
        else:
            # Exibe na saída que nenhum registro com determinada chave foi encontrada.
            self.master_container.render_to_output(
                f"1. Nenhum registro com a chave '{key}' foi encontrada."
            )

    def bucket_search(self, key: str) -> None:
        """Procura por uma chave nos Buckets.

        Args:
            key (str): A chave a ser procurada nos buckets.
        """
        # Pega a tupla caso seja encontrada no bucket.
        tuple_from_bucket, bucket_id = self.bucket.search_data(key)
        if tuple_from_bucket:
            # Exibe na saída se a chave foi encontrada e em qual bucket.
            self.master_container.render_to_output(
                f"1. O registro com a chave '{key}' foi encontrado no bucket '{bucket_id}'!\n" +
                f"2. Esse registro pertence a Página '{tuple_from_bucket.get_page_index()}'"
            )
        else:
            # Exibe na saída que nenhuma tupla com determinada chave foi encontrada.
            self.master_container.render_to_output(
                f"1. Nenhum registro com a chave '{key}' foi encontrado nos Buckets."
            )

    def get_bucket_info(self, bucket_id: int) -> None:
        """Retorna as informações de um Bucket.

        Args:
            bucket_id (int): O índice de um Bucket.
        """
        # Pega a taxa de colisões de um bucket.
        collision_count = self.bucket.get_collision_count(bucket_id)
        # Pega a qntd. de overflows de um bucket.
        overflow_count = self.bucket.get_overflow_count(bucket_id)
        # Exibe na saída a taxa de colisão e a quantidade de overflows.
        self.master_container.render_to_output(
            f"1. Informações do bucket de índice '{bucket_id}'\n" +
            f"2. Uma taxa de colisão de '{collision_count}'\n" +
            f"3. Um overflow de '{overflow_count}'"
        )
