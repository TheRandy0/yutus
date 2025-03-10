from tkinter import messagebox
import config
from utils.files import obtener_direccion_carpeta, ffmpeg_merge
from utils.video import obtener_video_id
import requests
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os
import re

class YoutubeModel:

    def descargar_video_mp4(self, direccion_video:str, resolucion='144p'):
        carpeta_destino = obtener_direccion_carpeta()
        if carpeta_destino == None:
            messagebox.showinfo("Error", config.errorCarpeta)
        else:
            # Obtener el ID del video
            url = direccion_video.strip()
            print(url)
            video_id = obtener_video_id(url)

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
            video_lcn = os.path.join(carpeta_destino, config.video_descargado)
            audio_lcn = os.path.join(carpeta_destino, config.audio_descargado)
            salida_lcn = os.path.join(carpeta_destino, f"{video_salida}.mp4")

            # Descargar video
            streams_filtered.first().download(output_path=carpeta_destino, filename=(config.video_descargado))
            streams_audio.download(output_path=carpeta_destino, filename=(config.audio_descargado))
            # Mezclar audio y video
            ffmpeg_merge(video_lcn, audio_lcn, salida_lcn)
            messagebox.showinfo("Yeii", "Video descargado con éxito ")
            # Borrar archivos temporales
            os.remove(video_lcn)
            os.remove(audio_lcn)

    def descargar_audio(self, direccion_video:str):
        try:
            carpeta_destino = obtener_direccion_carpeta()
            if carpeta_destino == None:
                messagebox.showerror("Error", config.errorCarpeta)
                print("Entró")
            else:
                url = direccion_video.strip()
                print(url)
                video_id = obtener_video_id(url)

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

    def descargar_playlist(self, direccion_video:str):
        try:
            carpeta_destino = obtener_direccion_carpeta()
            if carpeta_destino == None:
                messagebox.showerror("Error", config.errorCarpeta)
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
            carpeta_destino = obtener_direccion_carpeta()
            if carpeta_destino == None:
                messagebox.showerror("Error", config.errorCarpeta)
            else:
                url = direccion_video.strip()
                print(url)
                video_id = obtener_video_id(url)

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
                video_lcn = os.path.join(carpeta_destino, config.video_descargado)
                audio_lcn = os.path.join(carpeta_destino, config.audio_descargado)
                salida_lcn = os.path.join(carpeta_destino, f"{video_salida}.mp4")

                # Descargar video
                streams_filtered.first().download(output_path=carpeta_destino, filename=(config.video_descargado))
                streams_audio.download(output_path=carpeta_destino, filename=(config.audio_descargado))
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
            carpeta_destino = obtener_direccion_carpeta()
            if carpeta_destino == None:
                messagebox.showerror("Error", "No se pudo obtener la carpeta de descarga")
            else:
                print(direccion_video)
        except Exception as e:
            messagebox.showinfo("Mensaje de error", str(e))
