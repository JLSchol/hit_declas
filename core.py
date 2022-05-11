import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askdirectory, askopenfilename
from tkinter.messagebox  import showinfo

from modules.data_manager import JsonHelper, ProjectPaths
from modules.tkinter_utils import Button, Grid, Entry, Label



class App(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.paths = ProjectPaths()
        self.config = JsonHelper(self.paths.config).data # check if config exists

        # Create the application entry variables
        self.name_var = tk.StringVar(value=self.config["name"])
        self.months_var = tk.StringVar()
        self.iban_var = tk.StringVar(value=self.config["iban"])
        self.inv_date_var = tk.StringVar()
        self.declared_months_var = tk.StringVar()
        self.inv_nr_var = tk.IntVar()
        self.signature_var = tk.StringVar(value=self.config["signature"])
        self.receits_var = tk.StringVar(value=self.config["receits"])
        

        self.init_frame("HIT declarations", 1280, 720, "black", "#ff6666", 0.02, 0.02)

        self.rows, self.cols = 20, 15
        self.grid = Grid(self.rows, self.cols, 0.05, 0.05)

        self.initialize_layout()

    def init_frame(self, title, width, height, bg_color, fg_color, margin_x, margin_y):
        self.root.title(title)
        self.root["bg"]= bg_color
        self.root.geometry(f"{width}x{height}")

        frame = tk.Frame(self.root, bg=fg_color).place(
            relx=margin_x, rely=margin_y, 
            relwidth=1-2*margin_x,relheight=1-2*margin_y)

    def initialize_layout(self):
        self.init_invoice_section() # first three rows

        self.init_decla_section() # middle section

        self.init_conformation_section() # button section

    def init_invoice_section(self):
        # left block
        Label(self.root, "Name", 
            self.grid.x[0], self.grid.y[0], self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.name_var, self.name_cb,
            self.grid.x[1], self.grid.y[0], 2*self.grid.cell_w, self.grid.cell_h)

        Label(self.root, "IBAN", 
            self.grid.x[0], self.grid.y[1], self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.iban_var, self.iban_cb,
            self.grid.x[1], self.grid.y[1], 2*self.grid.cell_w, self.grid.cell_h)

        Label(self.root, "Month(s)", 
            self.grid.x[0], self.grid.y[2], self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.declared_months_var, self.declared_months_cb,
            self.grid.x[1], self.grid.y[2], 2*self.grid.cell_w, self.grid.cell_h)

        # middle block
        Label(self.root, "invoice nr", 
            self.grid.x[4], self.grid.y[0], self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.inv_nr_var, self.inv_nr_cb,
            self.grid.x[5], self.grid.y[0], self.grid.cell_w, self.grid.cell_h)

        Label(self.root, "invoice date", 
            self.grid.x[4], self.grid.y[1], self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.inv_date_var, self.inv_date_cb,
            self.grid.x[5], self.grid.y[1], self.grid.cell_w, self.grid.cell_h)

        # last block
        Button(self.root, "select signature path", self.set_signature_but,
            self.grid.x[7], self.grid.y[0], 2*self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.signature_var, self.signature_cb,
            self.grid.x[9], self.grid.y[0], 6*self.grid.cell_w, self.grid.cell_h)

        Button(self.root, "select receits dir", self.set_receits_dir_but,
            self.grid.x[7], self.grid.y[1], 2*self.grid.cell_w, self.grid.cell_h)
        Entry(self.root, self.receits_var, self.receits_cb,
            self.grid.x[9], self.grid.y[1], 6*self.grid.cell_w, self.grid.cell_h)

        # save but
        Button(self.root, "save settings as default", self.save_settings_but,
            self.grid.x[-2], self.grid.y[2], 2*self.grid.cell_w, self.grid.cell_h)

    def init_decla_section(self):
        pass

    def init_conformation_section(self):
        pass


    ##CALLBACKS
    # buttons
    def set_signature_but(self):
        path = Path( askopenfilename(
            parent=self.root,
            initialdir=self.paths.config_dir,
            title="please select signature image",
            filetypes=[('png files', '*.png'), ('jpeg files', '*.jpeg')],
            multiple=False) )
        self.signature_var.set(path)

    def set_receits_dir_but(self):
        path = Path(askdirectory(
            parent=self.root,
            initialdir=self.paths.receits_dir.parent,
            title="please select directory containing receits") )
        self.receits_var.set(path)

    def save_settings_but(self):
        # write to jsonfile
        self.config["name"] = self.name_var.get()
        self.config["iban"] = self.iban_var.get()
        self.config["signature"] = self.signature_var.get()
        self.config["receits"] = self.receits_var.get()
        JsonHelper().write_json(self.config, self.paths.config)

        # popop textbox
        name = f"Name: \n{self.name_var.get()}\n\n"
        iban = f"IBAN: \n{self.iban_var.get()}\n\n"
        signature = f"signature: \n{self.signature_var.get()}\n\n"
        receits = f"receits dir: \n{self.receits_var.get()}"
        text = name + iban + signature + receits
        showinfo("settings saved as default", text)

    # trace variables
    def name_cb(self, *args):
        print(self.name_var.get())

    def months_cb(self, *args):
        print(self.months_var.get())

    def iban_cb(self, *args):
        print(self.iban_var.get())

    def inv_date_cb(self, *args):
        print(self.inv_date_var.get())

    def inv_nr_cb(self, *args):
        print(self.inv_nr_var.get())

    def declared_months_cb(self, *args):
        print(self.declared_months_var.get())

    def signature_cb(self, *args):
        print(self.signature_var.get())

    def receits_cb(self, *args):
        print(self.receits_var.get())



if __name__ == "__main__":
    paths = ProjectPaths()
    # paths.show_dirs()
    # paths.show_files()
    data = JsonHelper(paths.config).data
    # print(data)

    root = tk.Tk()
    decla_gui = App(root)
    decla_gui.mainloop()