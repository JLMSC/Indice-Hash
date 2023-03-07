"""Representa um GUI."""
import tkinter as tk

# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

# TODO: Implementar a Interface Gráfica.
class Application:
    """Interfáce Gráfica (GUI)."""
    # A aplicação top-level principal.
    master: tk.Tk

    def __init__(self, master: tk.Tk=None) -> None:
        """Inicializa as principais variáveis da aplicação.

        Args:
            master (tk.Tk, optional): A aplicação top-level principal.
            Valor padrão é "None".
        """
        # Define a aplicação top-level nesta aplicação.
        self.master = master
        # Realiza as primeiras configurações na aplicação.
        self.__first_time_setup()

    def __first_time_setup(self) -> None:
        """Realiza as primeira configurações da aplicação,
        configura nome da janela, tamanho, posicionamento etc."""
        # Define o título da aplicação para "Índice Hash".
        self.master.title("Índice Hash")
        # Define a resolução da janela (800x600).
        self.master.geometry("800x600")
        # Define o ícone da aplicação.
        self.master.iconphoto(True, tk.PhotoImage(file="src/GUI/assets/icon.png"))


if __name__ == "__main__":
    root = tk.Tk()
    Application(root)
    root.mainloop()
