from views import Colors

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

        button_quit = Button(self, command=quit, text="Fechar", width=8)
        button_quit.place(x=300, y=500)


if __name__ == '__main__':
    app = App()
    app.mainloop()
