from tkinter import filedialog, messagebox
import json
import subprocess
import config

class manejo_carpetas:
    def asignar_carpeta(self):
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta descarga")
        data = {}
        data['carpeta'] = []
        data['carpeta'].append({
            'carpeta_descargas': carpeta
        })

        with open('data.json', "w") as file:
            json.dump(data, file, indent=4)

    def obtener_direccion_carpeta(self):

        with open(config.json_path) as file:
            data = json.load(file)
            for carpetas in data["carpeta"]:
                if carpetas["carpeta_descargas"] == "":
                    messagebox.showerror("Error", "No se ha encontrado la direccion de la descarga")
                    break
                else:
                    carpeta = carpetas["carpeta_descargas"]
                    print(carpeta)   
                    return carpeta

def ffmpeg_merge(video, audio, salida):
    # Se ejecuta el comando
    subprocess.run(
        [config.FFMPEG_PATH, 
         "-i", video, 
         "-i", audio, 
         "-c:v", "copy", 
         "-c:a", "aac", 
         salida], shell=False)
