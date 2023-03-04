from tkinter import *
from tkinter import ttk
import math

def ingresarvalores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '-' or tecla == '+':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')
    
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarvaloresTeclado(event):
    tecla = event.char

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '-' or tecla == '+':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == '-':
            entrada1.set(entrada2.get() + '-')

        entrada2.set('')
    
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raizCuadrada():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def potencia():
    entrada1.set(entrada2.get() + '^')
    resultado = math.pow(entrada1, entrada2)
    entrada2.set(resultado)

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio: final-1])

def borrarTodo(*args):
    entrada1.set('')
    entrada2.set('')

#creacion de la ventana
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#010924")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#Estilos Labels
estilo_label1 =ttk.Style()
estilo_label1.configure('label1.TLabel', font = "arial 18", anchor ="e", background="#010924", foreground="white")

estilo_label2 =ttk.Style()
estilo_label2.configure('label2.TLabel', font = "arial 42", anchor ="e", background="#010924", foreground="white")

entrada1 = StringVar()
label_1 =ttk.Label(mainframe, textvariable=entrada1, style="label1.TLabel")
label_1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada2 = StringVar()
label_2 = ttk.Label(mainframe, textvariable=entrada2, style="label2.TLabel")
label_2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

#estilo de los btns
estilo_btns =ttk.Style()
estilo_btns.configure('Btns_numeros.TButton', font = "arial 22", width=5, background ="#00044A", foreground="white", relief ="flat")
estilo_btns.map('Btns_numeros.TButton', foreground=[('active', '#020A90')])

estilo_btnBorrar =ttk.Style()
estilo_btnBorrar.configure('Btn_borrar.TButton', font = "arial 22", width=5, background ="#010924", foreground="white", relief ="flat")
estilo_btnBorrar.map('Btn_borrar.TButton', foreground=[('active', '#000AB1')], backgroung=[('active', '#000AB1')])

estilo_btnsRestantes =ttk.Style()
estilo_btnsRestantes.configure('Btns_restantes.TButton', font = "arial 22", width=5, background ="#010924", foreground="white", relief ="flat")
estilo_btnsRestantes.map('Btns_restantes.TButton', foreground=[('active', '#000AB1')])

#Creacion de btns
Btn0 = ttk.Button(mainframe, text="0", style="Btns_numeros.TButton", command= lambda: ingresarvalores('0'))
Btn1 = ttk.Button(mainframe, text="1", style="Btns_numeros.TButton", command= lambda: ingresarvalores('1'))
Btn2 = ttk.Button(mainframe, text="2", style="Btns_numeros.TButton", command= lambda: ingresarvalores('2'))
Btn3 = ttk.Button(mainframe, text="3", style="Btns_numeros.TButton", command= lambda: ingresarvalores('3'))
Btn4 = ttk.Button(mainframe, text="4", style="Btns_numeros.TButton", command= lambda: ingresarvalores('4'))
Btn5 = ttk.Button(mainframe, text="5", style="Btns_numeros.TButton", command= lambda: ingresarvalores('5'))
Btn6 = ttk.Button(mainframe, text="6", style="Btns_numeros.TButton", command= lambda: ingresarvalores('6'))
Btn7 = ttk.Button(mainframe, text="7", style="Btns_numeros.TButton", command= lambda: ingresarvalores('7'))
Btn8 = ttk.Button(mainframe, text="8", style="Btns_numeros.TButton", command= lambda: ingresarvalores('8'))
Btn9 = ttk.Button(mainframe, text="9", style="Btns_numeros.TButton", command= lambda: ingresarvalores('9'))

Btn_borrar = ttk.Button(mainframe, text=chr(9003), style="Btn_borrar.TButton", command= lambda: borrar())
Btn_borrarTodo = ttk.Button(mainframe, text="C", style="Btn_borrar.TButton", command= lambda:borrarTodo())
Btn_parentesis1 = ttk.Button(mainframe, text="(", style="Btns_restantes.TButton", command= lambda: ingresarvalores('('))
Btn_parentesis2 = ttk.Button(mainframe, text=")", style="Btns_restantes.TButton", command= lambda: ingresarvalores(')'))
Btn_punto = ttk.Button(mainframe, text=".", style="Btns_restantes.TButton", command= lambda: ingresarvalores('.'))

Btn_division = ttk.Button(mainframe, text="/", style="Btns_restantes.TButton", command= lambda: ingresarvalores('/'))
Btn_multiplicacion = ttk.Button(mainframe, text="X", style="Btns_restantes.TButton", command= lambda: ingresarvalores('*'))
Btn_resta = ttk.Button(mainframe, text="-", style="Btns_restantes.TButton", command= lambda: ingresarvalores('-'))
Btn_suma = ttk.Button(mainframe, text="+", style="Btns_restantes.TButton", command= lambda: ingresarvalores('+'))
Btn_raizCuadrada = ttk.Button(mainframe, text="√", style="Btns_restantes.TButton", command= lambda: raizCuadrada())
Btn_potencia = ttk.Button(mainframe, text="^", style="Btns_restantes.TButton", command= lambda: potencia())
Btn_igual = ttk.Button(mainframe, text="=", style="Btns_restantes.TButton", command= lambda: ingresarvalores('='))

#posicion de btns en pantalla
Btn_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
Btn_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
Btn_borrarTodo.grid(column=2, row=2, sticky=(W, N, E, S))
Btn_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

Btn7.grid(column=0, row=3, sticky=(W, N, E, S))
Btn8.grid(column=1, row=3, sticky=(W, N, E, S))
Btn9.grid(column=2, row=3, sticky=(W, N, E, S))
Btn_division.grid(column=3, row=3, sticky=(W, N, E, S))

Btn4.grid(column=0, row=4, sticky=(W, N, E, S))
Btn5.grid(column=1, row=4, sticky=(W, N, E, S))
Btn6.grid(column=2, row=4, sticky=(W, N, E, S))
Btn_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

Btn1.grid(column=0, row=5, sticky=(W, N, E, S))
Btn2.grid(column=1, row=5, sticky=(W, N, E, S))
Btn3.grid(column=2, row=5, sticky=(W, N, E, S))
Btn_resta.grid(column=3, row=5, sticky=(W, N, E, S))

Btn0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
Btn_punto.grid(column=2, row=6, sticky=(W, N, E, S))
Btn_suma.grid(column=3, row=6, sticky=(W, N, E, S))

Btn_igual.grid(column=0, row=7,columnspan=2, sticky=(W, N, E, S))
Btn_potencia.grid(column=2, row=7, sticky=(W, N, E, S))
Btn_raizCuadrada.grid(column=3, row=7, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<Key>', ingresarvaloresTeclado)
root.bind('<KeyPress-m>', borrar)
root.bind('<KeyPress-c>', borrarTodo)

root.mainloop()