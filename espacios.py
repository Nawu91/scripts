import os
import pandas as pd

def eliminar_espacios_excel(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)

    # Aplicar la función strip a cada celda del DataFrame
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Sobrescribir el archivo Excel original
    df.to_excel(archivo_excel, index=False)

if __name__ == "__main__":
    # Nombre del archivo Excel en la misma carpeta que el script
    archivo_excel = "nombre_del_archivo.xlsx"

    # Obtener la ruta completa del archivo Excel
    ruta_completa = os.path.join(os.path.dirname(__file__), archivo_excel)

    # Llamar a la función para eliminar los espacios y sobrescribir el archivo
    eliminar_espacios_excel(ruta_completa)

    print(f"Se han eliminado los espacios en {archivo_excel} y se ha sobrescrito el mismo archivo.")
