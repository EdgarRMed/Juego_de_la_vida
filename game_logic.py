import random
import pickle
import tkinter.filedialog as tk_fd
import tkinter.messagebox as msgbox

ALIVE = "1"
DEAD = "0"


def invalid_value_msg():
    msgbox.showwarning(
        "Error",
        "Introdujo un valor u opción inválidos. Inténtelo de nuevo."
    )


def show_matrix(mat, size_m, size_n):
    for i in range(size_m):
        for j in range(size_n):
            print(f'{mat[i][j]}', end='')
        print('|')
    print('-'*size_n)


def create_blank_matrix(m, n):
    mat = [[DEAD for j in range(n)] for i in range(m)]

    return mat


def clean_matrix(mat, size_m, size_n):
    for i in range(size_m):
        for j in range(size_n):
            mat[i][j] = DEAD


def random_mode(mat, size_m, size_n):
    # rellena la matriz con 300 celulas vivas aleatoriamente
    for i in range(500):
        mat[random.randint(0, size_m-1)][random.randint(0, size_n-1)] = ALIVE


def load_from_pattern_folder(file_name: str):
    file_path = f'patterns/{file_name}'

    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            mat = data['mat']
            return mat

    except FileNotFoundError:
        msgbox.showerror(title='File not found', message='The pattern you tried to open was not found.\n'
                                                         'Check your files at "patterns" folder.')
        return ''

    except KeyError:
        msgbox.showerror(title='Reading error', message='The file you tried to open was corrupt or non-compatible.\n'
                                                        'Try with a different file.')
        return ''


def load_from_file():
    file_path = tk_fd.askopenfilename(title='Open pattern file', initialdir='patterns/personal/', filetypes=(
        ('Binary file', '*.bin'), ('All', '*.*')))

    if file_path == '':
        return ''

    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            mat = data['mat']
            return mat

    except KeyError:
        msgbox.showerror(title='Reading error', message='The file you tried to open was corrupt or non-compatible.\n'
                                                        'Try with a different file.')
        return ''


def count_neighbors(i, j, mat, size_m, size_n):
    cont = 0
    for k in range(-1, 2, 1):
        for l in range(-1, 2, 1):
            i_pos = i + k
            j_pos = j + l

            if (i_pos != i or j_pos != j) and (-1 not in (i_pos, j_pos) and i_pos != size_m and j_pos != size_n):
                if mat[i_pos][j_pos] == ALIVE:
                    cont += 1

    return cont


def new_gen(mat, new_mat, size_m, size_n):
    updated_cells = []
    for i in range(size_m):
        for j in range(size_n):
            cont = count_neighbors(i, j, mat, size_m, size_n)

            if mat[i][j] == ALIVE:
                if cont not in (2, 3):
                    new_mat[i][j] = DEAD
                else:
                    new_mat[i][j] = ALIVE
                updated_cells.append((i, j))

            elif mat[i][j] == DEAD:
                if cont == 3:
                    new_mat[i][j] = ALIVE
                    updated_cells.append((i, j))

    return updated_cells


def update_p_mat(mat, new_mat, size_m, size_n):
    for i in range(size_m):
        for j in range(size_n):
            mat[i][j] = new_mat[i][j]


def start_from_option(op, len_m, len_n, file_name=''):
    s_mat = create_blank_matrix(len_m, len_n)

    if op == 0:  # blank_matrix
        p_mat = create_blank_matrix(len_m, len_n)
        return p_mat, s_mat

    elif op == 1:  # load_from_file
        something = load_from_file()
        if something != True and something != False:
            p_mat = something
            return p_mat, s_mat
        else:
            pass

    elif op == 2:  # random mode
        p_mat = create_blank_matrix(len_m, len_n)
        random_mode(p_mat, len_m, len_n)
        return p_mat, s_mat

    elif op == 3:   # pattern
        p_mat = load_from_pattern_folder(file_name)
        return p_mat, s_mat

    else:
        invalid_value_msg()
