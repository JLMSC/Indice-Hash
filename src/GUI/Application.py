"""Representa um GUI."""

from tkinter.font import Font
from tkinter import Tk, PhotoImage, Text, Button
from tkinter.ttk import Label, Frame, Entry, Style

# pylint: disable=import-error

from structs.Tabela import Tabela
from structs.Pagina import Pagina
from structs.Bucket import BucketManager

# FIXME: Revisar função por função.

# TODO: Implementar a Interface Gráfica.
class Application:
    """Interfáce Gráfica (GUI)."""
    # A aplicação top-level principal.
    master: Tk
    # O tema da aplicação.
    app_style: Style
    # A largura e comprimento da aplicação.
    width: int = 800
    height: int = 600
    # O Frame em que será renderizado os objetos/elementos da aplicação.
    page_frame: Frame
    search_frame: Frame
    # A fonte usada nos textos da aplicação.
    label_font: Font
    # A fonte usada nos botões da aplicação.
    button_font: Font
    # A fonte usada na sáida da aplicação.
    output_font: Font
    # Contém todas as Tuplas registradas.
    table: Tabela
    # Contém a divisão e alocação da Tabela.
    page: Pagina
    # Responsável pelo Mapeamento das chaves de busca.
    bucket: BucketManager

    def __init__(self, master: Tk = None, table: Tabela = None) -> None:
        """Inicializa as principais variáveis da aplicação.

        Args:
            master (tk.Tk, optional): A aplicação top-level principal.
            Valor padrão é "None".
            table (Tabela, optional): A Tabela com todas as Tuplas registradas.
            Valor padrão é "None".
        """
        # Define a aplicação top-level nesta aplicação.
        self.master = master
        # Define a Tabela com todas as Tuplas registradas.
        self.table = table
        # Inicializa o Bucket.
        self.bucket = BucketManager(self.table.get_size())
        # Insere as Tuplas da Tabela no Bucket.
        self.bucket.insert_data_from_table(self.table)
        # Define um tema para a aplicação.
        self.set_theme("plastik")
        # Realiza as primeiras configurações na aplicação.
        self.__first_time_setup()
        # Adiciona alguns objetos/elementos à aplicação.
        self.__draw_in_window()

    def set_theme(self, theme: str) -> None:
        """Define um tema para a aplicação.

        Args:
            theme (str): O nome do tema.
        """
        self.app_style = Style(self.master)
        self.master.call("source", f"src/GUI/themes/{theme}/{theme}.tcl")
        self.app_style.theme_use(theme)

    def __first_time_setup(self) -> None:
        """Realiza as primeira configurações da aplicação,
        configura nome da janela, tamanho, posicionamento etc."""
        # Define o título da aplicação para "Índice Hash".
        self.master.title("Índice Hash")
        # Define a resolução da janela (800x600).
        self.master.geometry(f"{self.width}x{self.height}")
        # Impede o redimensionamento da aplicação.
        self.master.resizable(False, False)
        # Define o ícone da aplicação.
        self.master.iconphoto(True, PhotoImage(file="src/GUI/assets/icon.png"))
        # Define as fontes da aplicação.
        self.__configure_fonts()
        # Define os 'Frames' de acordo com a estrutura da aplicação.
        self.__setup_frames()

    def __configure_fonts(self) -> None:
        """Define as fontes usadas nos objetos da aplicação aplicação."""
        # Define a fonte dos textos da aplicação.
        self.label_font = Font(family="Callibri", size=16, weight="normal")
        # Define a fonte dos botões da aplicação.
        self.button_font = Font(size=12)
        # Define a fonte da saída da aplicação.
        self.output_font = Font(size=12)


    def __setup_frames(self) -> None:
        """Define os 'Frames' conforme a estrutura da aplicação."""
        # Cria o primeiro 'Frame'.
        self.page_frame = Frame(self.master, relief="sunken")
        self.page_frame.pack(
            fill="both", expand=False, padx=0.01 * self.width, pady=0.01 * self.height
        )
        # Configura o 'grid' do primeiro 'Frame'.
        self.page_frame.grid_columnconfigure(0, weight=0)
        self.page_frame.grid_columnconfigure(1, weight=1)

        # Cria o segundo 'Frame'.
        self.search_frame = Frame(self.master, relief="sunken")
        # Configura o 'grid' do segundo 'Frame'.
        self.search_frame.grid_columnconfigure(0, weight=0)
        self.search_frame.grid_columnconfigure(1, weight=1)
        self.search_frame.grid_rowconfigure(3, weight=1)

    def draw_label(self, frame: Frame, text: str, column: int, row: int, sticky: str) -> None:
        """Renderiza um 'Label' no 'Frame' alvo.

        Args:
            frame (Frame): O 'Frame' onde será renderizado o 'Label'.
            text (str): O texto a ser renderizado no 'Label'.
            column (int): A coluna do 'Label' no 'Frame'.
            row (int): A linha do 'Label' no 'Frame'.
            sticky (str): A posição do 'Label' no 'Frame'.
        """
        Label(
            frame,
            text=text,
            font=self.label_font
        ).grid(
            padx=0.01 * self.width,
            pady=0.01 * self.height,
            column=column,
            row=row,
            sticky=sticky,
        )

    def draw_entry(self, frame: Frame, column: int, row: int, sticky: str) -> None:
        """Renderiza um 'Entry' no 'Frame' alvo.

        Args:
            frame (Frame): O 'Frame' onde será renderizado o 'Entry'.
            column (int): A coluna do 'Entry' no 'Frame'.
            row (int): A linha do 'Entry' no 'Frame'.
            sticky (str): A posição do 'Entry' no 'Frame'.
        """
        Entry(
            frame,
            font=self.button_font
        ).grid(
            padx=0.01 * self.width,
            pady=0.01 * self.height,
            column=column,
            row=row,
            sticky=sticky
        )

    def draw_button(self, frame: Frame, text: str, column: int, row: int, sticky: str, func) -> None:
        """Renderiza um 'Button' no 'Frame' alvo.

        Args:
            frame (Frame): O 'Frame' onde será renderizado o 'Button'.
            text (str): O texto a ser renderizado no 'Button'.
            column (int): A coluna do 'Button' no 'Frame'.
            row (int): A linha do 'Button' no 'Frame'.
            sticky (str): A posição do 'Button' no 'Frame'.
        """
        Button(
            frame,
            text=text,
            font=self.button_font,
            command=func
        ).grid(
            padx=0.01 * self.width,
            pady=0.01 * self.height,
            column=column,
            row=row,
            sticky=sticky
        )

    def draw_output(self, frame: Frame, column: int, row: int, sticky: str) -> None:
        """Renderiza um 'Output' no 'Frame' alvo.

        Args:
            frame (Frame): O 'Frame' onde será renderizado o 'Output'.
            column (int): A coluna do 'Output' no 'Frame'.
            row (int): A linha do 'Output' no 'Frame'.
            sticky (str): A posição do 'Output' no 'Frame'.
        """
        Text(
            frame,
            font=self.output_font
        ).grid(
            padx=0.01 * self.width,
            pady=0.01 * self.height,
            column=column,
            row=row,
            columnspan=2,
            sticky=sticky
        )

    def __draw_in_window(self) -> None:
        """Adiciona alguns objetos/elementos à aplicação."""
        # Configura os objetos relacionados à manipulação da Página.
        # Campo referente a inserção e identificação do tamanho da Página.
        self.draw_label(
            self.page_frame,
            text="Tamanho da Página:",
            column=0,
            row=0,
            sticky="W"
        )
        self.draw_entry(
            self.page_frame,
            column=1,
            row=0,
            sticky="NSWE"
        )
        self.draw_button(
            self.page_frame,
            text="Ajustar Página",
            column=0,
            row=1,
            sticky="W",
            func=self.__adjust_page_size
        )

        # Configura os objetos relacionados à busca de uma chave.
        # Campo referente a inserção e identificação de uma chave.
        self.draw_label(
            self.search_frame,
            text="Chave a ser buscada:",
            column=0,
            row=0,
            sticky="W"
        )
        self.draw_entry(
            self.search_frame,
            column=1,
            row=0,
            sticky="NSWE"
        )
        # Campo referente a quantificação de busca.
        self.draw_label(
            self.search_frame,
            text="Qntd. máxima de busca na Tabela:",
            column=0,
            row=1,
            sticky="W"
        )
        self.draw_entry(
            self.search_frame,
            column=1,
            row=1,
            sticky="NSWE"
        )
        # Botões de buscas.
        self.draw_button(
            self.search_frame,
            text="Buscar na Tabela",
            column=0,
            row=2,
            sticky="W",
            func=self.__table_scan
        )
        self.draw_button(
            self.search_frame,
            text="Buscar nos Buckets",
            column=1,
            row=2,
            sticky="E",
            func=self.__bucket_search
        )
        # Campo de saída.
        self.draw_output(
            self.search_frame,
            column=0,
            row=3,
            sticky="NSWE"
        )

    def clear_output(self, output_widget: Text) -> None:
        """Limpa o conteúdo do 'Output'.

        Args:
            output_widget (Text): O 'Output' a ter o conteúdo limpado.
        """
        output_widget.delete("1.0", "end")

    def update_output(self, output_widget: Text, text: str) -> None:
        """Atualiza o 'Output' da aplicação.

        Args:
            output_widget (Text): O 'Output' a ter o conteúdo limpado.
            text (str): O texto a ser inserido no 'Output' da aplicação.
        """
        self.clear_output(output_widget)
        output_widget.insert("insert", text)

    def __adjust_page_size(self) -> None:
        """Reajusta o tamanho da Página."""
        # Verifica a veracidade da entrada do usuário.
        page_size: str = self.page_frame.children["!entry"].get()
        if page_size.isdigit():
            # Reajusta a Página do Índice Hash.
            self.page = Pagina(int(page_size))
            self.page.insert(self.table)
            # Torna o segundo 'Frame' visível e ajusta-o.
            if not self.search_frame.winfo_ismapped():
                self.search_frame.pack(
                    fill="both", expand=True, padx=0.01 * self.width, pady=0.01 * self.height
                )
            # Limpa a saída da aplicação e exibe novas informações.
            self.update_output(
                self.search_frame.children["!text"],
                f"1. O tamanho da Página foi reajustado para '{page_size}'!" +
                f"\n2. Quantidade de Páginas - '{self.page.get_page_count()}'" +
                f"\n3. '{self.table.get_size()}' - Tuplas foram registradas."
            )

    def __table_scan(self) -> None:
        """Realiza um Table Scan."""
        # Verifica a veracidade da entrada do usuário.
        key: str = self.search_frame.children["!entry"].get()
        search_size: str = self.search_frame.children["!entry2"].get()
        if key.isalpha() and (search_size.isdigit() or not search_size):
            # Ajusta a qntd. de busca.
            search_size = int(search_size) if search_size else None
            # Realiza o Table Scan.
            tuple_from_table = self.table.table_scan(key, search_size)
            # TODO: Só isso que tem que mostrar? precisa mostar a posição na tabela?
            # Limpa a saída da aplicação e exibe novas informações.
            self.update_output(
                self.search_frame.children["!text"],
                f"1. Tupla '{tuple_from_table.get_data()}' encontrada!"
                if tuple_from_table else
                f"1. Nenhuma Tupla com o dado '{key}' " +
                f"foi encontrado em '{search_size}' buscas."
            )

    def __bucket_search(self) -> None:
        """Realiza uma busca nos Buckets."""
        # Verifica a veracidade da entrada do usuário.
        key: str = self.search_frame.children["!entry"].get()
        if key.isalpha():
            # Realiza a busca pela Tupla nos Buckets.
            tuple_from_bucket = self.bucket.search_data(key)
            # TODO: Precisa mostrar o índice do bucket? colisão dele? overflow?
            # Limpa a saída da aplicação e exibe novas informações.
            self.update_output(
                self.search_frame.children["!text"],
                f"1. A Tupla '{tuple_from_bucket.get_data()}' foi encontrada!" +
                f"\n2. Sua posição na Página é '{tuple_from_bucket.get_page_index()}'"
                if tuple_from_bucket else
                f"1. Nenhuma Tupla com o dado '{key}' foi encontradon nos Buckets."
            )
