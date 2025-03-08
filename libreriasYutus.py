import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from tkinter import Button, Tk
from tkinter import filedialog, ttk, messagebox
import requests
from urllib.parse import parse_qs, urlparse
import subprocess
import re
import json
import sys

FFMPEG_PATH = "ffmpeg.exe"
BASE_DIR = getattr(sys, '_MEIPASS', os.path.abspath("."))

command = [FFMPEG_PATH, "-version"]
json_path = os.path.join(BASE_DIR, "data.json")


video_descargado = "Video_descargado_video.mp4"
audio_descargado = "Audio_descargado_audio.mp4"
errorCarpeta = "No se seleccionó una carpeta de descarga"

def ffmpeg_merge(video, audio, salida):
    # Se ejecuta el comando
    subprocess.run(
        [FFMPEG_PATH, 
         "-i", video, 
         "-i", audio, 
         "-c:v", "copy", 
         "-c:a", "aac", 
         salida], shell=False)

class descarga_videos_youtube:

    def obtener_video_id(self, url):
        if "youtu.be" in url:
            return url.split("/")[-1].split("?")[0]

        if "shorts" in url:
            return url.split("/")[-1].split("?")[0]

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        if "v" in query_params:
            return query_params["v"][0]
        
        return None

    def descargar_video_mp4(self, direccion_video:str, resolucion='144p'):
        carpeta_destino = manejo_carpetas.obtener_direccion_carpeta("")
        if carpeta_destino == None:
            messagebox.showinfo("Error", errorCarpeta)
        else:
            # Obtener el ID del video
            url = direccion_video.strip()
            print(url)
            video_id = descarga_videos_youtube.obtener_video_id("", url)

            # Verificar si el video existe
            if not video_id:
                print("URL no válida. ")

            # Adjuntar id a formato
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print("URL", video_url)

            # Obtener el video
            response = requests.get(video_url, allow_redirects=True)
            if response.status_code != 200:
                messagebox.showerror("Error", "Error al obtener el video")

            # Crear una variable de tipo YouTube
            yt = YouTube(video_url, on_progress_callback=on_progress)

            # Obtener lista de resoluciones y filtrar
            streams = yt.streams
            streams_filtered = streams.filter(res=resolucion, only_video=True, file_extension='mp4')
            streams_audio = streams.filter(file_extension='mp4', only_audio=True).first()
            stream = streams_filtered
            
            # Verificar que la resolución o el audio existan
            if not stream or not streams_audio:
                messagebox.showwarning("Error", "Resolución o audio no encontrada")
                return
            
            # Eliminar caracteres especiales para evitar problemas con FFMPEG
            video_salida = (re.sub('[^A-Za-z0-9]+', '_', f"{yt.title}"))

            # Archivos temporales y archivo final en la carpeta de descarga
            video_lcn = os.path.join(carpeta_destino, video_descargado)
            audio_lcn = os.path.join(carpeta_destino, audio_descargado)
            salida_lcn = os.path.join(carpeta_destino, f"{video_salida}.mp4")

            # Descargar video
            streams_filtered.first().download(output_path=carpeta_destino, filename=(video_descargado))
            streams_audio.download(output_path=carpeta_destino, filename=(audio_descargado))
            # Mezclar audio y video
            ffmpeg_merge(video_lcn, audio_lcn, salida_lcn)
            messagebox.showinfo("Yeii", "Video descargado con éxito ")
            # Borrar archivos temporales
            os.remove(video_lcn)
            os.remove(audio_lcn)

    def descargar_audio(self, direccion_video:str):
        try:
            carpeta_destino = manejo_carpetas.obtener_direccion_carpeta("")
            if carpeta_destino == None:
                messagebox.showerror("Error", errorCarpeta)
                print("Entró")
            else:
                url = direccion_video.strip()
                print(url)
                video_id = descarga_videos_youtube.obtener_video_id("", url)

                if not video_id:
                    messagebox.showerror("Error", "URL no válida")

                video_url = f"https://www.youtube.com/watch?v={video_id}"
                print("URL", video_url)

                response = requests.get(video_url, allow_redirects=True)

                if response.status_code != 200:
                    messagebox.showerror("Error", "Error al obtener el video")
                yt = YouTube(video_url)

                stream = yt.streams.filter(only_audio=True).first()

                stream.download(output_path=carpeta_destino, filename=f"{yt.title}.mp4")
                messagebox.showinfo("Yeii", "Audio descargado con éxito")
        except Exception:
            messagebox.showerror("Error", "Error al descargar el audio")

    def descargar_playlist(self, direccion_video):
        try:
            carpeta_destino = manejo_carpetas.obtener_direccion_carpeta("")
            if carpeta_destino == None:
                messagebox.showerror("Error", errorCarpeta)
            else:

                playlist = Playlist(direccion_video)
                playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                print(len(playlist.video_urls))

                for url in playlist.video_urls:
                    print(url)

                # Descargar video
                for video in playlist.videos:
                    audio_stream = video.streams.filter(only_audio=True).first()
                    audio_stream.download(output_path=carpeta_destino, filename=f"{video.title}.mp4")
                    
                messagebox.showinfo("Yeii", "Video descargado con éxito")
        except Exception:
            messagebox.showerror("Error", "No se pudo descargar la playlist")

    def descargar_shorts(self, direccion_video:str):
        try:
            carpeta_destino = manejo_carpetas.obtener_direccion_carpeta("")
            if carpeta_destino == None:
                messagebox.showerror("Error", errorCarpeta)
            else:
                url = direccion_video.strip()
                print(url)
                video_id = descarga_videos_youtube.obtener_video_id("", url)

                if not video_id:
                    messagebox.showerror("Error", "No se pudo obtener el id del video")
                
                video_url = f"https://www.youtube.com/shorts/{video_id}"

                response = requests.get(video_url, allow_redirects=True)
                if response.status_code != 200:
                    messagebox.showerror("Error", "No se pudo obtener el video")
                yt = YouTube(video_url)

                streams = yt.streams
                streams_filtered = streams.filter(only_video=True, file_extension='mp4')
                streams_audio = streams.filter(file_extension='mp4', only_audio=True).first()
                stream = streams_filtered

                # Verificar que la resolución o el audio existan
                if not stream or not streams_audio:
                    messagebox.showwarning("Error", "Resolución o audio no encontrada")
                    return

                video_salida = (re.sub('[^A-Za-z0-9]+', '_', f"{yt.title}"))
                
                # Archivos temporales y archivo final en la carpeta de descarga
                video_lcn = os.path.join(carpeta_destino, video_descargado)
                audio_lcn = os.path.join(carpeta_destino, audio_descargado)
                salida_lcn = os.path.join(carpeta_destino, f"{video_salida}.mp4")

                # Descargar video
                streams_filtered.first().download(output_path=carpeta_destino, filename=(video_descargado))
                streams_audio.download(output_path=carpeta_destino, filename=(audio_descargado))
                # Mezclar audio y video
                ffmpeg_merge(video_lcn, audio_lcn, salida_lcn)
                messagebox.showinfo("Yeii", "Video descargado con éxito")
                # Borrar archivos temporales
                os.remove(video_lcn)
                os.remove(audio_lcn)
                print(direccion_video, "direccionVideo for shorts")
        except Exception:
            messagebox.showerror("Error", "No se pudo descargar los shorts")

    def descargar_clips(self, direccion_video:str):
        try:
            # Obtener la carpeta de descarga
            carpeta_destino = descarga_videos_youtube.obtener_carpeta_descarga("")
            if carpeta_destino == None:
                messagebox.showerror("Error", "No se pudo obtener la carpeta de descarga")
            else:
                print(direccion_video)
        except Exception as e:
            messagebox.showinfo("Mensaje de error", str(e))

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
        script_json = os.path.dirname(__file__)

        with open(script_json + "/data.json") as file:
            data = json.load(file)
            for carpetas in data["carpeta"]:
                if carpetas["carpeta_descargas"] == "":
                    messagebox.showerror("Error", "No se ha encontrado la direccion de la descarga")
                    break
                else:
                    carpeta = carpetas["carpeta_descargas"]
                    print(carpeta)   
                    return carpeta

class manejo_datos:
    def ventana_seleccion_resolucion(self, url_youtube:str):
        root = Tk()
        root.geometry('500x500')
        vsr = ttk.Frame(root, padding=10)
        vsr.grid()
        root.resizable(False, False)
        fuente = "Roboco Cn"

        Button(vsr, text="1080p", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '1080p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=0)
        Button(vsr, text="720p", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '720p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=1)
        Button(vsr, text="480", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '480p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=2)
        Button(vsr, text="360", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '360p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=3)
        Button(vsr, text="240", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '240p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=4)
        Button(vsr, text="144", command=lambda: descarga_videos_youtube.descargar_video_mp4("", url_youtube, '144p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=5)

        root.mainloop()

    def comprobar_dato_input(self, direccion_video:str):
        print(direccion_video)
        # Preguntar si el link está vacío
        if direccion_video == "" or direccion_video == None:
            messagebox.showerror("Error", "No se ingresó la URL del video")

        elif "clip" in direccion_video:
            print(direccion_video, " Video Clips")

        elif "shorts" in direccion_video:
            print(direccion_video, " Video shorts")
            descarga_videos_youtube.descargar_shorts("", direccion_video)

        elif "playlist" in direccion_video:
            print(direccion_video, " Video Playlist")
            descarga_videos_youtube.descargar_playlist("", direccion_video)

        # Preguntar si el video es de youtube
        elif "youtube.com" in direccion_video or "youtu.be" in direccion_video:
            print(direccion_video, " Video Youtube")
            manejo_datos.ventana_seleccion_resolucion("", direccion_video)
