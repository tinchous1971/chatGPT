import tkinter as tk
import random
import string

def generate_password():
    length = int(password_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_result.set(password)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")
root.geometry("400x200")

# Variables para la longitud y resultado de la contraseña
password_length = tk.StringVar()
password_result = tk.StringVar()

# Etiqueta e input para la longitud de la contraseña
length_label = tk.Label(root, text="Longitud de la contraseña:")
length_label.pack()
length_entry = tk.Entry(root, textvariable=password_length)
length_entry.pack()

# Botón para generar la contraseña
generate_button = tk.Button(root, text="Generar Contraseña", command=generate_password)
generate_button.pack()

# Etiqueta para mostrar la contraseña generada
result_label = tk.Label(root, text="Contraseña generada:")
result_label.pack()
result_entry = tk.Entry(root, textvariable=password_result, state='readonly')
result_entry.pack()

# Bucle principal de la aplicación
root.mainloop()
