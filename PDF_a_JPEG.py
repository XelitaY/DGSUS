import os
from pdf2image import convert_from_path

# 🔧 RUTA a la carpeta con los PDF
carpeta_pdfs = r"C:\Users\gis_d\Downloads\CASAXCASA"

# 🔧 RUTA a la carpeta bin de Poppler
poppler_path = r"C:\Users\gis_d\OneDrive\Documents\OMAR\Release-24.08.0-0\poppler-24.08.0\Library\bin"  # ← Ajusta esto

# 🔁 Recorrer todos los archivos PDF de la carpeta
for archivo in os.listdir(carpeta_pdfs):
    if archivo.lower().endswith(".pdf"):
        ruta_pdf = os.path.join(carpeta_pdfs, archivo)
        nombre_base = os.path.splitext(archivo)[0]

        print(f"Convirtiendo: {archivo}")
        try:
            # Convertir PDF a imágenes
            paginas = convert_from_path(ruta_pdf, dpi=300, poppler_path=poppler_path)
            
            for i, imagen in enumerate(paginas):
                ruta_salida = os.path.join(carpeta_pdfs, f"{nombre_base}_pag{i+1}.jpg")
                imagen.save(ruta_salida, "JPEG")
                print(f"  → Guardado: {ruta_salida}")
        except Exception as e:
            print(f"  ❌ Error al procesar {archivo}: {e}")

print("✅ Conversión completada.")
