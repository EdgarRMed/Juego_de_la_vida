import tkinter as tk
from functools import partial
import game_logic as g_log
import table


class Funciones:

    def __init__(self, parent, size_m, size_n):
        self.size_m = size_m
        self.size_n = size_n
        self.frame = tk.Frame(parent)
        self.imagen1 = tk.PhotoImage(file="Images/AND.png")
        self.imagen2 = tk.PhotoImage(file="Images/OR.png")
        self.imagen3 = tk.PhotoImage(file="Images/NOT.png")
        self.imagen4 = tk.PhotoImage(file="Images/SUMA.png")
        self.imagen5 = tk.PhotoImage(file="Images/colisiones1.png")
        self.imagen6 = tk.PhotoImage(file="Images/colisiones2.png")
        self.imagen7 = tk.PhotoImage(file="Images/ANDinfo.png")
        self.imagen8 = tk.PhotoImage(file="Images/ORinfo.png")
        self.imagen9 = tk.PhotoImage(file="Images/NOTinfo.png")
        self.imagen10 = tk.PhotoImage(file="Images/SUMinfo.png")

        self.master = parent

        self.setUp()

 ############################################ Configuración principal #################################################
    def setUp(self):
        # Paso 1 se crea la barra de menús
        menuBar = tk.Menu(self.frame)
        menuBar.config(bg="white", fg="navy")
        # Paso 2 se crean los menús
        menuArchivo = tk.Menu(menuBar, tearoff=0)
        menuInfo = tk.Menu(menuBar, tearoff =0)
        # Paso 3 se crean los comandos de los menús
        menuArchivo.add_command(label="Salir   ", font=("Comic Sans Ms", 15), command=self.master.destroy)

        ################################ Menu de informacion #############################################
        menuInfo.add_command(label = "General", font=("Comic Sans Ms", 15), command = self.openInformation)
        menuInfo.add_separator()
        menuInfo.add_command(label = "AND", font=("Comic Sans Ms", 15), command = self.openAND)
        menuInfo.add_command(label="OR", font=("Comic Sans Ms", 15), command=self.openOR)
        menuInfo.add_command(label="NOT", font=("Comic Sans Ms", 15), command=self.openNOT)
        menuInfo.add_command(label="Suma binaria", font=("Comic Sans Ms", 15), command=self.openBin)
        # Paso 4 Agregar los menús a la barra de menús
        menuBar.add_cascade(label="Archivo", font=("Comic Sans Ms", 15), menu=menuArchivo)
        menuBar.add_cascade(label = "Información", font=("Comic Sans Ms", 15), menu=menuInfo )
        # Paso 5 Indicar que la barra de menús estará en la ventana
        self.master.config(menu=menuBar)

        for i in range(2):
            self.master.grid_columnconfigure(i, weight=1)

        for j in range(1):
            self.master.grid_rowconfigure(j, weight=1)


##################################33 Botones de la ventana principal #################################################################

        patron1 = tk.Button(self.master, text ="NOT", image = self.imagen3, compound = "left", font=("Comic Sans Ms", 20), command = partial(self.select_button, "NOT")).grid(column=0, row=0,sticky ='NEWS')
        #patron2 = tk.Button(self.master, text="OR", image = self.imagen2, compound = "left", font=("Comic Sans Ms", 20), command = partial(self.select_button, "OR")).grid(column=0, row=1,sticky = 'NEWS')
        patron3 = tk.Button(self.master, text="AND", image = self.imagen1, compound = "left", font=("Comic Sans Ms", 20), command = partial(self.select_button, "AND")).grid(column=1, row=0,sticky = 'NEWS')
        #patron4 = tk.Button(self.master, text="Suma\nBinaria", image = self.imagen4, compound = "left", font=("Comic Sans Ms", 20), command = partial(self.select_button,"Bin")).grid(column=1, row=1,sticky = 'NEWS')
       # patron5 = tk.Button(self.frame, text="Inestables", image = self.imagen5, compound = "left").grid(column=1, row=1,sticky = 'NEWS')
       # patron6 = tk.Button(self.frame, text="Patron6").grid(column=1, row=2,sticky = 'NEWS')



################################### Ventanas secundarias ###########################################################################
    def openInformation(self):
        information_win = tk.Toplevel(self.master)
        information_win.title("Información de Funciones")
        instructionsFrame = tk.Frame(information_win)
        f = open ("text/infoFunciones.txt","r")
        texto = f.read()
        f.close()
#################################### Configuración #################################################################################
        label = tk.Label(information_win, text= texto, font=("arial", 12), justify = tk.LEFT)
        label.grid (column =0, row =0, sticky = 'NEWS', columnspan = 2)
        colision1 = tk.Label(information_win, image = self.imagen5, padx =20)
        colision1.grid (column =0, row =1)
        colision2 = tk.Label(information_win, image = self.imagen6, padx = 20)
        colision2.grid (column =1, row =1)
        okButton = tk.Button(information_win, text="Ok", font=("Free Sans", 17), command=information_win.destroy, bg="blue")
        okButton.grid (column =0, row =2, sticky = "NEWS", columnspan = 2, pady = 10)
        information_win.resizable(width=False, height=False)
        information_win.mainloop()

    def openAND(self):
        informationAND_win = tk.Toplevel(self.master)
        informationAND_win.title("Acerca de AND")
        ANDFrame = tk.Frame(informationAND_win)
        f = open("text/infoAND.txt", "r")
        texto = f.read()
        f.close()
########################################### Configuración #######################################################################
        label = tk.Label(informationAND_win, text=texto, font=("arial", 20), justify=tk.LEFT)
        label.grid(column=0, row=0, sticky='NEWS', columnspan=2)
        okButtonAND = tk.Button(informationAND_win, text="Ok", font=("Free Sans", 17), command=informationAND_win.destroy, bg="blue")
        ANDimage = tk.Label(informationAND_win, image = self.imagen7)
        ANDimage.grid(column=0,row=1)
        okButtonAND.grid(column=0, row=2, sticky="NEWS", columnspan=2, pady=10)
        informationAND_win.resizable(width=False, height=False)
        informationAND_win.mainloop()

    def openOR(self):
        informationOR_win = tk.Toplevel(self.master)
        informationOR_win.title("Acerca de OR")
        ORFrame = tk.Frame(informationOR_win)
        f = open("text/infoOR.txt", "r")
        texto = f.read()
        f.close()
        ########################################### Configuración #######################################################################
        label = tk.Label(informationOR_win, text=texto, font=("arial", 20), justify=tk.LEFT)
        label.grid(column=0, row=0, sticky='NEWS', columnspan=2)
        okButtonOR = tk.Button(informationOR_win, text="Ok", font=("Free Sans", 17),command=informationOR_win.destroy, bg="blue")
        ORimage = tk.Label(informationOR_win, image=self.imagen8)
        ORimage.grid(column=0, row=1)
        okButtonOR.grid(column=0, row=2, sticky="NEWS", columnspan=2, pady=10)
        informationOR_win.resizable(width=False, height=False)
        informationOR_win.mainloop()

    def openNOT(self):
        informationNOT_win = tk.Toplevel(self.master)
        informationNOT_win.title("Acerca de NOT")
        NOTFrame = tk.Frame(informationNOT_win)
        f = open("text/infoNOT.txt", "r")
        texto = f.read()
        f.close()
        ########################################### Configuración #######################################################################
        label = tk.Label(informationNOT_win, text=texto, font=("arial", 20), justify=tk.LEFT)
        label.grid(column=0, row=0, sticky='NEWS', columnspan=2)
        okButtonNOT = tk.Button(informationNOT_win, text="Ok", font=("Free Sans", 17), command=informationNOT_win.destroy,bg="blue")
        NOTimage = tk.Label(informationNOT_win, image=self.imagen9)
        NOTimage.grid(column=0, row=1)
        okButtonNOT.grid(column=0, row=2, sticky="NEWS", columnspan=2, pady=10)
        informationNOT_win.resizable(width=False, height=False)
        informationNOT_win.mainloop()

    def openBin(self):
        informationSUM_win = tk.Toplevel(self.master)
        informationSUM_win.title("Acerca de NOT")
        SUMFrame = tk.Frame(informationSUM_win)
        f = open("text/infoSUM.txt", "r")
        texto = f.read()
        f.close()
        ########################################### Configuración #######################################################################
        label = tk.Label(informationSUM_win, text=texto, font=("arial", 20), justify=tk.LEFT)
        label.grid(column=0, row=0, sticky='NEWS', columnspan=2)
        okButtonSUM = tk.Button(informationSUM_win, text="Ok", font=("Free Sans", 17),
                                command=informationSUM_win.destroy, bg="blue")
        SUMimage = tk.Label(informationSUM_win, image=self.imagen10)
        SUMimage.grid(column=0, row=1, columnspan =2)
        okButtonSUM.grid(column=0, row=2, sticky="NEWS", columnspan=2, pady=10)
        informationSUM_win.resizable(width=False, height=False)
        informationSUM_win.mainloop()

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
        if opt == "AND":
            file_name = "AND.bin"
        elif opt == "OR":
            file_name = "OR.bin"
        elif opt == "NOT":
            file_name = "NOT.bin"
        elif opt == "Bin":
            file_name = "Sum.bin"

        self.start_game(file_name)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Funciones")
    root.geometry("600x300")
    funciones = Funciones(root).frame.pack(fill = tk.BOTH, expand= True)
    root.mainloop()
