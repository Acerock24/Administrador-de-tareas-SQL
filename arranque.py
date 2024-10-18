import sqlite3
import tkinter as tk
from tkinter import messagebox

def crear_tabla():
    con = sqlite3.connect('tareas.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas 
                      (id INTEGER PRIMARY KEY, tarea TEXT, prioridad INTEGER)''')
    con.commit()
    con.close()

def agregar_tarea():
    tarea = entry_tarea.get()
    prioridad = entry_prioridad.get()
    if tarea and prioridad.isdigit():
        con = sqlite3.connect('tareas.db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO tareas (tarea, prioridad) VALUES (?, ?)", (tarea, int(prioridad)))
        con.commit()
        con.close()
        entry_tarea.delete(0, tk.END)
        entry_prioridad.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea y una prioridad válida.")

def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    con = sqlite3.connect('tareas.db')
    cursor = con.cursor()
    cursor.execute("SELECT tarea, prioridad FROM tareas ORDER BY prioridad ASC")
    for row in cursor.fetchall():
        lista_tareas.insert(tk.END, f"{row[0]} (Prioridad: {row[1]})")
    con.close()

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Administrador de Tareas")
ventana.geometry("300x400")

crear_tabla()

label_tarea = tk.Label(ventana, text="Tarea:")
label_tarea.pack()

entry_tarea = tk.Entry(ventana)
entry_tarea.pack()

label_prioridad = tk.Label(ventana, text="Prioridad:")
label_prioridad.pack()

entry_prioridad = tk.Entry(ventana)
entry_prioridad.pack()

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

lista_tareas = tk.Listbox(ventana)
lista_tareas.pack(fill=tk.BOTH, expand=True)

actualizar_lista()

ventana.mainloop()
