import tkinter as tk

class Grid:
    def __init__(self, nr_rows, nr_cols, marg_x, marg_y):
        self.nr_cols = nr_cols
        self.nr_rows = nr_rows
        self.marg_x = marg_x
        self.marg_y = marg_y

        self.cell_w = self.calc_size_per_dim(nr_cols, marg_x)
        self.cell_h = self.calc_size_per_dim(nr_rows, marg_y)

        self.x = self.get_positions(nr_cols, marg_x, self.cell_w)
        self.y = self.get_positions(nr_rows, marg_y, self.cell_h)

        # self.show()
        # print()

    def calc_size_per_dim(self, nr_dim, rel_margin):
        if rel_margin >= 0.5:
            print(f"{rel_margin=} does not leave space for creating rows")

        available_size = 1 - 2*rel_margin

        return available_size/nr_dim

    def get_positions(self, nr_dim, start_pos, cell_size):
        return [start_pos + i*cell_size for i in range(nr_dim)]

    def show(self):
        print(f"{self.nr_cols = }")
        print(f"{self.cell_w = }")
        print(f"{self.x = }")
        print('--')
        print(f"{self.nr_rows = }")
        print(f"{self.cell_h = }")
        print(f"{self.y = }")
        print('--')
        print(f"{self.marg_x = }")
        print(f"{self.marg_y = }")
        print()

class Button:
    def __init__(self, master, text, cb_fun, 
                rel_x, rel_y, rel_width, rel_height):
        self.master = master
        self.text = text
        self.cb_fun = cb_fun

        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height

        self.tk_button = self.create_button(master, text, cb_fun)
        self.place_button(self.tk_button, rel_x, rel_y, rel_width, rel_height)

        # self.show()
        # print()

    def create_button(self, master, text, cb_fun):
        return tk.Button(master, text=text, command=cb_fun)

    def place_button(self, tk_button, rel_x, rel_y, rel_width, rel_height):
        tk_button.place(relx=rel_x, rely=rel_y, relwidth=rel_width, relheight=rel_height)

    def show(self):
        print(f"{self.master=}")
        print(f"{self.text=}")
        print(f"{self.cb_fun=}")
        print(f"{self.rel_x=}")
        print(f"{self.rel_y=}")
        print(f"{self.rel_width=}")
        print(f"{self.rel_height=}")
        print(f"{self.tk_button=}")

class Label:
    def __init__(self, master, text, 
        rel_x, rel_y, rel_width, rel_height):
        self.master = master
        self.text = text

        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height

        self.tk_label = self.create_label(master, text)
        self.place_label(self.tk_label, rel_x, rel_y, rel_width, rel_height)

        # self.show()
        # print()

    def create_label(self, master, text):
        return tk.Label(master, text=text)

    def place_label(self, tk_label, rel_x, rel_y, rel_width, rel_height):
        tk_label.place(relx=rel_x, rely=rel_y, relwidth=rel_width, relheight=rel_height)

    def show(self):
        print(f"{self.master =}")
        print(f"{self.text = }")
        print(f"{self.rel_x = }")
        print(f"{self.rel_y = }")
        print(f"{self.rel_width = }")
        print(f"{self.rel_height = }")
        print(f"{self.tk_label = }")

class Entry:
    def __init__(self, master, tk_text_var, cb_fun,
        rel_x, rel_y, rel_width, rel_height):
        self.master = master
        self.tk_text_var = tk_text_var
        self.cb_fun = cb_fun

        self.rel_x = rel_x
        self.rel_y = rel_y
        self.rel_width = rel_width
        self.rel_height = rel_height
        
        self.bg_color = "white"

        self.tk_entry = self.create_entry(master, tk_text_var)
        self.tk_text_var.trace('w', cb_fun)
        self.place_entry(self.tk_entry, rel_x, rel_y, rel_width, rel_height)

        # self.show()
        # print()

    def create_entry(self, master, tk_text_var):
        return tk.Entry(self.master, bg=self.bg_color, textvariable=tk_text_var)

    def place_entry(self, tk_entry, rel_x, rel_y, rel_width, rel_height):
        tk_entry.place(relx=rel_x, rely=rel_y, relwidth=rel_width, relheight=rel_height)