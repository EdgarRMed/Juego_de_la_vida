import tkinter as tk
from functools import partial

class PatronesConocidos:

    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.imagen1 = tk.PhotoImage(file="Images/patron1n.png")
        self.imagen2 = tk.PhotoImage(file="Images/patron2.png")
        self.imagen3 = tk.PhotoImage(file="Images/patron3n.png")
        self.imagen4 = tk.PhotoImage(file="Images/patron4n.png")
        self.imagen5 = tk.PhotoImage(file="Images/patron5.png")
        self.master = parent

        self.setUp()
    def openInformation(self):
        information_win = tk.Toplevel(self.master)
        information_win.title("Información")
        instructionsFrame = tk.Frame(information_win)
        f = open ("text/informacion.txt","r")
        texto = f.read()
        f.close()
        label = tk.Label(information_win, text= texto, font=("Free Sans", 12), justify = tk.LEFT)
        label.pack(side="top", fill="both", padx=10, pady=10)
        okButton = tk.Button(information_win, text = "Ok", font = ("Free Sans", 17), command = information_win.destroy, bg = "blue")
        okButton.pack(side = "top", padx =100, pady=5)
        information_win.resizable(width=False, height=False)
        information_win.mainloop()



    def setUp(self):
        # Paso 1 se crea la barra de menús
        menuBar = tk.Menu(self.frame)
        menuBar.config(bg="white", fg="navy")
        # Paso 2 se crean los menús
        menuArchivo = tk.Menu(menuBar, tearoff=0)
        # Paso 3 se crean los comandos de los menús
        menuArchivo.add_command(label="Información", font=("Comic Sans Ms", 15), command = self.openInformation)
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", font=("Comic Sans Ms", 15), command=root.destroy)
        # Paso 4 Agregar los menús a la barra de menús
        menuBar.add_cascade(label="Archivo", font=("Comic Sans Ms", 15), menu=menuArchivo)
        # Paso 5 Indicar que la barra de menús estará en la ventana
        root.config(menu=menuBar)

        for i in range(2):
            self.frame.grid_columnconfigure(i, weight=1)

        for j in range(3):
            self.frame.grid_rowconfigure(j, weight=1)



        patron1 = tk.Button(self.frame, text ="Constantes", image = self.imagen1, compound = "left", font=("Comic Sans Ms", 15), command= partial(self.select_button, "Patron1")).grid(column=0, row=0,sticky ='NEWS')

        patron2 = tk.Button(self.frame, text="Osciladores", image = self.imagen2, compound = "left", font=("Comic Sans Ms", 15), command=partial(self.select_button, "Patron2")).grid(column=0, row=1,sticky = 'NEWS')
        #patron2.bind("<Button-1>", )
        patron3 = tk.Button(self.frame, text="Naves\nespaciales", image = self.imagen3, compound = "left", font=("Comic Sans Ms", 15), command=partial(self.select_button, "Patron3")).grid(column=0, row=2,sticky = 'NEWS', columnspan=2)
        #patron3.bind("<Button-1>", )
        patron4 = tk.Button(self.frame, text="En aumento", image = self.imagen4, compound = "left", font=("Comic Sans Ms", 15), command=partial(self.select_button, "Patron4")).grid(column=1, row=0,sticky = 'NEWS')
        #patron4.bind("<Button-1>", )
        patron5 = tk.Button(self.frame, text="Inestables", image = self.imagen5, compound = "left", font=("Comic Sans Ms", 15), command=partial(self.select_button, "Patron5")).grid(column=1, row=1,sticky = 'NEWS')
        #patron5.bind("<Button-1>", )



    def select_button(self,opt):
        self.fileName = ""
        if opt == "Patron1":
            self.fileName = "Constantes.bin"
        elif opt == "Patron2":
            self.fileName = "Osciladores.bin"
        elif opt == "Patron3":
            self.fileName = "naves_espaciales.bin"
        elif opt == "Patron4":
            self.fileName="en_aumento.bin"
        elif opt == "patron5":
            self.fileName="Inestables.bin"

        return self.fileName



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Patrones conocidos")
    root.geometry("600x500")
    patronesConocidos = PatronesConocidos(root).frame.pack(fill = tk.BOTH, expand= True)
    root.mainloop()
