import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class Imagen:
    def __init__(self):
        self.__nombre_imagen = ""
                
    @staticmethod
    def subir_y_guardar_imagen(self):
        try:
            # Cuadro de diálogo para seleccionar una imagen
            ruta_archivo = filedialog.askopenfilename(
                title="Selecciona una imagen",
                filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif")]
            )

            # Si el usuario selecciona un archivo, proceder
            if ruta_archivo:
                print(f"Imagen seleccionada: {ruta_archivo}")

                
                directorio = "Imagenes" # Definir la carpeta de destino donde se guardará la imagen

                # Crear la carpeta si no existe
                if not os.path.exists(directorio):
                    os.makedirs(directorio)
                    print(f"Carpeta '{directorio}' creada exitosamente.")

                # Obtener el nombre del archivo seleccionado
                nombre_archivo = os.path.basename(ruta_archivo)
                self.__nombre_imagen = nombre_archivo  
        
                # Definir la ruta de destino con el nombre de archivo
                destino = os.path.join(os.getcwd(),directorio, nombre_archivo)
                # Comprobar si la imagen ya existe en la carpeta
                if os.path.exists(destino):
                    # Mensaje de confirmación para sobreescribir
                    sobreescribir = messagebox.askyesno("Imagen existente", "La imagen ya existe. ¿Quieres sobrescribirla?")
                    if not sobreescribir:
                        print("Se canceló la operación de guardado.")
                        return nombre_archivo

                # Copiar la imagen a la carpeta de destino
                shutil.copy(ruta_archivo, destino)

                # Mostrar un mensaje indicando que la imagen se guardó correctamente
                messagebox.showinfo("Guardado exitoso", f"Imagen guardada exitosamente en: {destino}")
                print(f"Imagen guardada exitosamente en: {destino}")
                return nombre_archivo
            else:
                print("No se seleccionó ninguna imagen.")

        except Exception as e:
            print(f"Ocurrió un error al guardar la imagen: {e}")

    def get_nombre_imagen(self):
        return self.__nombre_imagen
    
    def abrir_ventana_subir_imagen(self):        
        # Crear la ventana principal de tkinter
        root = tk.Tk()
        root.title("Subir y Guardar Imagen")

        # Botón para subir la imagen y guardarla
        boton_subir_guardar = tk.Button(root, text="Subir y Guardar Imagen", command=lambda: Imagen.subir_y_guardar_imagen(self), font=("Arial", 14))
        boton_subir_guardar.pack(pady=20)
        
        # Ejecutar la interfaz gráfica
        root.mainloop()