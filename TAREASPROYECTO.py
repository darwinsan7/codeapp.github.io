import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, nombre, fecha_limite):
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        for tarea in self.tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            tarea_text = f"{tarea.nombre} - {tarea.fecha_limite} - {estado}"
            tareas_listbox.insert(tk.END, tarea_text)

    def marcar_completada(self):
        seleccion = tareas_listbox.curselection()
        if len(seleccion) == 0:
            messagebox.showerror("Error", "Selecciona una tarea primero.")
        else:
            tarea_text = tareas_listbox.get(seleccion[0])
            nombre_tarea = tarea_text.split(" - ")[0]
            for tarea in self.tareas:
                if tarea.nombre == nombre_tarea:
                    tarea.completada = True
                    tareas_listbox.delete(seleccion[0])
                    tareas_listbox.insert(seleccion[0], f"{tarea_text} (Completada)")
                    break

    def agregar_nueva_tarea(self):
        nombre = nombre_entry.get()
        fecha_limite = fecha_limite_entry.get()
        if nombre == "" or fecha_limite == "":
            messagebox.showerror("Error", "Introduce el nombre y la fecha límite de la tarea.")
        else:
            tarea = Tarea(nombre, fecha_limite)
            self.agregar_tarea(tarea)
            tarea_text = f"{tarea.nombre} - {tarea.fecha_limite} - Pendiente"
            tareas_listbox.insert(tk.END, tarea_text)
            nombre_entry.delete(0, tk.END)
            fecha_limite_entry.delete(0, tk.END)

if __name__ == "__main__":
    lista_tareas = ListaTareas()

    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Lista de tareas")

    # Crear widgets
    tareas_listbox = tk.Listbox(ventana)
    nueva_tarea_label = tk.Label(ventana, text="Nueva tarea:")
    nombre_entry = tk.Entry(ventana)
    fecha_limite_label = tk.Label(ventana, text="Fecha límite (dd/mm/aaaa):")
    fecha_limite_entry = tk.Entry(ventana)
    agregar_tarea_button = tk.Button(ventana, text="Agregar tarea", command=lista_tareas.agregar_nueva_tarea)
    completar_tarea_button = tk.Button(ventana, text="Completar tarea", command=lista_tareas.marcar_completada)

    # Añadir widgets a la ventana
    tareas_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    nueva_tarea_label.pack(side=tk.LEFT, padx=5, pady=5)
    nombre_entry.pack(side=tk.LEFT, padx=5, pady=5)
    fecha_limite_label.pack(side=tk.LEFT, padx=5, pady=5)
    fecha_limite_entry.pack(side=tk.LEFT, padx=5, pady=5)
    agregar_tarea_button.pack(side=tk.LEFT, padx=5, pady=5)
    completar_tarea_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Mostrar ventana
    ventana.mainloop()

    ancho_ventana = ventana.winfo_reqwidth()
    altura_ventana = ventana.winfo_reqheight()
    posicion_x = int((ventana.winfo_screenwidth() / 2) - (ancho_ventana / 2))
    posicion_y = int((ventana.winfo_screenheight() / 2) - (altura_ventana / 2))
    ventana.geometry(f"+{posicion_x}+{posicion_y}")
