"""Representa o rodapé de uma aplicação"""

from tkinter.font import Font
from tkinter.ttk import Frame, Label

class Footer(Frame):
    """Representa um rodapé para uma aplicação.

    Args:
        Frame (Frame): Rodapé de uma aplicação.
    """
    # O contêiner principal.
    master_container: Frame
    # Fonte usada nos textos do rodapé.
    footer_text_font: Font

    def __init__(self, master: Frame = None) -> None:
        """Inicializa o rodapé em um contêiner.

        Args:
            master (Frame, optional): O contêiner a ser
            referênciada durante a inicialização do
            rodapé.
            Valor padrão 'None'.
        """
        super().__init__(master=master, relief="sunken")
        self.master_container = master
        # Configura as fontes usadas no rodapé.
        self.__configure_footer_fonts()

    def __configure_footer_fonts(self) -> None:
        """Configura as fontes usadas no rodapé."""
        self.footer_text_font = Font(family="Callibri", size=8, weight="normal")

    def frame_grid(self, column: int, row: int, padx: int, pady: int) -> None:
        """Configura o rodapé.

        Args:
            column (int): Índice da coluna do rodapé.
            row (int): Índice da linha do rodapé.
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        self.grid(column=column, row=row, padx=padx, pady=pady, sticky="WE")

    def configure_columns(self, column_id: int, weight: int) -> None:
        """Configura uma coluna do rodapé.

        Args:
            column_id (int): O índice da coluna.
            weight (int): A área da coluna (valor multiplicativo).
        """
        self.grid_columnconfigure(column_id, weight=weight)

    def draw_body(self, padx: int, pady: int) -> None:
        """Renderiza elementos ao rodapé.

        Args:
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        # Texto indicando o tamanho das páginas.
        Label(self, text="Tamanho da Página: -", font=self.footer_text_font)\
            .grid(padx=padx, pady=pady, column=0, row=0, sticky="W")
        # Texto indicando a quantidade das páginas.
        Label(self, text="Qntd. de Páginas: -", font=self.footer_text_font)\
            .grid(padx=padx, pady=pady, column=1, row=0, sticky="W")

        # Texto indicando a porcentagem de dispersão.
        Label(self, text="Porcentagem de Dispersão: -", font=self.footer_text_font)\
            .grid(padx=padx, pady=pady, column=2, row=0, sticky="WE")

        # Texto indicando o tamanho dos buckets.
        Label(self, text="Capacidade dos Buckets: -", font=self.footer_text_font)\
            .grid(padx=padx, pady=pady, column=3, row=0, sticky="E")
        # Texto indicando a quantidade de buckets.
        Label(self, text="Qntd. de Buckets: -", font=self.footer_text_font)\
            .grid(padx=padx, pady=pady, column=4, row=0, sticky="E")

    def update_page_size(self, page_size: int) -> None:
        """Atualiza o texto contendo o tamanho das páginas.

        Args:
            page_size (int): O tamanho da página.
        """
        self.children["!label"].config(text=f"Tamanho da Página: {page_size}")

    def update_page_count(self, page_count: int) -> None:
        """Atualiza o texto contendo a quantidade de páginas.

        Args:
            page_count (int): A quantidade de páginas.
        """
        self.children["!label2"].config(text=f"Qntd. de Páginas: {page_count}")

    def update_dispersion_percentage(self, percentage: float) -> None:
        """Atualiza o texto contendo a porcentagem de dispersão.

        Args:
            percentage (float): A porcentagem de dispersão.
        """
        self.children["!label3"].config(text=f"Porcentagem de Dispersão: {percentage:.2f}%")

    def update_bucket_size(self, bucket_size: int) -> None:
        """Atualiza o texto contendo a capacidade dos buckets.

        Args:
            bucket_size (int): A capacidade dos buckets.
        """
        self.children["!label4"].config(text=f"Capacidade dos Buckets: {bucket_size}")

    def update_bucket_count(self, bucket_count: int) -> None:
        """Atualiza o texto contendo a quantidade de buckets.

        Args:
            bucket_count (int): A quantidade de buckets.
        """
        self.children["!label5"].config(text=f"Qntd. de Buckets: {bucket_count}")
