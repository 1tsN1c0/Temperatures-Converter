"""
***************************
**                       **
**       © 1tsN1c0       **
**                       **
***************************
"""

from tkinter import *
from tkinter import messagebox

const1 = 1.8
const2 = 32
const3 = 273.15
const4 = 459.67
const5 = 5/9

window = Tk()
window.geometry("630x630")
window.title("Converter")
window.resizable(False, False)
window.configure(background="#2f4f4f")

l = Label(window, text="TEMPERATURES CONVERTER", font=("Helvetica 27 bold"), fg="#00bfff", bg="#2f4f4f")
l.grid(row=0, column=0)

l1 = Label(window, text="Scegli il tipo di conversione che vuoi effettuare.", font=("Helvetica 20 bold"), fg="red", bg="#2f4f4f")
l1.grid(row=1, column=0)

def dacelsius_afahreneit():
    tc = user_input.get()
    tf = (tc * const1) + const2    
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Celsius equivalgono a {} gradi Fahreneit.".format(tc, tf))

def dacelsius_akelvin():
    tc = user_input.get()
    tk = tc + const3    
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Celsius equivalgono a {} gradi Fahreneit.".format(tc, tk))

def dakelvin_acelsius():
    tk = user_input.get()
    tc = tk - const3
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Kelvin equivalgono a {} gradi Celsius.".format(tk, tc))

def dakelvin_afahreneit():
    tk = user_input.get()
    tf = (tk - const3) * const1 + const2   
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Kelvin equivalgono a {} gradi Fahreneit.".format(tk, tf))

def dafahreneit_acelsius():
    tf = user_input.get()
    tc = (tf - const2) * const5   
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Fahreneit equivalgono a {} gradi Celsius.".format(tf, tc))
    
def dafahreneit_akelvin():
    tf = user_input.get()
    tk = (tf - const2) * const5 + const3 
    messagebox.showinfo(title="Operazione Riuscita!", message="{} gradi Fahreneit equivalgono a {} gradi Kelvin.".format(tf, tk))

user_input = IntVar()
t1 = Entry(window, textvariable=user_input, font=("Century Gothic", 14))
t1.grid(row=2, column=0, padx=5, pady=10)

#Codice dei Pulsanti

b1 = Button(window, command=dacelsius_afahreneit, text="Da Celsius a Fahreneit", font=("Comic Sans MS", 14, "bold"))
b1.grid(row=3, column=0, padx=200, pady=10, sticky=W)

b2 = Button(window, command=dacelsius_akelvin, text="Da Celsius a Kelvin", font=("Comic Sans MS", 14, "bold"))
b2.grid(row=4, column=0, padx=220, pady=10, sticky=W)

b3 = Button(window, command=dafahreneit_acelsius, text="Da Fahreneit a Celsius", font=("Comic Sans MS", 14, "bold"))
b3.grid(row=5, column=0, padx=200, pady=10, sticky=W)

b4 = Button(window, command=dafahreneit_akelvin, text="Da Fahreneit a Kelvin", font=("Comic Sans MS", 14, "bold"))
b4.grid(row=6, column=0, padx=205, pady=10, sticky=W)

b5 = Button(window, command=dakelvin_acelsius, text="Da Kelvin a Celsius", font=("Comic Sans MS", 14, "bold"))
b5.grid(row=7, column=0, padx=220, pady=10, sticky=W)

b6 = Button(window, command=dakelvin_afahreneit, text="Da Kelvin a Fahreneit", font=("Comic Sans MS", 14, "bold"))
b6.grid(row=8, column=0, padx=205, pady=10, sticky=W)

if __name__ == "__main__":
    window.mainloop()
