import tkinter as tk
import tkinter.ttk as ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        self.root.geometry("400x300")

        self.password_length = tk.StringVar()
        self.include_special_chars = tk.BooleanVar()
        self.password_result = tk.StringVar()

        self.create_widgets()
        self.set_indigo_theme()

    def generate_password(self):
        length = int(self.password_length.get())
        include_special_chars = self.include_special_chars.get()

        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for i in range(length))
        self.password_result.set(password)

        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)  # Limpiamos el contenido anterior
        self.result_text.insert(tk.END, '*' * len(password), 'bold_center')  # Insertamos la contraseña generada con asteriscos
        self.result_text.config(state='disabled')

    def copy_password(self):
        password = self.password_result.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)

    def clear_inputs(self):
        self.password_length.set("")
        self.include_special_chars.set(False)
        self.password_result.set("Aquí aparecerá la contraseña generada")
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')

    def create_widgets(self):
        length_label = tk.Label(self.root, text="Longitud de la contraseña:")
        length_label.pack()

        length_entry = tk.Entry(self.root, textvariable=self.password_length)
        length_entry.pack()

        special_chars_checkbutton = tk.Checkbutton(self.root, text="Incluir caracteres especiales", variable=self.include_special_chars)
        special_chars_checkbutton.pack()

        generate_button = tk.Button(self.root, text="Generar Contraseña", command=self.generate_password)
        generate_button.pack()

        result_label = tk.Label(self.root, text="Contraseña generada:")
        result_label.pack()

        self.result_text = tk.Text(self.root, height=1, state='disabled')
        self.result_text.pack()

        self.password_result.set("Aquí aparecerá la contraseña generada")
        self.result_text.tag_configure('bold_center', font=('Helvetica', 12, 'bold'), justify='center')  # Configuramos el estilo para el texto en negrita y centrado
        self.result_text.insert(tk.END, self.password_result.get(), 'bold_center')

        # Agregamos el menú contextual (click derecho) al widget Text
        self.context_menu = tk.Menu(self.result_text, tearoff=0)
        self.context_menu.add_command(label="Copiar", command=self.copy_password)
        self.result_text.bind("<Button-3>", self.show_context_menu)

        copy_button = tk.Button(self.root, text="Copiar Contraseña", command=self.copy_password)
        copy_button.pack()

        clear_button = tk.Button(self.root, text="Generar Otra Contraseña", command=self.clear_inputs)
        clear_button.pack()

        exit_button = tk.Button(self.root, text="SALIR", command=self.root.quit)
        exit_button.pack()

    def set_indigo_theme(self):
        # Establecemos el esquema de color a indigo
        indigo = "#4B0082"
        self.root.configure(background=indigo)
        ttk_style = ttk.Style()
        ttk_style.theme_use('default')  # Reseteamos cualquier tema anterior
        ttk_style.configure(".", background=indigo, foreground="white", fieldbackground=indigo)
        ttk_style.map("TCombobox", fieldbackground=[("readonly", indigo)])
        ttk_style.map("TCombobox", selectbackground=[("readonly", indigo)])
        ttk_style.map("TCombobox", selectforeground=[("readonly", "white")])

    def show_context_menu(self, event):
        self.context_menu.tk_popup(event.x_root, event.y_root)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()