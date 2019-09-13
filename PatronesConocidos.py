import tkinter as tk
from functools import partial
import game_logic as g_log
import table
import Funciones as fun


class PatronesConocidos:

    def __init__(self, parent, size_m, size_n):
        self.frame = tk.Frame(parent)
        self.image_dict = {'0': tk.PhotoImage(file="Images/patron1n.png"),
                           '1': tk.PhotoImage(file="Images/patron2.png"),
                           '2': tk.PhotoImage(file="Images/patron3n.png"),
                           '3': tk.PhotoImage(file="Images/patron4n.png"),
                           '4': tk.PhotoImage(file="Images/patron5.png"),
                           '5': tk.PhotoImage(file='Images/OR.png')}

        self.size_m, self.size_n = size_m, size_n

        self.master = parent

        self.setUp()

    def openInformation(self):
        information_win = tk.Toplevel(self.master)
        information_win.title("Información")
        instructionsFrame = tk.Frame(information_win)
        f = open("text/informacion.txt", "r")
        texto = f.read()
        f.close()
        label = tk.Label(information_win, text=texto, font=("Free Sans", 12), justify=tk.LEFT)
        label.pack(side="top", fill="both", padx=10, pady=10)
        okButton = tk.Button(information_win, text="Ok", font=("Free Sans", 17), command=information_win.destroy,
                             bg="blue")
        okButton.pack(side="top", padx=100, pady=5)
        information_win.resizable(width=False, height=False)
        information_win.mainloop()

    def setUp(self):
        # Paso 1 se crea la barra de menús
        menuBar = tk.Menu(self.frame)
        menuBar.config(bg="white", fg="navy")
        # Paso 2 se crean los menús
        menuArchivo = tk.Menu(menuBar, tearoff=0)
        # Paso 3 se crean los comandos de los menús
        menuArchivo.add_command(label="Información", font=("Comic Sans Ms", 15), command=self.openInformation)
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", font=("Comic Sans Ms", 15), command=self.master.destroy)
        # Paso 4 Agregar los menús a la barra de menús
        menuBar.add_cascade(label="Archivo", font=("Comic Sans Ms", 15), menu=menuArchivo)
        # Paso 5 Indicar que la barra de menús estará en la ventana
        self.master.config(menu=menuBar)

        for i in range(2):
            self.master.grid_columnconfigure(i, weight=1)

        for j in range(3):
            self.master.grid_rowconfigure(j, weight=1)

        button_text = ('Constantes', 'Osciladores', 'Naves\nespaciales', 'En aumento', 'Inestables',
                       'Compuertas\nlógicas')

        n = 0
        for k in range(3):
            for l in range(2):
                tk.Button(self.master, text=button_text[n], image=self.image_dict[f'{n}'], compound='left',
                          font=("Comic Sans Ms", 15), command=partial(self.select_button, f'{n}')).grid(row=k,
                                                                                                        column=l,
                                                                                                        sticky='NEWS')
                n += 1

    def start_game(self, file_name):
        p_mat, s_mat = g_log.start_from_option(3, self.size_m, self.size_n, file_name)
        if p_mat == '':
            pass
        else:
            game_window = tk.Toplevel(self.master)
            game_window.wm_geometry("1200x700")
            self.game_app = table.TableGrid(game_window, self.size_m, self.size_n, p_mat, s_mat)

    def select_button(self, opt):
        file_name = ''
        if opt == '5':
            self.open_fun()
        else:
            if opt == "0":
                file_name = "constantes.bin"
            elif opt == "1":
                file_name = "osciladores.bin"
            elif opt == "2":
                file_name = "naves.bin"
            elif opt == "3":
                file_name = "en_aumento.bin"
            elif opt == "4":
                file_name = "inestables.bin"

            self.start_game(file_name)

    def open_fun(self):
        funciones_window = tk.Toplevel(self.master)
        funciones_window.wm_geometry('600x300')
        self.fun_w_app = fun.Funciones(funciones_window, self.size_m, self.size_n)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Patrones conocidos")
    root.geometry("600x500")
    #patronesConocidos = PatronesConocidos(root).frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
