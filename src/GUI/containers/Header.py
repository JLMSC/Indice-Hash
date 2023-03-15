"""Representa o cabeçalho de uma aplicação."""

from tkinter.font import Font
from tkinter import Button
from tkinter.ttk import Frame, Label, Entry

class Header(Frame):
    """Representa um cabeçalho para uma aplicação.

    Args:
        Frame (Frame): Contêiner de uma aplicação.
    """
    # O contêiner principal.
    master_container: Frame
    # Fontes usadas nos textos do cabeçalho.
    header_text_font: Font
    header_entry_font: Font
    header_button_font: Font

    def __init__(self, master: Frame = None) -> None:
        """Inicializa o cabeçalho em um contêiner.

        Args:
            master (Frame, optional): O contêiner a ser
            referenciado durante a inicialização do
            cabeçalho.
            Valor padrão: 'None'.
        """
        super().__init__(master=master, relief="sunken")
        self.master_container = master
        # Configura as fontes usadas no cabeçalho.
        self.__configure_header_fonts()

    def __configure_header_fonts(self) -> None:
        """Configura as fontes usadas no cabeçalho."""
        self.header_text_font = Font(family="Callibri", size=16, weight="normal")
        self.header_entry_font = Font(family="Callibri", size=12, weight="normal")
        self.header_button_font = Font(family="Callibri", size=12, weight="bold")

    def frame_grid(self, column: int, row: int, padx: int, pady: int) -> None:
        """Configura o cabeçalho.

        Args:
            column (int): Índice da coluna do cabeçalho.
            row (int): Índice da linha do cabeçalho.
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        self.grid(column=column, row=row, padx=padx, pady=pady, sticky="WE")

    def configure_column(self, column_id: int, weight: int) -> None:
        """Configura uma coluna do cabeçalho.

        Args:
            column_id (int): O índice da coluna.
            weight (int): A área da coluna (valor multiplicativo).
        """
        self.grid_columnconfigure(column_id, weight=weight)

    def draw_body(self, padx: int, pady: int) -> None:
        """Renderiza elementos ao cabeçalho.

        Args:
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        # Texto indicando o tamanho da página.
        Label(self, text="Tamanho da Página", font=self.header_text_font)\
            .grid(padx=padx, pady=pady, column=0, row=0, sticky="W")
        # Campo de entrada para o tamanho da página.
        Entry(self, font=self.header_entry_font)\
            .grid(padx=padx, pady=pady, column=1, row=0, sticky="NSWE")
        # Botão para reajuste de tamanho da página.
        Button(self, text="Ajustar Página", font=self.header_button_font,
               command=self.__grab_page_entries)\
            .grid(padx=padx, pady=pady, column=0, row=1, sticky="W")

    def __grab_page_entries(self) -> None:
        """Pega os valores inseridos nos campos de entrada."""
        # Campos de entradas requeridos.
        size_entry = self.children["!entry"]
        # Extrai o tamanho da página.
        page_size: str = size_entry.get()

        # Valida a entrada.
        if len(page_size) > 0:
            # Verifica se possui somente digitos.
            if page_size.isdigit():
                # Chama a função para ajusta da página.
                self.master_container.app.adjust_page(int(page_size))
        # Limpa o campo de entrada.
        size_entry.delete(0, "end")
