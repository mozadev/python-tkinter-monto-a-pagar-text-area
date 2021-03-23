import tkinter
from tkinter import messagebox


def calcular():
    numero_unidades = txtnumero1.get()

    if (len(numero_unidades) == 0):
        messagebox.showinfo(message="Ingrese Unidades !!", title="Mensaje")
        txtnumero1.focus()

    else:
        numero_unidades = int(numero_unidades)

        if 1 <= numero_unidades <= 20:
            precio_unitario = 29.5
            descuento = 0.04 * precio_unitario * numero_unidades

        elif numero_unidades >= 21 and numero_unidades <= 40:
            precio_unitario = 27.5
            descuento = 0.04 * precio_unitario * numero_unidades

        elif numero_unidades >= 41 and numero_unidades <= 60:
            precio_unitario = 23.7
            descuento = 0.04 * precio_unitario * numero_unidades

        else:
            precio_unitario = 20.5
            descuento = 0.12 * precio_unitario * numero_unidades

        monto_compra = precio_unitario * numero_unidades
        monto_cancelar = monto_compra - descuento

        area.insert(1.0, "\nEl monto de compra es : {}".format(monto_compra))
        area.insert(1.0, "\nEl monto a cancelar  es : {}".format(monto_cancelar))
        area.insert(1.0, "\nEl descuento es : {}".format(descuento))


ventana = tkinter.Tk()  # instancia del formulario
ventana.title("Ventana Principal")
ventana.geometry("600x500")
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='Ingrese Unidades')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=200, y=50)

boton = tkinter.Button(ventana, text="Calcular", command=calcular)
boton.place(x=200, y=120)

area = tkinter.Text(ventana)
area.config(width=50, height=10)
area.place(x=100, y=150)
# paises=tkinter.StringVar(ventana)
# paises.set("--------------")
# combo=tkinter.OptionMenu(ventana,paises,"--------------","Peru","Chile","Mexico")
# combo.place(x=100,y=400)
ventana.mainloop()  # ejecutando formulario
