from pytube import YouTube

def baixar_videos(links):
    for link in links:
        try:
            yt = YouTube(link)
            # Baixa o vídeo na maior resolução disponível
            video = yt.streams.get_highest_resolution()
            print(f'Baixando vídeo: {yt.title}')
            video.download(output_path='downloads/')
            print('Download concluído!')
        except Exception as e:
            print(f'Ocorreu um erro ao baixar o vídeo {link}: {e}')

if __name__ == "__main__":
    # Lista de links dos vídeos do YouTube
    links = [
        # 'https://www.youtube.com/watch?v=VIDEO_ID_1',
        # 'https://www.youtube.com/watch?v=VIDEO_ID_2',
        # # # Adicione mais links conforme necessário
        
        # https://www.youtube.com/watch?v=CGdbSAi99H4
        # https://www.youtube.com/watch?v=W9_KJKlg92c
        # https://www.youtube.com/watch?v=wKvur8YsQmg
    ]

    baixar_videos(links)
