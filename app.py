from pydoc import text
from turtle import right
from utils import Colors
from models import Stocks
from controllers import StockController

import tkinter as tk
from tkinter import Button, ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # default window size
        window_width = 800
        window_height = 600

        # Get system current screen size
        screen_width = self.winfo_screenwidth
        screen_height = self.winfo_screenheight

        # find the center point
        # center_x = int(screen_width / 2 - window_width / 2)
        # center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}')#{center_x}+{center_y}')

        self.title('FacilitaIR')
        self.configure(background=Colors.c0_powder_blue)
        
        messagebox.showinfo('Disclaimer', 'Essa aplicação utiliza como fonte dados disponíveis na internet. Conferir os dados é sempre importante!')

        # Stocks Tree View
        columns = ('ticker', 'cnpj','company_name', 'year_price', 'medium_price', 'stock_quantity', 'details')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('ticker', text='Ticker')
        tree.heading('cnpj', text='CNPJ')
        tree.heading('company_name', text='Razão Social')
        tree.heading('year_price', text='Fechamento Anual')
        tree.heading('medium_price', text='Preço Médio')
        tree.heading('stock_quantity', text='Quantidade de ações')
        tree.heading('details', text='Discriminação')
        


        stocks = []

        # for n in range(1,10):
        #     stocks.append((f'ABC3 {n}', f'00.100.000/0001-0{n}', f'R${n}'))

        for stock in stocks:
            tree.insert('', tk.END, values=stock)

        # tree.bind('<<TreeviewSelect>>', item_selected(tree, tree.event_info()))
        tree.grid(row=0, column=0,sticky='nsew')
        tree.pack()

        string_var = tk.StringVar()
        stocks_label = tk.Label(self, text='Ticker')
        stocks_label.pack()

        stocks_box = ttk.Combobox(self, textvariable=string_var)
        stocks_box.pack()


        year_var = tk.IntVar()
        year_label = tk.Label(self, text='Ano')
        year_label.pack()
        year_box = ttk.Combobox(self, textvariable=year_var)
        year_box.pack()

        year_box['values'] = ('2021', '2022')
        stocks_box['values'] = Stocks.fetch_stock_tickers()

        label_medium_price = tk.Label(self, text='Preço médio')
        label_medium_price.pack()

        medium_price_var = tk.DoubleVar()

        entry_medium_price = tk.Entry(self,textvariable=medium_price_var, justify='left', relief='solid')
        entry_medium_price.pack()

        label_stock_quantity = tk.Label(self, text='Qtde Ações')
        label_stock_quantity.pack()

        stock_quantity_var = tk.IntVar()
        entry_stock_quantity = tk.Entry(self,textvariable=stock_quantity_var, justify='left', relief='solid')
        entry_stock_quantity.pack()


        button_add_stock = Button(self, command=lambda: StockController.add_stock(stocks_box.get(), year_box.get(), tree, entry_medium_price.get(), entry_stock_quantity.get()), text="+")
        button_add_stock.pack()

        # Quit Button
        button_quit = Button(self, command=quit, text="Fechar", width=8)
        button_quit.pack()

        self.state('zoomed')

    
if __name__ == '__main__':
    app = App()
    app.mainloop()
