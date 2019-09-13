import game_logic as g_log
import tkinter as tk
from tkinter import filedialog as tk_fd
from functools import partial
import pickle
import copy


class TableGrid:
    def __init__(self, master, size_m: int, size_n: int, p_mat: list, s_mat: list):
        master.columnconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=0)

        self.master = master
        self.frame_grid = tk.Frame(self.master)
        self.frame_grid.grid(row=1, sticky='news')
        self.frame_controls = tk.Frame(self.master, bg='gray', height=30, relief='sunken')
        self.frame_controls.grid(row=2, sticky='ew')

        self.p_mat = p_mat
        self.s_mat = s_mat
        self.initial_point = copy.deepcopy(p_mat)
        self.size_m = size_m
        self.size_n = size_n
        self.gen_num_var = tk.IntVar(0)
        self.alive_cells_var = tk.IntVar()
        self.menu_setup()
        self.buttons_setup()
        self.controls_setup()

    def menu_setup(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        file_cascade = tk.Menu(menu_bar, tearoff=0)
        file_cascade.add_command(label='New blank', command=partial(self.clean_table))
        file_cascade.add_command(label='Save pattern...', command=partial(self.save_generation))
        file_cascade.add_separator()
        file_cascade.add_command(label='Close', command=partial(self.master.destroy))
        menu_bar.add_cascade(label='File', menu=file_cascade)

    def clean_table(self):
        g_log.clean_matrix(self.p_mat, self.size_m, self.size_n)
        g_log.clean_matrix(self.s_mat, self.size_m, self.size_n)
        for i in range(self.size_m):
            for j in range(self.size_n):
                temp_widget = self.frame_grid.grid_slaves(row=i, column=j)[0]
                temp_widget['background'] = '#292524'

        self.alive_cells_var.set(0)
        self.gen_num_var.set(0)

    def buttons_setup(self):
        alive_count = 0
        for row in range(self.size_m):
            for col in range(self.size_n):
                temp_widget = tk.Button(self.frame_grid, bg='#292524')

                # Si la celula esta viva se pone de color amarillo
                if self.p_mat[row][col] == g_log.ALIVE:
                    temp_widget['background'] = 'yellow'
                    alive_count += 1
                # De lo contrario se pondra en negro
                else:
                    temp_widget['background'] = '#292524'
                temp_widget.grid(row=row, column=col, sticky="NEWS")
                temp_widget.bind("<Button-1>", partial(self.change_cell, row, col))

        self.alive_cells_var.set(alive_count)

        for i in range(self.size_m):
            self.frame_grid.grid_rowconfigure(i, weight=1)

        for j in range(self.size_n):
            self.frame_grid.grid_columnconfigure(j, weight=1)

    def change_cell(self, i, j, event):
        del event

        temp_widget = self.frame_grid.grid_slaves(row=i, column=j)[0]
        if self.p_mat[i][j] == g_log.ALIVE:
            self.p_mat[i][j] = g_log.DEAD
            temp_widget['background'] = '#292524'
            self.alive_cells_var.set(self.alive_cells_var.get() - 1)
        else:
            self.p_mat[i][j] = g_log.ALIVE
            temp_widget['background'] = 'yellow'
            self.alive_cells_var.set(self.alive_cells_var.get() + 1)

    def controls_setup(self):
        save_initial_point_btn = tk.Button(self.frame_controls, text='Save as initial point')
        save_initial_point_btn.grid(row=0, column=0)
        save_initial_point_btn.bind('<Button-1>', partial(self.save_init_point))
        self.master.bind('s', partial(self.save_init_point))

        return_initial_point_btn = tk.Button(self.frame_controls, text='Return to initial point')
        return_initial_point_btn.grid(row=0, column=1)
        return_initial_point_btn.bind('<Button-1>', partial(self.return_init_point))
        self.master.bind('r', partial(self.return_init_point))

        next_btn = tk.Button(self.frame_controls, text='Next gen')
        next_btn.grid(row=0, column=2)
        next_btn.bind('<Button-1>', partial(self.next_button))
        self.master.bind('<Right>', partial(self.next_button))

        number_gen_text = tk.Label(self.frame_controls, text='Num. of generations:', anchor='e', padx=3)
        number_gen_text.grid(row=0, column=3, padx=5)

        gen_num = tk.Label(self.frame_controls, textvariable=self.gen_num_var, anchor='w')
        gen_num.grid(row=0, column=4)

        number_alive_cells_text = tk.Label(self.frame_controls, text='Num. of living cells:', anchor='e', padx=3)
        number_alive_cells_text.grid(row=0, column=5, padx=5)

        alive_cells = tk.Label(self.frame_controls, textvariable=self.alive_cells_var, anchor='w')
        alive_cells.grid(row=0, column=6)

    def next_button(self, event):
        del event
        updated_cells = g_log.new_gen(self.p_mat, self.s_mat, self.size_m, self.size_n)

        alive_count = 0
        for i, j in updated_cells:
            if self.s_mat[i][j] != self.p_mat[i][j]:
                temp_widget = self.frame_grid.grid_slaves(row=i, column=j)[0]

                if self.s_mat[i][j] == g_log.DEAD:
                    temp_widget['background'] = '#292524'
                else:
                    temp_widget['background'] = 'yellow'

            if self.s_mat[i][j] == g_log.ALIVE:
                alive_count += 1

        g_log.update_p_mat(self.p_mat, self.s_mat, self.size_m, self.size_n)
        self.gen_num_var.set(self.gen_num_var.get()+1)
        self.alive_cells_var.set(alive_count)

    def save_init_point(self, event):
        del event
        g_log.update_p_mat(self.initial_point, self.p_mat, self.size_m, self.size_n)

    def return_init_point(self, event):
        del event
        g_log.update_p_mat(self.p_mat, self.initial_point, self.size_m, self.size_n)
        g_log.clean_matrix(self.s_mat, self.size_m, self.size_n)

        for i in range(self.size_m):
            for j in range(self.size_n):
                temp_widget = self.frame_grid.grid_slaves(row=i, column=j)[0]
                if self.p_mat[i][j] == g_log.ALIVE:
                    temp_widget['background'] = 'yellow'
                else:
                    temp_widget['background'] = '#292524'

        self.gen_num_var.set(0)

    def save_generation(self):
        file_path = tk_fd.asksaveasfilename(parent=self.master, title='Save generation...',
                                            filetypes=(('Binary file', '*.bin'), ('All', '*.*')))

        if file_path == '':
            pass
        else:
            mat_key = {'mat': self.p_mat}

            with open(file_path, 'wb') as file:
                pickle.dump(mat_key, file)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Game of Life")
    root.geometry("1200x640")
    #minsize
    app = TableGrid(root, 'xd', 'xd').frame_grid.pack(fill=tk.BOTH, expand=True)
    root.mainloop()