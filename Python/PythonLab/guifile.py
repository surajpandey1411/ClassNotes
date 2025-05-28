import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        self.text_area = tk.Text(master)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.filename = None
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As...", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

    def new_file(self):
         self.filename = None
         self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "r") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
root = tk.Tk()
editor = TextEditor(root)
root.mainloop()