import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        self.root.geometry("400x200")

        self.password_length = tk.StringVar()
        self.password_result = tk.StringVar()

        self.create_widgets()

    def generate_password(self):
        length = int(self.password_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        self.password_result.set(password)

    def create_widgets(self):
        length_label = tk.Label(self.root, text="Longitud de la contraseña:")
        length_label.pack()

        length_entry = tk.Entry(self.root, textvariable=self.password_length)
        length_entry.pack()

        generate_button = tk.Button(self.root, text="Generar Contraseña", command=self.generate_password)
        generate_button.pack()

        result_label = tk.Label(self.root, text="Contraseña generada:")
        result_label.pack()

        result_entry = tk.Entry(self.root, textvariable=self.password_result, state='readonly')
        result_entry.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
