import tkinter as tk
from tkinter import messagebox
from Usuarios import usuario
from menus import *  # Asegúrate de que este archivo tenga las funciones mostrar_menu_ropa, mostrar_menu_tenis, etc.
from ConectarBD import *  # Si necesitas importar algo relacionado con la base de datos

# Funciones para el registro y el inicio de sesión
def validar_login():
    email = entry_email.get()
    password = entry_password.get()
    obj_usuario = usuario.Usuario("", "", email, password)
    registro = obj_usuario.iniciar_sesion(email, password)
    if registro:
        ventana_login.destroy()  # Cierra la ventana de login
        mostrar_menu_principal()
    else:
        messagebox.showerror("Error", "Nombre de usuario y/o contraseña incorrectos. Inténtalo de nuevo.")

def abrir_login():
    global ventana_login, entry_email, entry_password
    ventana_login = tk.Toplevel(ventana_principal)
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry('600x400')
    ventana_login.configure(background='lightgreen')

    tk.Label(ventana_login, text="Correo", font=("Skull and void", 16), width=14, height=1, anchor='center').pack(padx=2, pady=2, anchor='center')
    entry_email = tk.Entry(ventana_login, font=("Arial", 13))
    entry_email.pack(padx=20, pady=10, anchor='center')

    tk.Label(ventana_login, text="Contraseña", font=("Skull and void", 16), width=14, height=1, anchor='center').pack(padx=2, pady=2, anchor='center')
    entry_password = tk.Entry(ventana_login, font=("Arial", 13), show='*')
    entry_password.pack(padx=20, pady=10, anchor='center')

    tk.Button(ventana_login, text="Iniciar Sesión", font=("Skull and void", 10), width=15, height=1, command=validar_login).pack(padx=20, pady=10, anchor='center')

def abrir_registro():
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry('350x500')
    ventana_registro.configure(background='lightgreen')

    tk.Label(ventana_registro, text="Nombre", font=("Skull and void", 16), width=14, height=1, anchor='w').pack(padx=2, pady=2, anchor='w')
    entry_nombre = tk.Entry(ventana_registro, font=("Arial", 13))
    entry_nombre.pack(padx=20, pady=10, anchor='w')

    tk.Label(ventana_registro, text="Apellido", font=("Skull and void", 16), width=14, height=1, anchor='w').pack(padx=2, pady=2, anchor='w')
    entry_apellido = tk.Entry(ventana_registro, font=("Arial", 13))
    entry_apellido.pack(padx=20, pady=10, anchor='w')

    tk.Label(ventana_registro, text="Correo", font=("Skull and void", 16), width=14, height=1, anchor='w').pack(padx=20, pady=10, anchor='w')
    entry_email_registro = tk.Entry(ventana_registro, font=("Arial", 13))
    entry_email_registro.pack(padx=20, pady=10, anchor='w')

    tk.Label(ventana_registro, text="Contraseña", font=("Skull and void", 16), width=14, height=1, anchor='w').pack(padx=20, pady=10, anchor='w')
    entry_password_registro = tk.Entry(ventana_registro, font=("Arial", 13), show='*')
    entry_password_registro.pack(padx=20, pady=10, anchor='w')

    def registrar_usuario():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        email = entry_email_registro.get()
        password = entry_password_registro.get()
        obj_usuario = usuario.Usuario(nombre, apellido, email, password)
        resultado = obj_usuario.registrar()
        if resultado:
            messagebox.showinfo("Registro", f"{nombre} {apellido} se registró correctamente.")
            ventana_registro.destroy()
        else:
            messagebox.showerror("Error", "No fue posible registrar el usuario. Inténtalo de nuevo.")

    tk.Button(ventana_registro, text="Registrar", font=("Skull and void", 16), width=15, height=1, command=registrar_usuario).pack(padx=1, pady=10, side="left")

def mostrar_menu_principal():
    ventana_principal.withdraw()  # Ocultar la ventana de login
    menu_ventana = tk.Toplevel()
    menu_ventana.title("Menú Principal - Tienda Skate")
    menu_ventana.geometry('1920x1080')
    menu_ventana.configure(background='lightgreen')

    tk.Label(menu_ventana, text="Menú Principal", font=("Skull and void", 16)).pack(padx=2, pady=2)
    tk.Button(menu_ventana, text="Ropa", width=30, height=2, command=mostrar_menu_ropa).pack(padx=2, pady=2)
    tk.Button(menu_ventana, text="Tenis", width=30, height=2, command=mostrar_menu_tenis).pack(padx=2, pady=2)
    tk.Button(menu_ventana, text="Skateboard", width=30, height=2, command=mostrar_menu_skateboard).pack(padx=2, pady=2)
    tk.Button(menu_ventana, text="Accesorios", width=30, height=2, command=mostrar_menu_accesorios).pack(padx=2, pady=2)
    tk.Button(menu_ventana, text="Salir", width=30, height=2,command=menu_ventana.destroy).pack(padx=2, pady=2)

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Tienda Skate")
ventana_principal.geometry('1920x1080')
ventana_principal.configure(background='lightgreen')

tk.Label(ventana_principal, text="Tienda Skates", font=("Skull and Void", 20),anchor='center').pack(pady=10)
# Botones en la ventana principal centrados horizontalmente
frame_botones = tk.Frame(ventana_principal)
frame_botones.pack(expand=True)

tk.Button(frame_botones, text="Iniciar Sesión", font=("Skull and void", 14), width=15, height=1, command=abrir_login).pack(side='left', padx=2, pady=2)
tk.Button(frame_botones, text="Agregar Usuario", font=("Skull and void", 14), width=15, height=1, command=abrir_registro).pack(side='left', padx=2, pady=2)

ventana_principal.mainloop()
