import yt_dlp
import os

def baixar_mp3(url):
    folder_name = "Musicas"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Cole a URL do vídeo: ")
    baixar_mp3(url)