"""Representa o corpo de uma aplicação"""

from tkinter.font import Font
from tkinter import Button, Text, Scrollbar
from tkinter.ttk import Frame, Label, Entry

class Body(Frame):
    """Representa um corpo para uma aplicação.

    Args:
        Frame (Frame): Contêiner de uma aplicação.
    """
    # O contêiner principal.
    master_container: Frame
    # Fontes usadas nos textos do corpo.
    body_text_font: Font
    body_entry_font: Font
    body_button_font: Font
    body_output_font: Font

    def __init__(self, master: Frame = None) -> None:
        """Inicializa o corpo em um contêiner.

        Args:
            master (Frame, optional): O contêiner a ser
            referenciada durante a inicialização do
            corpo.
            Valor padrão 'None'.
        """
        super().__init__(master=master, relief="sunken")
        self.master_container = master
        # Configura as fontes usadas no corpo.
        self.__configure_body_fonts()

    def __configure_body_fonts(self) -> None:
        """Configura as fontes usadas no corpo."""
        self.body_text_font = Font(family="Callibri", size=16, weight="normal")
        self.body_entry_font = Font(family="Callibri", size=12, weight="normal")
        self.body_button_font = Font(family="Callibri", size=12, weight="bold")
        self.body_output_font = Font(family="Callibri", size=12, weight="normal")

    def frame_grid(self, column: int, row: int, padx: int, pady: int) -> None:
        """Configura o corpo.

        Args:
            column (int): Índice da coluna do corpo.
            row (int): Índice da linha do corpo.
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        self.grid(column=column, row=row, padx=padx, pady=pady, sticky="WE")

    def configure_column(self, column_id: int, weight: int) -> None:
        """Configura uma coluna do corpo.

        Args:
            column_id (int): O índice da coluna.
            weight (int): A área da coluna (valor multiplicativo).
        """
        self.grid_columnconfigure(column_id, weight=weight)

    def configure_row(self, row_id: int, weight: int) -> None:
        """Configura uma linha do corpo.

        Args:
            row_id (int): O índice da linha.
            weight (int): A área da linha (valor multiplicativo).
        """
        self.grid_rowconfigure(row_id, weight=weight)

    def draw_body(self, padx: int, pady: int) -> None:
        """Renderiza elementos ao corpo.

        Args:
            padx (int): Margem no eixo X, para ambos os lados.
            pady (int): Margem no eixo Y, para ambos os lados.
        """
        # Texto indicando a chave de busca.
        Label(self, text="Chave", font=self.body_text_font)\
            .grid(padx=padx, pady=pady, column=0, row=0, sticky="W")
        # Campo de entrada para a chave de busca.
        Entry(self, font=self.body_entry_font)\
            .grid(padx=padx, pady=pady, column=1, row=0, sticky="NSWE")
        # Texto indicando a quantidade do Table Scan.
        Label(self, text="Quantidade Table Scan", font=self.body_text_font)\
            .grid(padx=padx, pady=pady, column=0, row=1, sticky="W")
        # Campo de entrada para a quantidade do Table Scan
        Entry(self, font=self.body_entry_font)\
            .grid(padx=padx, pady=pady, column=1, row=1, sticky="NSWE")
        # Botão para Table Scan.
        Button(self, text="Table Scan", font=self.body_button_font,
               command=self.__grab_table_scan_entries)\
            .grid(padx=padx, pady=pady, column=0, row=2, sticky="W")
        # Botão para pesquisar (Buckets).
        Button(self, text="Pesquisar nos Buckets", font=self.body_button_font,
               command=self.__grab_bucket_search_entries)\
            .grid(padx=padx, pady=pady, column=1, row=2, sticky="W")

        # Texto indicando o índice do Bucket.
        Label(self, text="Índice do Bucket", font=self.body_text_font)\
            .grid(padx=padx, pady=pady, column=0, row=3, sticky="W")
        # Campo de entrada para a chave de busca.
        Entry(self, font=self.body_entry_font)\
            .grid(padx=padx, pady=pady, column=1, row=3, sticky="NSWE")
        # Botão para ver as informações do Bucket.
        Button(self, text="Ver informações sobre o Bucket", font=self.body_button_font,
               command=self.__grab_bucket_info_entries)\
            .grid(padx=padx, pady=pady, column=0, row=4, sticky="W")

        # Scrollbar da saída de texto.
        text_scrollbar = Scrollbar(self)
        text_scrollbar.grid(row=5, column=2, padx=(0 ,10), pady=(5, 0), sticky="NS")
        # Saída de texto.
        Text(self, font=self.body_output_font, yscrollcommand=text_scrollbar.set)\
            .grid(padx=padx, pady=pady, column=0, row=5, columnspan=2, sticky="NSWE")
        text_scrollbar.config(command=self.children["!text"].yview)

    def get_output(self) -> Text:
        """Retorna o campo de saída deste contêiner.

        Returns:
            Text: O objeto referente ao campo de saída.
        """
        return self.children["!text"]

    def __grab_table_scan_entries(self) -> None:
        """Pega os valores inseridos nos campos de entrada."""
        # Campos de entradas requeridos.
        key_entry = self.children["!entry"]
        count_entry = self.children["!entry2"]
        # Extrai a chave de busca.
        key_to_search: str = key_entry.get()
        # Extrai a quantidade Table Scan.
        key_count: str = count_entry.get()

        # Valida as entradas.
        if len(key_to_search) > 0:
            # Chama a função para busca nas tabelas.           
            self.master_container.app.table_scan(
                key_to_search,
                int(key_count) if key_count.isdigit() else None
            )
        # Limpa os campos de entrada.
        key_entry.delete(0, "end")
        count_entry.delete(0, "end")

    def __grab_bucket_search_entries(self) -> None:
        """Pega os valores inseridos nos campos de entrada."""
        # Campos de entradas requeridos.
        key_entry = self.children["!entry"]
        # Extrai a chave de busca.
        key_to_search: str = key_entry.get()

        # Valida a entrada.
        if len(key_to_search) > 0:
            # Chama a função para busca nos buckets.
            self.master_container.app.bucket_search(key_to_search)
        # Limpa o campo de entrada.
        key_entry.delete(0, "end")

    def __grab_bucket_info_entries(self) -> None:
        """Pega os valores inseridos nos campos de entrada."""
        # Campos de entradas requeridos.
        bucket_entry = self.children["!entry3"]
        # Extrai o índice do bucket.
        bucket_id: str = bucket_entry.get()

        # Valia a entrada.
        if len(bucket_id) > 0:
            # Verifica se o índice do bucket possui somente números.
            if bucket_id.isdigit():
                # Chama a função para ver as informações do bucket.
                self.master_container.app.get_bucket_info(int(bucket_id))
        # Limpa o campo de entrada.
        bucket_entry.delete(0, "end")
