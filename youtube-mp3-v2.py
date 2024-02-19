from pytube import YouTube
import moviepy.editor as mp
import os

class YouTubeDownloaderMp3:
    def __init__(self):
        pass

    def extrair_mp3(self, url, nome_arquivo):
        # Baixar o vídeo do YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path='.', filename='temp')

        # Renomear o arquivo para ter a extensão correta
        temp_file = 'temp'
        for file in os.listdir('.'):
            if file.startswith(temp_file):
                os.rename(file, 'temp.webm')
                temp_file = 'temp.webm'
                break

        # Converter o vídeo para MP3
        clip = mp.AudioFileClip(temp_file)
        clip.write_audiofile(f'{nome_arquivo}.mp3')

        # Remover arquivos temporários
        clip.close()
        os.remove(temp_file)

# Exemplo de uso
downloader = YouTubeDownloaderMp3()
url = "https://www.youtube.com/watch?v=bUjQNMH1HYw"
nome_arquivo = "Oceano"
downloader.extrair_mp3(url, nome_arquivo)
