import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cuadros con Tkinter")
ventana.geometry("400x300")

# Crear un Frame para los cuadrados azules
frame_azules = tk.Frame(ventana)
frame_azules.pack()

# Cuadros azules
azul1 = tk.Canvas(frame_azules, width=100, height=100, bg="blue")
azul1.pack(side="left")
azul2 = tk.Canvas(frame_azules, width=100, height=100, bg="blue")
azul2.pack(side="left")

# Rectángulo horizontal
rectangulo = tk.Canvas(ventana, width=200, height=50, bg="green")  # Puedes cambiar el color a tu preferencia
rectangulo.pack()
rectangulo = tk.Canvas(ventana, width=200, height=50, bg="red")  # Puedes cambiar el color a tu preferencia
rectangulo.pack()
# Crear un Frame para los cuadrados rojos pequeños
frame_rojos = tk.Frame(ventana)
frame_rojos.pack()

# Cuadros rojos debajo del rectángulo
rojo1 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
rojo1.pack(side="left")
rojo2 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
rojo2.pack(side="left")
rojo3 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
rojo3.pack(side="left")
rojo4 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
rojo4.pack(side="left")

# Iniciar la aplicación
ventana.mainloop()
