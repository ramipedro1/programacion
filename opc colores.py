import tkinter as tk  # Tkinter para la ventana
from urllib.request import urlopen  # Para descargar la imagen desde internet
from PIL import Image, ImageTk  # Pillow para trabajar con imágenes
from io import BytesIO  # Para convertir los datos de la imagen

def descargarPortada():
    urlImagen ="https://raw.githubusercontent.com/ramipedro1/programacion/refs/heads/main/descarga%20(2).png"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarFondo():
    urlImagen ="file:///D:/Users/Alumno/Documents/R%20Y%20P/png-transparent-colored-pencil-drawing-color-pencil-pencil-label-shading-thumbnail.png"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def mostrarOpcion1():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste Rojo", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion2():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste Azul", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)


def mostrarOpcion3():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste Amarillo", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion4():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste Verde", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
    for widget in ventana.winfo_children():  
        widget.destroy()

        
def mostrarMenu():
    limpiarVentana()
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Rojo", font=("Arial", 14), width=20, command=mostrarOpcion1)
    boton1.pack(pady=10)

    boton2 = tk.Button(ventana, text="Azul", font=("Arial", 14), width=20, command=mostrarOpcion2)
    boton2.pack(pady=10)

    boton3 = tk.Button(ventana, text="Amarillo", font=("Arial", 14), width=20, command=mostrarOpcion3)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Verde", font=("Arial", 14), width=20, command=mostrarOpcion4)
    boton4.pack(pady=10)

def main():
    global ventana
    ventana = tk.Tk()

  
    ancho = ventana.winfo_screenwidth() 
    alto = ventana.winfo_screenheight() 
    ventana.geometry(f"{ancho}x{alto}")

    imagen=descargarPortada()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

    portada = ImageTk.PhotoImage(imagenRedimensionada)

    ventana.portada=portada

    etiqueta = tk.Label(ventana, image=ventana.portada)
    etiqueta.place(width=ancho,height=alto) 

    
    botonComenzar=tk.Button(ventana, text="inicio", font=("Arial", 14), width=20, command=mostrarMenu)
    botonComenzar.place(x=550,y=100)

    ancho = ventana.winfo_screenwidth() 
    alto = ventana.winfo_screenheight() 
    ventana.geometry(f"{ancho}x{alto}")

    imagen=descargarFondo()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

    fondo = ImageTk.PhotoImage(imagenRedimensionada)

    ventana.fondo=fondo

    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho,height=alto) 

    ventana.mainloop()

if __name__=="__main__":
    main()
