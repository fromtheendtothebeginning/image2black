import tkinter as tk

class Win:
    def __init__(self, name: str, size: str) -> None:
        
        self.win=tk.Tk()
        self.win.title(name)
        self.win.geometry(size)