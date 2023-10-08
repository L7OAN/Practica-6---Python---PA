import tkinter as tk
from tkinter import messagebox
import re

def guardar_datos():
    # Obtener los datos de los campos
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    edad = entry_edad.get()
    estatura = entry_estatura.get()
    telefono = entry_telefono.get()

    # Obtener el género seleccionado
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
        
    #Validar que los campos tengan el formato correcto
    if (es_entero_valido(edad) and es_decimal_valido(estatura) and 
        es_entero_valido_de_10_digitos(telefono) and es_texto_valido(nombres) and es_texto_valido(apellidos)):
        # Crear una cadena con los datos
        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad} años\nEstatura: {estatura} cm\nTeléfono: {telefono}\nGénero: {genero}"

        # Guardar los datos en un archivo de texto
        with open("Datospython.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
    
        # Mostrar un mensaje con los datos capturados
        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)
    
        # Limpiar los controles después de guardar
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos validos en lols campos.")
        
def limpiar_campos():
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)
    
def es_entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
def es_entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def es_texto_valido(valor):
    return bool(re.Match("^[a-zA-Z\s]+$", valor))

# Crear la ventana principal
app = tk.Tk()
app.title("Formulario")

# Crear variables para los RadioButtons
var_genero = tk.IntVar()

# Crear etiquetas y campos de entrada
label_nombres = tk.Label(app, text="Nombres:")
label_nombres.pack()
entry_nombres = tk.Entry(app)
entry_nombres.pack()

label_apellidos = tk.Label(app, text="Apellidos:")
label_apellidos.pack()
entry_apellidos = tk.Entry(app)
entry_apellidos.pack()

label_edad = tk.Label(app, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(app)
entry_edad.pack()

label_estatura = tk.Label(app, text="Estatura (cm):")
label_estatura.pack()
entry_estatura = tk.Entry(app)
entry_estatura.pack()

label_telefono = tk.Label(app, text="Teléfono:")
label_telefono.pack()
entry_telefono = tk.Entry(app)
entry_telefono.pack()

label_genero = tk.Label(app, text="Género:")
label_genero.pack()

rb_hombre = tk.Radiobutton(app, text="Hombre", variable=var_genero, value=1)
rb_hombre.pack()

rb_mujer = tk.Radiobutton(app, text="Mujer", variable=var_genero, value=2)
rb_mujer.pack()

#Boton para guardar datos
btn_guardar = tk.Button(app, text="Guardar", command=guardar_datos)
btn_guardar.pack()

#Boton para borrar campos
btn_borrar = tk.Button(app, text="Borrar Campos", command=limpiar_campos)
btn_borrar.pack()

# Iniciar la aplicación
app.mainloop()