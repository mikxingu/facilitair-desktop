from models import Stocks
import tkinter as tk

def add_stock(ticker, year, view, med_price, stock_qty):
    info = Stocks.get_stock_info(ticker, year)
    
    info_list = list(info)
    
    if (med_price or not med_price == 0.0):
        info_list.append(med_price)

    else:
        med_price = info_list[2]
        info_list.append(med_price)

    if (stock_qty):
        info_list.append(stock_qty)

    details = f'{stock_qty} AÇÕES {ticker} COM PREÇO MÉDIO DE {med_price} POR AÇÃO'
    
    info_list.append(details)

    view.insert('', tk.END, values=info_list)
    