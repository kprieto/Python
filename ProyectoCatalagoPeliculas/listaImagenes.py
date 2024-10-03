import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pelicula

class ListaImagenes:
    
    def crear_ventana(lista_imagenes, nombreCatalogo):
        # Crear la ventana principal
        root = tk.Tk()
        root.title(f"Catálogo de Películas de {nombreCatalogo}")
        root.geometry("800x600")

        # Crear un contenedor para las películas
        frame = ttk.Frame(root, padding="10 10 10 10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear un contenedor con desplazamiento (scrollable container)
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        # Configurar el canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        ListaImagenes.mostrar_peliculas(scrollable_frame, lista_imagenes, canvas, scrollbar, root)
        

    # Crear la función para mostrar las películas
    def mostrar_peliculas(scrollable_frame,lista_imagenes, canvas, scrollbar, root):
        for idx, pelicula in enumerate(lista_imagenes):
            # Cargar la imagen de la película
            try:
                img = Image.open(pelicula["Imagen"])
                img = img.resize((150, 220), Image.Resampling.LANCZOS)  # Redimensionar imagen
                img = ImageTk.PhotoImage(img)

                # Crear un marco para cada película
                movie_frame = ttk.Frame(scrollable_frame, relief="raised", padding=10)
                movie_frame.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)

                # Etiqueta con la imagen
                lbl_img = tk.Label(movie_frame, image=img)
                lbl_img.image = img  # Necesario para evitar que la imagen se recolecte por el garbage collector
                lbl_img.pack()

                # Etiqueta con el título
                lbl_title = tk.Label(movie_frame, text=f"{pelicula['Pelicula']}", font=("Arial", 12, "bold"))
                lbl_title.pack()

            except FileNotFoundError:
                print("Imagen para la película no fue encontrada.")
                
        # Colocar el canvas y el scrollbar en la ventana principal
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

        # Iniciar el bucle principal
        root.mainloop()


