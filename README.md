# Sistema de Descarga de Multimedia de RRSS

Una vez instalado, se debe mover a la carpeta del proyecto y la carpeta debe tener el nombre de "FFMPEG-full-build", dentro del proyecto, el ejecutable que se encuentra dentro de FFMPEG se debe mover al directorio principal para su uso.

## Requirements

* [FFMPEG](https://ffmpeg.org/download.html)
* [Python 3.11](https://www.python.org/downloads/release/python-3119/)

##  Install

```bash
pip install -r requirements.txt
```

## Execute

```bash
python ./src/main.py
```

## Build

Se utiliza [Pyinstaller](https://pyinstaller.org/en/stable/) para la contrucción de la aplicación

```bash
pyinstaller --onefile --noconsole --add-data BackGround:minecraft.png Icons:apple.ico yutus.py
```
