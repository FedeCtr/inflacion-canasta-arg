import pandas as pd

def cargar_datos(ruta_csv):
    try:
        df = pd.read_csv(ruta_csv)
        print("Datos cargados correctamente.")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_csv}")
        return None

if __name__ == "__main__":
    ruta = "data/canasta_basica.csv"  # Ajustá el nombre según tu archivo
    df = cargar_datos(ruta)
