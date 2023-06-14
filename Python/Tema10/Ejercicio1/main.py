import tkinter as tk
from tkinter import ttk

def reiniciar(event):
    opciones.set(None)

window=tk.Tk()

encabezado=ttk.Label(window,text='Elija una bebida')
opciones=tk.StringVar()
op1=ttk.Radiobutton(window,text='Agua',value='1',variable=opciones)
op2=ttk.Radiobutton(window,text='Zumo',value='2',variable=opciones)
op3=ttk.Radiobutton(window,text='Refresco',value='3',variable=opciones)
op4=ttk.Radiobutton(window,text='Cerveza',value='4',variable=opciones)
op5=ttk.Radiobutton(window,text='Vino',value='5',variable=opciones)

encabezado.grid(column=0,row=0,sticky=tk.E,padx=5,pady=5)
op1.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
op2.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)
op3.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)
op4.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)
op5.grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)

boton=tk.Button(window,text='Reinicio')
boton.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)
boton.bind('<Button-1>',reiniciar)

window.mainloop()