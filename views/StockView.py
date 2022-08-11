from doctest import master
import tkinter as tk
from tkinter import ttk


class View():
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.stockPanel = StockPanel(master)


class StockPanel():
    def __init__(self, root):

        self.framePanel = tk.Frame(root)
        self.framePanel.pack()

        self.label = tk.Label(self.framePanel, text='Test')
        self.label.pack()

        

    def create_tree_widget(self):
        columns = ('ticker', 'price_year', 'cnpj')
        tree = ttk.Treeview(columns=columns,show='headings')

        tree.heading('ticker', text='Ticker')
        tree.heading('price_year', text='Preço Fechamento')
        tree.heading('cnpj', text='CNPJ')
