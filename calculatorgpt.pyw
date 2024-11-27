from tkinter import Tk, Frame, Button, Label, StringVar

# Función para actualizar el texto del Label
def actualizar_texto(valor): 
    contenido_actual = texto.get()
    texto.set(contenido_actual + str(valor))

# Función para evaluar la operación
def calcular():
    try:
        resultado = eval(texto.get().replace('x', '*').replace('÷', '/'))
        texto.set(str(resultado))
    except Exception as e:
        texto.set("Error")

# Inicializar la ventana
ventana = Tk()
ventana.title("Calc Frame")
ventana.geometry("300x350")

# Variable dinámica para mostrar el contenido
texto = StringVar()
texto.set("")

# Crear el Frame superior y el Label
frame_0 = Frame(ventana, bg="grey")
frame_0.place(x=0, y=0, height=45, width=300)
lbl0 = Label(frame_0, text="Casio FX100MS", fg="brown", bg="black", height=2)
lbl0.pack()

frame_1 = Frame(ventana, bg="dark green")
frame_1.place(x=30, y=60, height=35, width=240)
lbl_display = Label(frame_1, textvariable=texto, fg="white", bg="dark green", font=("Arial", 14), anchor="e")
lbl_display.pack(fill="both")

# Crear botones y asignar sus comandos
btns = [
    (0, 50, 140), (1, 90, 140), (2, 130, 140), (3, 170, 140),
    (4, 50, 180), (5, 90, 180), (6, 130, 180), (7, 170, 180),
    (8, 50, 220), (9, 90, 220), (",", 130, 220), ("+", 220, 140),
    ("-", 260, 140), ("x", 220, 180), ("÷", 260, 180), ("C", 170, 220),
    ("=", 220, 220)
]

for b in btns:
    if b[0] == "=":
        btn = Button(ventana, text=b[0], fg="white", bg="green", command=calcular)
    elif b[0] == "C":
        btn = Button(ventana, text=b[0], fg="white", bg="red", command=lambda: texto.set(""))
    else:
        btn = Button(ventana, text=b[0], fg="white", bg="black", command=lambda val=b[0]: actualizar_texto(val))
    btn.place(x=b[1], y=b[2], height=25, width=25)

ventana.mainloop()
