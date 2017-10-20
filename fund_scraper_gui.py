#!/usr/bin/python

import tkinter as tk
from tkinter import ttk


class fund_manager(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        #main fund table
        self.fund_tree = tk.ttk.Treeview(self)
        self.fund_tree['show'] = 'headings'     #remove empty column identifier
        self.fund_tree.pack()
        #define columns here
        self.fund_tree['columns'] = ('isin', 'fund_name', 'nav', 'change')
        self.fund_tree.heading('isin', text = 'ISIN')
        self.fund_tree.column('isin', anchor = 'center')
        self.fund_tree.heading('fund_name', text = 'Fund Name')
        self.fund_tree.column('fund_name', anchor = 'center')
        self.fund_tree.heading('nav', text = 'NAV')
        self.fund_tree.column('nav', anchor = 'center')
        self.fund_tree.heading('change', text = 'Change')
        self.fund_tree.column('change', anchor = 'center')

root = tk.Tk()
root.title('Fund Manager')
app = fund_manager(master = root)
app.mainloop()

