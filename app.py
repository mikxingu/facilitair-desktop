from utils import Colors

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
        
        # Stocks Tree View
        columns = ('ticker', 'cnpj', 'year_price')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('ticker', text='Ticker')
        tree.heading('cnpj', text='CNPJ')
        tree.heading('year_price', text='Fechamento')

        stocks = []

        for n in range(1,10):
            stocks.append((f'ABC3 {n}', f'00.100.000/0001-0{n}', f'R${n}'))

        for stock in stocks:
            tree.insert('', tk.END, values=stock)

        tree.bind('<<TreeviewSelect>>', item_selected(tree, tree.event_info()))
        tree.grid(row=0, column=0,sticky='nsew')
        tree.pack()

        # Quit Button
        button_quit = Button(self, command=quit, text="Fechar", width=8)
        button_quit.pack()

    

def item_selected(tree: ttk.Treeview, event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            messagebox.showinfo(title='Info', message='testing'.join(record))

if __name__ == '__main__':
    app = App()
    app.mainloop()
