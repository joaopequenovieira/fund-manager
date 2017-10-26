#!/usr/bin/python

import tkinter as tk
from tkinter import ttk
import db_manage


def add_new_fund():
    window = tk.Toplevel()
    window.wm_title('Add new fund...')
    link_entry = tk.Entry(window)
    link_entry.pack(fill='x', expand=1)
    #lambda to prevent function being called on assignment
    def add_butt_func():
        db_manage.db_manager.add_fund(db, (link_entry.get()))
        window.destroy()
    add_button = tk.Button(window, text='Add', command=lambda: (add_butt_func()))
    add_button.pack(side='right')
    cancel_button = tk.Button(window, text='Cancel', command=window.destroy)
    cancel_button.pack(side='right')


class fund_manager(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_menu_widget()
        self.create_table_widget()
        self.pack(fill='both', expand=1)


    def create_menu_widget(self):
        #menu bar setup
        self.menubar = tk.Menu(self)
        menubar = self.menubar
        self.master.config(menu=menubar)
        #new submenu
        menu_new = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(menu=menu_new, label='New')
        menu_new.add_command(label='Add New Fund', command=add_new_fund)


    def create_table_widget(self):
        """Create principle fund table"""
        #main fund table
        self.fund_tree = tk.ttk.Treeview(self)
        fund_tree = self.fund_tree
        fund_tree['show'] = 'headings'     #remove empty column identifier
        fund_tree.pack(fill='both', expand=1)
        #define columns here
        fund_tree['columns'] = ('isin', 'fund_name', 'nav', 'change')

        fund_tree.heading('isin', text='ISIN')
        fund_tree.column('isin', anchor='center')

        fund_tree.heading('fund_name', text='Fund Name')
        fund_tree.column('fund_name', anchor='center')

        fund_tree.heading('nav', text='NAV')
        fund_tree.column('nav', anchor='center')

        fund_tree.heading('change', text='Change')
        fund_tree.column('change', anchor='center')



if __name__ == "__main__":
    #initialize database
    db = db_manage.db_manager('fund_manager.db')
    db.load_database()
    
    root = tk.Tk()
    root.attributes('-zoomed', True)
    root.title('Fund Manager')
    app = fund_manager(root)


    root.mainloop()
