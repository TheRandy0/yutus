import os

FFMPEG_PATH = "ffmpeg.exe"
BASE_DIR = os.getcwd()
json_path = os.path.join(BASE_DIR, "..", "data.json")

command = [FFMPEG_PATH, "-version"]

video_descargado = "Video_descargado_video.mp4"
audio_descargado = "Audio_descargado_audio.mp4"
errorCarpeta = "No se seleccionó una carpeta de descarga"
