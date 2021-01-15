# import modules
from tkinter import *
import Calebs_Scraper

# configure workspace
ws = Tk()
ws.title("Pagine Bianche Scraper")
ws.geometry('500x500')
ws.configure(bg="#567")

# function territory
def welcome():
    name = nameTf.get()
    my_url2 = ("https://www.paginebianche.it/cerca-da-indirizzo?dv=Modena+" + name.replace(" ", "+" ))
    Calebs_Scraper()
    return Label(ws, text=f'Success! {my_url2}', pady=15, bg='#567').grid(row=2, columnspan=2)
    

# label & Entry boxes territory
nameLb = Label(ws, text="Scrivi l'indirizzo eg: Via Savoniero", pady=15, padx=10, bg='#567')
nameTf = Entry(ws)

# button territory
welBtn = Button(ws, text="Prendi Tutto", command=welcome)

# Position Provide territory
nameLb.grid(row=0, column=0)
nameTf.grid(row=0, column=1)
welBtn.grid(row=1, columnspan=2)

# infinite loop 
ws.mainloop()