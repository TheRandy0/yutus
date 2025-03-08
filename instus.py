from libreriasYutus import obtener_direccion_carpeta
from datetime import datetime
import os
import shutil
from tkinter import messagebox
from instaloader import instaloader, Post
from urllib.parse import urlparse
import re

class descargar_insta:
    def descargar_video_instagram(self, insta):
        try:
            carpeta_destino = obtener_direccion_carpeta()
            if carpeta_destino == None:
                messagebox.showerror("Error", "No se pudo obtener la carpeta de descarga")
            else:
                # Separar la URL en partes
                parsed_url = urlparse(insta)
                print(parsed_url)
                insta = parsed_url.path
                print(insta)
                # Obtener último valor de la lista del path
                insta = insta.split("/")[-2]
                print(insta)
                # Obtener el video
                loader = instaloader.Instaloader()
                post = Post.from_shortcode(loader.context, insta)

                fecha_descarga = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                titulo_insta = re.sub(r'[\\/*?:"<>|]', "", post.owner_username) + f"_{post.mediaid}" + f"_{fecha_descarga}"
                print(titulo_insta)
                
                insta_downloads = "Instagram Downloads"
                os.chdir(carpeta_destino)
                carpeta_temporal = os.path.join(carpeta_destino, insta_downloads)
                # Descargar video
                loader.download_post(post, target='Instagram Downloads')

                for file in os.listdir(os.path.join(carpeta_destino, insta_downloads)):
                    if file.endswith(".mp4"):
                        viejo_path = os.path.join(carpeta_destino, insta_downloads, file)
                        nuevo_path = os.path.join(carpeta_destino, f"{titulo_insta}.mp4")
                        
                        contador = 1
                        while os.path.exists(nuevo_path):  # Evita sobreescribir archivos existentes
                            nuevo_path = os.path.join(carpeta_destino, f"{titulo_insta}_{contador}.mp4")
                            contador += 1
                        
                        os.rename(viejo_path, nuevo_path)
                        os.utime(nuevo_path, (datetime.now().timestamp(), datetime.now().timestamp()))
                        
                        break
                
                shutil.rmtree(carpeta_temporal, ignore_errors=True)
                # os.rmdir(os.path.join(carpeta_destino, insta_downloads))

                messagebox.showinfo("Yeii", "Video descargador correctamente")
                print(insta)
        except Exception as e:
            messagebox.showerror("Error", "Error durante el proceso de ejecución")
            print(e)
