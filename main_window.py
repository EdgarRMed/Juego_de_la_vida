import tkinter as tk
from functools import partial
import table
import game_logic as g_log
import PatronesConocidos as pat_c


class StartPage:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.grid(sticky='news')
        self.radio_var = tk.IntVar(self.frame, None)

        # matrix dimensions
        self.size_m = 42
        self.size_n = 80

        self.page_setup()

    def load_images(self):
        pass

    def page_setup(self):
        tk.Label(self.frame, text="Selecciona una partida", relief='solid',
                 padx=20, pady=10).grid(row=0, columnspan=2, pady=10)
        self.radio_button_setup()
        self.select_btn = tk.Button(self.frame, bg='black', fg='white', text='Seleccionar')
        self.select_btn.grid(row=3, columnspan=2, pady=8)
        self.select_btn.bind("<Button-1>", partial(self.selection_button))

        for i in range(2):
            self.frame.grid_columnconfigure(i, weight=1, minsize=200)

        for j in range(1, 3):
            self.frame.grid_rowconfigure(j, weight=1)

    def radio_button_setup(self):
        labels = (('En blanco', 'Cargar archivo'),
                  ('Aleatorio', 'Patrones...'))
        value = 0
        for row in range(2):
            for column in range(2):
                temp_radbutton = tk.Radiobutton(self.frame, bg="black", fg='white', text=labels[row][column],
                                                variable=self.radio_var, value=value, indicatoron=0,
                                                selectcolor='orangered', activebackground='darkslategray')
                temp_radbutton.grid(row=row+1, column=column, sticky='NEWS', padx=2, pady=2)
                value += 1

    def selection_button(self, event):
        del event
        opt = self.radio_var.get()

        if opt != 'None':
            if opt == 3:
                self.open_pattern_window()
            else:
                self.start_game(opt)
        else:
            pass

    def start_game(self, opt):
        p_mat, s_mat = g_log.start_from_option(opt, self.size_m, self.size_n)
        if p_mat == '':
            pass
        else:
            game_window = tk.Toplevel(self.master)
            game_window.wm_geometry("1200x700")
            self.game_app = table.TableGrid(game_window, self.size_m, self.size_n, p_mat, s_mat)

    def open_pattern_window(self):
        pattern_window = tk.Toplevel(self.master)
        pattern_window.wm_geometry('600x500')
        self.patt_w_app = pat_c.PatronesConocidos(pattern_window, self.size_m, self.size_n)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Game of Life")
    root.geometry("400x500")
    app = StartPage(root)
    app.master.columnconfigure(0, weight=1)
    app.master.rowconfigure(0, weight=1)
    root.mainloop()
