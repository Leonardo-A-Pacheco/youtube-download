from pytube import YouTube

class Downloader:
    def __init__(self, links):
        self.links = links

    def baixar_videos(self):
        for link in self.links:
            try:
                yt = YouTube(link)
                self.baixar_video(yt)
            except Exception as e:
                print(f'Ocorreu um erro ao baixar o vídeo {link}: {e}')

    def baixar_video(self, yt):
        try:
            video = yt.streams.get_highest_resolution()
            print(f'Baixando vídeo: {yt.title}')
            video.download(output_path='downloads/')
            print('Download concluído!')
        except Exception as e:
            print(f'Ocorreu um erro ao baixar o vídeo {yt.title}: {e}')

if __name__ == "__main__":
    # Lista de links dos vídeos do YouTube
    links = [
        # insira seus links aqui

    ]

    downloader = Downloader(links)
    downloader.baixar_videos()
