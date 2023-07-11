"""
Enunciado del ejercicio:
    En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""
import tkinter as tk
from tkinter import ttk

def reiniciar(event):
    opcionesColor.set(None)
    opcionesTapiceria.set(None)
    opcionesPropulsion.set(None)

window=tk.Tk()
window.title('Coche nuevo')
window.geometry('800x300')



encabezado=ttk.Label(window,text='Hola, comencemos con la personalización de su coche ',background='sky blue',foreground='black')
encabezado.grid(column=1,sticky=tk.W,padx=5,pady=5)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(3,weight=1)
window.rowconfigure(10,weight=4)

opcionesColor=tk.StringVar()
encabezadoColor=ttk.Label(window,text='Elija el color del coche')
encabezadoColor.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
opc1=ttk.Radiobutton(window,text='Blanco',value='1',variable=opcionesColor)
opc2=ttk.Radiobutton(window,text='Negro',value='2',variable=opcionesColor)
opc3=ttk.Radiobutton(window,text='Azul',value='3',variable=opcionesColor)
opc4=ttk.Radiobutton(window,text='Rojo',value='4',variable=opcionesColor)
opc5=ttk.Radiobutton(window,text='Verde',value='5',variable=opcionesColor)
opc1.grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)
opc2.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)
opc3.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)
opc4.grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)
opc5.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)

opcionesTapiceria=tk.StringVar()
encabezadoColor=ttk.Label(window,text='Elija la tapicería')
encabezadoColor.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)
opt1=ttk.Radiobutton(window,text='Cuero',value='1',variable=opcionesTapiceria)
opt2=ttk.Radiobutton(window,text='Paño de tela',value='2',variable=opcionesTapiceria)
opt3=ttk.Radiobutton(window,text='Microfibra',value='3',variable=opcionesTapiceria)
opt4=ttk.Radiobutton(window,text='Polipiel',value='4',variable=opcionesTapiceria)
opt5=ttk.Radiobutton(window,text='Vinilo',value='5',variable=opcionesTapiceria)
opt1.grid(column=1,row=2,sticky=tk.W,padx=5,pady=5)
opt2.grid(column=1,row=3,sticky=tk.W,padx=5,pady=5)
opt3.grid(column=1,row=4,sticky=tk.W,padx=5,pady=5)
opt4.grid(column=1,row=5,sticky=tk.W,padx=5,pady=5)
opt5.grid(column=1,row=6,sticky=tk.W,padx=5,pady=5)

opcionesPropulsion=tk.StringVar()
encabezadoColor=ttk.Label(window,text='Elija el sistema de propulsión')
encabezadoColor.grid(column=2,row=1,sticky=tk.W,padx=5,pady=5)
opp1=ttk.Radiobutton(window,text='Térmico',value='1',variable=opcionesPropulsion)
opp2=ttk.Radiobutton(window,text='Eléctrico',value='2',variable=opcionesPropulsion)
opp3=ttk.Radiobutton(window,text='Híbrido',value='3',variable=opcionesPropulsion)
opp4=ttk.Radiobutton(window,text='Pila de hidrógeno',value='4',variable=opcionesPropulsion)
opp1.grid(column=2,row=2,sticky=tk.W,padx=5,pady=5)
opp2.grid(column=2,row=3,sticky=tk.W,padx=5,pady=5)
opp3.grid(column=2,row=4,sticky=tk.W,padx=5,pady=5)
opp4.grid(column=2,row=5,sticky=tk.W,padx=5,pady=5)

boton=tk.Button(window,text='Reiniciar')
boton.grid(column=0,rows=10,sticky=tk.SW,padx=5,pady=5)
boton.bind('<Button-1>',reiniciar)

window.mainloop()
