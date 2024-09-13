import yt_dlp

def download_video(url, path):
    try:
        # Configuração de download
        ydl_opts = {
            'outtmpl': path + '/%(title)s.%(ext)s',  # Salva o vídeo no caminho fornecido
        }

        # Baixa o vídeo usando yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído!")
        
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

# URL do vídeo do YouTube
video_url = input("Digite a URL do vídeo do YouTube: ")

# Caminho onde o vídeo será salvo
save_path = input("Digite o caminho para salvar o vídeo: ")

# Baixar o vídeo
download_video(video_url, save_path)
