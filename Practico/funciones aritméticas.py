import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def sumar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA+numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Sumar A y B", command=sumar)
botonTransportar.place(x=0,y=90)


ventana.mainloop()


#Resta
import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def restar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA-numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Restar A y B", command=restar)
botonTransportar.place(x=0,y=90)


ventana.mainloop()

#Multiplicacion

import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def multiplicacion():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA*numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Multiplicar A y B", command=multiplicacion)
botonTransportar.place(x=0,y=90)


ventana.mainloop()

#Division
import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def Division():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA/numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Dividir A y B", command=Division)
botonTransportar.place(x=0,y=90)


ventana.mainloop()
