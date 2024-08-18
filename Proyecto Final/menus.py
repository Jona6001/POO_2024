import tkinter as tk
from tkinter import messagebox,scrolledtext
from ConectarBD import *
from Ropa import ropa
from Tenis import tenis
from Skateboard import skateboard
from Accesorios import accesorios

# Menú de Ropa
def mostrar_menu_ropa():
    ropa_ventana = tk.Toplevel()
    ropa_ventana.title("Menú de Ropa")
    ropa_ventana.geometry('600x450')
    ropa_ventana.configure(background='lightgreen')

    tk.Label(ropa_ventana, text="Menú de Ropa", font=("Skull and void", 12),anchor='center').pack(pady=10)
    tk.Button(ropa_ventana, text="Agregar Ropa",font=("Skull and void", 12), width=30, height=2,anchor='center', command=agregar_ropa).pack(pady=5)
    tk.Button(ropa_ventana, text="Eliminar Stock de Ropa",font=("Skull and void", 12), width=30, height=2,anchor='center', command=eliminar_stock_ropa).pack(pady=5)
    tk.Button(ropa_ventana, text="Eliminar Producto de Ropa",font=("Skull and void", 12), width=30, height=2,anchor='center', command=eliminar_producto_ropa).pack(pady=5)
    tk.Button(ropa_ventana, text="Actualizar Cantidad de Ropa",font=("Skull and void", 12), width=30, height=2,anchor='center', command=actualizar_cantidad_ropa).pack(pady=5)
    tk.Button(ropa_ventana, text="Mostrar Productos de Ropa", font=("Skull and void", 12),width=30, height=2,anchor='center', command=mostrar_inventario_ropa).pack(pady=5)
    tk.Button(ropa_ventana, text="Volver",font=("Skull and void", 10), width=30, height=2,anchor='center', command=ropa_ventana.destroy).pack(pady=20)

def agregar_ropa():
    agregar_ventana = tk.Toplevel()  # Cambiado de Tk() a Toplevel() para abrir una ventana emergente
    agregar_ventana.title("Agregar Ropa")

    # Crear las etiquetas y entradas de texto
    tk.Label(agregar_ventana, text="Nombre").pack()
    entry_nombre = tk.Entry(agregar_ventana)
    entry_nombre.pack()

    tk.Label(agregar_ventana, text="Precio").pack()
    entry_precio = tk.Entry(agregar_ventana)
    entry_precio.pack()

    tk.Label(agregar_ventana, text="Cantidad").pack()
    entry_cantidad = tk.Entry(agregar_ventana)
    entry_cantidad.pack()

    tk.Label(agregar_ventana, text="Talla").pack()
    entry_talla = tk.Entry(agregar_ventana)
    entry_talla.pack()

    tk.Label(agregar_ventana, text="Material").pack()
    entry_material = tk.Entry(agregar_ventana)
    entry_material.pack()

    tk.Label(agregar_ventana, text="Stock Máximo").pack()
    entry_stockMax = tk.Entry(agregar_ventana)
    entry_stockMax.pack()

    tk.Label(agregar_ventana, text="Stock Mínimo").pack()
    entry_stockMin = tk.Entry(agregar_ventana)
    entry_stockMin.pack()

    def procesar_agregar_ropa():
        # Captura de entradas
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        talla = entry_talla.get()
        material = entry_material.get()
        stock_max = entry_stockMax.get()
        stock_min = entry_stockMin.get()

        # Creación del objeto Ropa y agregar a la BD
        obj_Ropa = ropa.Ropa(nombre, precio, cantidad, talla, material, stock_max, stock_min)
        resultado = obj_Ropa.agregar()

        if resultado:
            print(f"\n\tLa ropa {nombre} se registró correctamente")
        else:
            print(f"\n\t** Por favor inténtalo de nuevo, no fue posible agregar ** ...")

    # Botón para procesar la entrada de datos
    tk.Button(agregar_ventana, text="Agregar Ropa", command=procesar_agregar_ropa).pack()

    agregar_ventana.mainloop()

def eliminar_stock_ropa():
    def eliminar():
        try:
            id = int(entry_id.get())
            resultado = ropa.Ropa.eliminarStock(id)
            if resultado:
                messagebox.showinfo("Éxito", f"Se ha eliminado el stock de la ropa con id '{id}'")
            else:
                messagebox.showwarning("Error", "Por favor, inténtalo de nuevo, no fue posible eliminar el stock")
            ventana_eliminar.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido")

    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Stock de Ropa")
    
    label_id = tk.Label(ventana_eliminar, text="Ingrese el ID del producto:")
    label_id.pack(pady=10)
    
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack(pady=10)
    
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar Stock", command=eliminar)
    boton_eliminar.pack(pady=20)

    ventana_eliminar.mainloop()

def eliminar_producto_ropa():
    def eliminar():
        try:
            id = int(entry_id.get())
            resultado = ropa.Ropa.eliminarProducto(id)
            if resultado:
                messagebox.showinfo("Éxito", f"Se ha eliminado la ropa con id '{id}'")
            else:
                messagebox.showwarning("Error", "Por favor, inténtalo de nuevo, no fue posible eliminar el producto")
            ventana_eliminar.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido")

    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Producto de Ropa")
    
    label_id = tk.Label(ventana_eliminar, text="Ingrese el ID del producto que deseas eliminar:")
    label_id.pack(pady=10)
    
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack(pady=10)
    
    boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar Producto", command=eliminar)
    boton_eliminar.pack(pady=20)

    ventana_eliminar.mainloop()

def actualizar_cantidad_ropa():
    def actualizar():
        try:
            id = int(entry_id.get())
            cantidad = int(entry_cantidad.get())
            resultado = ropa.Ropa.actualizarCantidad(id, cantidad)
            if resultado:
                messagebox.showinfo("Éxito", "La cantidad de producto de la ropa se ha actualizado correctamente")
            else:
                messagebox.showwarning("Error", "Ha ocurrido un error al momento de modificar la cantidad de producto")
            ventana_actualizar.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos")

    ventana_actualizar = tk.Toplevel()
    ventana_actualizar.title("Actualizar Cantidad de Ropa")

    label_id = tk.Label(ventana_actualizar, text="Ingrese el ID de la ropa:")
    label_id.pack(pady=10)
    
    entry_id = tk.Entry(ventana_actualizar)
    entry_id.pack(pady=10)
    
    label_cantidad = tk.Label(ventana_actualizar, text="Ingrese la nueva cantidad:")
    label_cantidad.pack(pady=10)
    
    entry_cantidad = tk.Entry(ventana_actualizar)
    entry_cantidad.pack(pady=10)
    
    boton_actualizar = tk.Button(ventana_actualizar, text="Actualizar Cantidad", command=actualizar)
    boton_actualizar.pack(pady=20)

    ventana_actualizar.mainloop()

def mostrar_inventario_ropa():
    ventana_inventario = tk.Toplevel()
    ventana_inventario.title("Mostrar Inventario")

    resultado = ropa.Ropa.mostrarProducto()

    if resultado:
        text_area = tk.Text(ventana_inventario, wrap=tk.WORD, width=100, height=20)
        text_area.pack(pady=20)
        
        for fila in resultado:
            text_area.insert(tk.END, f"ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Cantidad: {fila[3]} | Talla: {fila[4]} | Material: {fila[5]} | Stock Max: {fila[6]} | Stock Min: {fila[7]}\n")

        text_area.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Inventario vacío", "No hay productos en el inventario")
    
    boton_cerrar = tk.Button(ventana_inventario, text="Cerrar", command=ventana_inventario.destroy)
    boton_cerrar.pack(pady=10)

    ventana_inventario.mainloop()

# Menú de Tenis
def mostrar_menu_tenis():
    tenis_ventana = tk.Toplevel()
    tenis_ventana.title("Menú de Tenis")
    tenis_ventana.geometry('600x450')
    tenis_ventana.configure(background='lightgreen')

    tk.Label(tenis_ventana, text="Menú de Tenis", font=("Skull and void", 16)).pack(pady=10)
    tk.Button(tenis_ventana, text="Agregar Tenis", width=30, height=2, command=agregar_teni).pack(pady=5)
    tk.Button(tenis_ventana, text="Eliminar Stock de Tenis", width=30, height=2, command=eliminar_stock_tenis).pack(pady=5)
    tk.Button(tenis_ventana, text="Eliminar Producto de Tenis", width=30, height=2, command=eliminar_tenis).pack(pady=5)
    tk.Button(tenis_ventana, text="Actualizar Cantidad de Tenis", width=30, height=2, command=actualizar_cantidad_tenis).pack(pady=5)
    tk.Button(tenis_ventana, text="Mostrar Productos de Tenis", width=30, height=2, command=mostrar_inventario_tenis).pack(pady=5)
    tk.Button(tenis_ventana, text="Volver", width=30, height=2, command=tenis_ventana.destroy).pack(pady=20)

def agregar_teni():
    def guardar():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        talla = entry_talla.get()
        color = entry_color.get()
        agujetas = entry_agujetas.get()
        stock_max = entry_stock_max.get()
        stock_min = entry_stock_min.get()

        obj_Teni = tenis.Tenis(nombre, precio, cantidad, talla, color, agujetas, stock_max, stock_min)
        resultado = obj_Teni.agregar()
        if resultado:
            messagebox.showinfo("Éxito", f"El teni {nombre} se registró correctamente")
        else:
            messagebox.showerror("Error", "No fue posible agregar el teni. Inténtalo de nuevo.")
        ventana_agregar.destroy()

    ventana_agregar = tk.Tk()
    ventana_agregar.title("Agregar Teni")

    tk.Label(ventana_agregar, text="Nombre del Teni:").pack()
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.pack()

    tk.Label(ventana_agregar, text="Precio del Teni:").pack()
    entry_precio = tk.Entry(ventana_agregar)
    entry_precio.pack()

    tk.Label(ventana_agregar, text="Cantidad del Teni:").pack()
    entry_cantidad = tk.Entry(ventana_agregar)
    entry_cantidad.pack()

    tk.Label(ventana_agregar, text="Talla del Teni:").pack()
    entry_talla = tk.Entry(ventana_agregar)
    entry_talla.pack()

    tk.Label(ventana_agregar, text="Color del Teni:").pack()
    entry_color = tk.Entry(ventana_agregar)
    entry_color.pack()

    tk.Label(ventana_agregar, text="¿Tiene agujetas (Sí/No)?:").pack()
    entry_agujetas = tk.Entry(ventana_agregar)
    entry_agujetas.pack()

    tk.Label(ventana_agregar, text="Stock Máximo del Teni:").pack()
    entry_stock_max = tk.Entry(ventana_agregar)
    entry_stock_max.pack()

    tk.Label(ventana_agregar, text="Stock Mínimo del Teni:").pack()
    entry_stock_min = tk.Entry(ventana_agregar)
    entry_stock_min.pack()

    tk.Button(ventana_agregar, text="Guardar", command=guardar).pack()

    ventana_agregar.mainloop()

def eliminar_stock_tenis():
    def eliminar():
        id = entry_id.get()
        resultado = tenis.Tenis.eliminarStock(id)
        if resultado:
            messagebox.showinfo("Éxito", f"Se ha eliminado el stock del Teni con ID '{id}'")
        else:
            messagebox.showerror("Error", "No fue posible eliminar el stock. Inténtalo de nuevo.")
        ventana_eliminar.destroy()

    ventana_eliminar = tk.Tk()
    ventana_eliminar.title("Eliminar Stock de Tenis")

    tk.Label(ventana_eliminar, text="ID del Teni al cual deseas eliminar el stock:").pack()
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack()

    tk.Button(ventana_eliminar, text="Eliminar Stock", command=eliminar).pack()

    ventana_eliminar.mainloop()

def eliminar_tenis():
    def eliminar():
        id = entry_id.get()
        resultado = tenis.Tenis.eliminarProducto(id)
        if resultado:
            messagebox.showinfo("Éxito", f"Se ha eliminado el teni con ID '{id}'")
        else:
            messagebox.showerror("Error", "No fue posible eliminar el teni. Inténtalo de nuevo.")
        ventana_eliminar.destroy()

    ventana_eliminar = tk.Tk()
    ventana_eliminar.title("Eliminar Tenis")

    tk.Label(ventana_eliminar, text="ID del Teni que deseas eliminar:").pack()
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack()

    tk.Button(ventana_eliminar, text="Eliminar Tenis", command=eliminar).pack()

    ventana_eliminar.mainloop()

def actualizar_cantidad_tenis():
    def actualizar():
        id = entry_id.get()
        cantidad = entry_cantidad.get()
        resultado = tenis.Tenis.actualizarCantidad(id, cantidad)
        if resultado:
            messagebox.showinfo("Éxito", "La cantidad del teni se ha actualizado correctamente")
        else:
            messagebox.showerror("Error", "Ha ocurrido un error al modificar la cantidad del teni.")
        ventana_actualizar.destroy()

    ventana_actualizar = tk.Tk()
    ventana_actualizar.title("Actualizar Cantidad de Tenis")

    tk.Label(ventana_actualizar, text="ID del Teni que le deseas cambiar la cantidad:").pack()
    entry_id = tk.Entry(ventana_actualizar)
    entry_id.pack()

    tk.Label(ventana_actualizar, text="Nueva cantidad:").pack()
    entry_cantidad = tk.Entry(ventana_actualizar)
    entry_cantidad.pack()

    tk.Button(ventana_actualizar, text="Actualizar Cantidad", command=actualizar).pack()

    ventana_actualizar.mainloop()

def mostrar_inventario_tenis():
    def mostrar():
        resultado = tenis.Tenis.mostrarProducto()
        if resultado:
            text_area.delete(1.0, tk.END)  # Limpiar el área de texto antes de mostrar los datos
            for fila in resultado:
                text_area.insert(tk.END, (f"ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Cantidad: {fila[3]} | "
                                          f"Talla: {fila[4]} | Color: {fila[5]} | Agujetas: {fila[6]} | Stock Max: {fila[7]} | "
                                          f"Stock Min: {fila[8]}\n"))
        else:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, "No hay productos en el inventario.")
    
    ventana_mostrar = tk.Tk()
    ventana_mostrar.title("Mostrar Inventario Tenis")

    tk.Label(ventana_mostrar, text="Inventario de Tenis:").pack()

    # Área de texto con barra de desplazamiento
    text_area = scrolledtext.ScrolledText(ventana_mostrar, width=80, height=20)
    text_area.pack()

    mostrar()

    ventana_mostrar.mainloop()

# Menú de Skateboard
def mostrar_menu_skateboard():
    skateboard_ventana = tk.Toplevel()
    skateboard_ventana.title("Menú de Skateboard")
    skateboard_ventana.geometry('600x450')
    skateboard_ventana.configure(background='lightgreen')

    tk.Label(skateboard_ventana, text="Menú de Skateboard", font=("Skull and void", 16)).pack(pady=10)
    tk.Button(skateboard_ventana, text="Agregar Skateboard", width=30, height=2, command=agregar_skateboard).pack(pady=5)
    tk.Button(skateboard_ventana, text="Eliminar Stock de Skateboard", width=30, height=2, command=eliminar_stock_skateboard).pack(pady=5)
    tk.Button(skateboard_ventana, text="Eliminar Producto de Skateboard", width=30, height=2, command=eliminar_skateboard).pack(pady=5)
    tk.Button(skateboard_ventana, text="Actualizar Cantidad de Skateboard", width=30, height=2, command=actualizar_cantidad_skateboard).pack(pady=5)
    tk.Button(skateboard_ventana, text="Mostrar Productos de Skateboard", width=30, height=2, command=mostrar_inventario_skateboard).pack(pady=5)
    tk.Button(skateboard_ventana, text="Volver", width=30, height=2, command=skateboard_ventana.destroy).pack(pady=20)

def agregar_skateboard():
    def agregar():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        longitud = entry_longitud.get()
        stock_max = entry_stock_max.get()
        stock_min = entry_stock_min.get()

        obj_Skate = skateboard.Skates(nombre, precio, cantidad, longitud, stock_max, stock_min)
        resultado = obj_Skate.agregar()
        if resultado:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t La patineta {nombre} se registró correctamente")
        else:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t ** Por favor intentalo de nuevo, no fue posible agregar la patineta ** ...")
        text_area.config(state=tk.DISABLED)

    ventana_agregar = tk.Tk()
    ventana_agregar.title("Agregar Patineta")

    tk.Label(ventana_agregar, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_agregar)
    entry_nombre.pack()

    tk.Label(ventana_agregar, text="Precio:").pack()
    entry_precio = tk.Entry(ventana_agregar)
    entry_precio.pack()

    tk.Label(ventana_agregar, text="Cantidad:").pack()
    entry_cantidad = tk.Entry(ventana_agregar)
    entry_cantidad.pack()

    tk.Label(ventana_agregar, text="Longitud:").pack()
    entry_longitud = tk.Entry(ventana_agregar)
    entry_longitud.pack()

    tk.Label(ventana_agregar, text="Stock Máximo:").pack()
    entry_stock_max = tk.Entry(ventana_agregar)
    entry_stock_max.pack()

    tk.Label(ventana_agregar, text="Stock Mínimo:").pack()
    entry_stock_min = tk.Entry(ventana_agregar)
    entry_stock_min.pack()

    tk.Button(ventana_agregar, text="Agregar", command=agregar).pack()

    text_area = tk.Text(ventana_agregar, height=5, width=60, state=tk.DISABLED)
    text_area.pack()

    ventana_agregar.mainloop()

def eliminar_stock_skateboard():
    def eliminar():
        id = entry_id.get()

        resultado = skateboard.Skates.eliminarStock(id)
        if resultado:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t Se ha eliminado el stock de la patineta con id '{id}'")
        else:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t ** Por favor intentalo de nuevo, no fue posible eliminar el stock ** ...")
        text_area.config(state=tk.DISABLED)

    ventana_eliminar_stock = tk.Tk()
    ventana_eliminar_stock.title("Eliminar Stock de Patineta")

    tk.Label(ventana_eliminar_stock, text="ID de la patineta:").pack()
    entry_id = tk.Entry(ventana_eliminar_stock)
    entry_id.pack()

    tk.Button(ventana_eliminar_stock, text="Eliminar Stock", command=eliminar).pack()

    text_area = tk.Text(ventana_eliminar_stock, height=5, width=60, state=tk.DISABLED)
    text_area.pack()

    ventana_eliminar_stock.mainloop()

def eliminar_skateboard():
    def eliminar():
        id = entry_id.get()

        resultado = skateboard.Skates.eliminarProducto(id)
        if resultado:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t Se ha eliminado la patineta con id '{id}'")
        else:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t ** Por favor intentalo de nuevo, no fue posible eliminar el producto **")
        text_area.config(state=tk.DISABLED)

    ventana_eliminar = tk.Tk()
    ventana_eliminar.title("Eliminar Patineta")

    tk.Label(ventana_eliminar, text="ID de la patineta:").pack()
    entry_id = tk.Entry(ventana_eliminar)
    entry_id.pack()

    tk.Button(ventana_eliminar, text="Eliminar Patineta", command=eliminar).pack()

    text_area = tk.Text(ventana_eliminar, height=5, width=60, state=tk.DISABLED)
    text_area.pack()

    ventana_eliminar.mainloop()

def actualizar_cantidad_skateboard():
    def actualizar():
        id = entry_id.get()
        cantidad = entry_cantidad.get()

        resultado = skateboard.Skates.actualizarCantidad(id, cantidad)
        if resultado:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t La cantidad de producto de la patineta se ha actualizado correctamente")
        else:
            text_area.config(state=tk.NORMAL)
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, f"\n\t Ha ocurrido un error al momento de modificar la cantidad de producto de la patineta")
        text_area.config(state=tk.DISABLED)

    ventana_actualizar = tk.Tk()
    ventana_actualizar.title("Actualizar Cantidad de Patineta")

    tk.Label(ventana_actualizar, text="ID de la patineta:").pack()
    entry_id = tk.Entry(ventana_actualizar)
    entry_id.pack()

    tk.Label(ventana_actualizar, text="Nueva cantidad:").pack()
    entry_cantidad = tk.Entry(ventana_actualizar)
    entry_cantidad.pack()

    tk.Button(ventana_actualizar, text="Actualizar Cantidad", command=actualizar).pack()

    text_area = tk.Text(ventana_actualizar, height=5, width=60, state=tk.DISABLED)
    text_area.pack()

    ventana_actualizar.mainloop()

def mostrar_inventario_skateboard():
    def mostrar():
        resultado = skateboard.Skates.mostrarProducto()
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        if resultado:
            for fila in resultado:
                text_area.insert(tk.END, f"\t ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Cantidad: {fila[3]} | Longitud: {fila[4]} | Stock Max: {fila[5]} | Stock Min: {fila[6]}\n")
        else:
            text_area.insert(tk.END, "\t ** No se encontraron patinetas en el inventario **")
        text_area.config(state=tk.DISABLED)

    ventana_mostrar = tk.Tk()
    ventana_mostrar.title("Mostrar Inventario de Patineta")

    tk.Label(ventana_mostrar, text="Inventario de Patinetas:").pack()

    text_area = scrolledtext.ScrolledText(ventana_mostrar, height=20, width=80, state=tk.DISABLED)
    text_area.pack()

    mostrar()

    ventana_mostrar.mainloop()


# Menú de Accesorios
def mostrar_menu_accesorios():
    accesorios_ventana = tk.Toplevel()
    accesorios_ventana.title("Menú de Accesorios")
    accesorios_ventana.geometry('600x450')
    accesorios_ventana.configure(background='lightgreen')

    tk.Label(accesorios_ventana, text="Menú de Accesorios", font=("Skull and void", 16)).pack(pady=10)
    tk.Button(accesorios_ventana, text="Agregar Accesorio", width=30, height=2, command=agregar_accesorio).pack(pady=5)
    tk.Button(accesorios_ventana, text="Eliminar Stock de Accesorio", width=30, height=2, command=eliminar_stock_accesorio).pack(pady=5)
    tk.Button(accesorios_ventana, text="Eliminar Producto de Accesorio", width=30, height=2, command=eliminar_accesorio).pack(pady=5)
    tk.Button(accesorios_ventana, text="Actualizar Cantidad de Accesorio", width=30, height=2, command=actualizar_cantidad_accesorio).pack(pady=5)
    tk.Button(accesorios_ventana, text="Mostrar Productos de Accesorios", width=30, height=2, command=mostrar_inventario_accesorios).pack(pady=5)
    tk.Button(accesorios_ventana, text="Volver", width=30, height=2, command=accesorios_ventana.destroy).pack(pady=20)

def agregar_accesorio():
    agregar_ventana = tk.Toplevel()
    agregar_ventana.title("Agregar Accesorio")

    tk.Label(agregar_ventana, text="Nombre").pack()
    entry_nombre = tk.Entry(agregar_ventana)
    entry_nombre.pack()

    tk.Label(agregar_ventana, text="Precio").pack()
    entry_precio = tk.Entry(agregar_ventana)
    entry_precio.pack()

    tk.Label(agregar_ventana, text="Cantidad").pack()
    entry_cantidad = tk.Entry(agregar_ventana)
    entry_cantidad.pack()

    tk.Label(agregar_ventana, text="Tipo").pack()
    entry_tipo = tk.Entry(agregar_ventana)
    entry_tipo.pack()

    tk.Label(agregar_ventana, text="Stock Máximo").pack()
    entry_stockMax = tk.Entry(agregar_ventana)
    entry_stockMax.pack()

    tk.Label(agregar_ventana, text="Stock Mínimo").pack()
    entry_stockMin = tk.Entry(agregar_ventana)
    entry_stockMin.pack()

    def procesar_agregar_accesorio():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        tipo = entry_tipo.get()
        stock_max = entry_stockMax.get()
        stock_min = entry_stockMin.get()

        obj_Accesorio = accesorios.Accesorios(nombre, precio, cantidad, tipo, stock_max, stock_min)
        resultado = obj_Accesorio.agregar()

        if resultado:
            print(f"\n\tEl accesorio {nombre} se registró correctamente")
        else:
            print(f"\n\t** Por favor inténtalo de nuevo, no fue posible agregar ** ...")

    tk.Button(agregar_ventana, text="Agregar Accesorio", command=procesar_agregar_accesorio).pack()

    agregar_ventana.mainloop()

def eliminar_stock_accesorio():
    eliminar_ventana = tk.Toplevel()
    eliminar_ventana.title("Eliminar Stock de Accesorio")

    tk.Label(eliminar_ventana, text="ID del Accesorio").pack()
    entry_id = tk.Entry(eliminar_ventana)
    entry_id.pack()

    def procesar_eliminar_stock():
        id = entry_id.get()
        resultado = accesorios.Accesorios.eliminarStocka(id)

        if resultado:
            print(f"\n\tSe ha eliminado el stock del accesorio con id '{id}'")
        else:
            print(f"\n\t** Por favor inténtalo de nuevo, no fue posible eliminar el stock ** ...")

    tk.Button(eliminar_ventana, text="Eliminar Stock", command=procesar_eliminar_stock).pack()

    eliminar_ventana.mainloop()

def eliminar_accesorio():
    eliminar_ventana = tk.Toplevel()
    eliminar_ventana.title("Eliminar Accesorio")

    tk.Label(eliminar_ventana, text="ID del Accesorio").pack()
    entry_id = tk.Entry(eliminar_ventana)
    entry_id.pack()

    def procesar_eliminar_accesorio():
        id = entry_id.get()
        resultado = accesorios.Accesorios.eliminarStock(id)

        if resultado:
            print(f"\n\tSe ha eliminado el accesorio con id '{id}'")
        else:
            print(f"\n\t** Por favor inténtalo de nuevo, no fue posible eliminar el producto ** ...")

    tk.Button(eliminar_ventana, text="Eliminar Accesorio", command=procesar_eliminar_accesorio).pack()

    eliminar_ventana.mainloop()

def actualizar_cantidad_accesorio():
    actualizar_ventana = tk.Toplevel()
    actualizar_ventana.title("Actualizar Cantidad de Accesorio")

    tk.Label(actualizar_ventana, text="ID del Accesorio").pack()
    entry_id = tk.Entry(actualizar_ventana)
    entry_id.pack()

    tk.Label(actualizar_ventana, text="Nueva Cantidad").pack()
    entry_cantidad = tk.Entry(actualizar_ventana)
    entry_cantidad.pack()

    def procesar_actualizar_cantidad():
        id = entry_id.get()
        cantidad = entry_cantidad.get()
        resultado = accesorios.Accesorios.actualizarCantidad(id, cantidad)

        if resultado:
            print(f"\n\tLa cantidad del accesorio se ha actualizado correctamente")
        else:
            print(f"\n\t** Ha ocurrido un error al momento de modificar la cantidad del producto ** ...")

    tk.Button(actualizar_ventana, text="Actualizar Cantidad", command=procesar_actualizar_cantidad).pack()

    actualizar_ventana.mainloop()

def mostrar_inventario_accesorios():
    def mostrar():
        resultado = accesorios.Accesorios.mostrarProducto()
        text_area.config(state=tk.NORMAL)
        text_area.delete(1.0, tk.END)
        if resultado:
            for fila in resultado:
                text_area.insert(tk.END, f"\t ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Cantidad: {fila[3]} | Tipo: {fila[4]} | Stock Max: {fila[5]} | Stock Min: {fila[6]}\n")
        else:
            text_area.insert(tk.END, "\t ** No se encontraron accesorios en el inventario **")
        text_area.config(state=tk.DISABLED)

    ventana_mostrar = tk.Tk()
    ventana_mostrar.title("Mostrar Inventario de Accesorios")

    tk.Label(ventana_mostrar, text="Inventario de Accesorios:").pack()

    text_area = scrolledtext.ScrolledText(ventana_mostrar, height=200, width=200, state=tk.DISABLED)
    text_area.pack()

    mostrar()

    ventana_mostrar.mainloop()

    mostrar_ventana = tk.Toplevel()
    mostrar_ventana.title("Mostrar Inventario de Accesorios")

    resultado = accesorios.Accesorios.mostrarProducto()

    if resultado:
        for fila in resultado:
            tk.Label(mostrar_ventana, text=f"ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]} | Cantidad: {fila[3]} | Tipo: {fila[4]} | Stock Max: {fila[5]} | Stock Min: {fila[6]}").pack()
    else:
        tk.Label(mostrar_ventana, text="No hay accesorios en el inventario.").pack()

    mostrar_ventana.mainloop()