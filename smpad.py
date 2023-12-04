import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

class mygui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.title("SMPad")
        self.root.rowconfigure(0, minsize=800, weight=1)
        self.root.columnconfigure(1, minsize=800, weight=1)

        self.text = tk.Text(self.root, font=('arial', 12))

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save As..', command=self.save_file)
        self.filemenu.add_command(label='Clear', command=self.clear)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close', command=self.onclose)
        self.filemenu.add_command(label='Quick Exit', command=exit)
        self.toolsmenu = tk.Menu(self.menubar, tearoff=0)
        self.toolsmenu.add_command(label='Show Message')
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='About', command=self.about)
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.toolsmenu, label='Tools')
        self.menubar.add_cascade(menu=self.helpmenu, label='Help')
        self.root.config(menu=self.menubar)
        self.text.grid(row=0, column=1, sticky="nsew")

        self.root.protocol('WM_DELETE_WINDOW', self.onclose)
        self.root.mainloop()


    def open_file(self):
        self.filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not self.filepath:
            return
        self.text.delete("1.0", tk.END)
        with open(self.filepath, mode="r", encoding="utf-8") as self.input_file:
            self.filetext = self.input_file.read()
            self.text.insert(tk.END, self.filetext)
        self.root.title(f"SMPad - {self.filepath}")

    def save_file(self):
        self.filepath = asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
        if not self.filepath:
            return
        with open(self.filepath, mode="w", encoding="utf-8") as self.output_file:
            self.edtext = self.text.get("1.0", tk.END)
            self.output_file.write(self.edtext)
        self.root.title(f"SMPad - {self.filepath}")

    def about(self):
        messagebox.showinfo(title='About', message='SMPad version 1.0')

    def clear(self):
        self.text.delete('1.0', tk.END)

    def onclose(self):
        if messagebox.askyesno(title='Quit?', message='Want to go?'):   
            self.root.destroy()
    
mygui()