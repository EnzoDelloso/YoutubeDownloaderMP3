import yt_dlp

url = input("Cole o link do YouTube: ").strip()

opcoes = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,

    "extractor_args": {
        "youtube": {
            "player_client": ["web_embedded"]
        }
    },

    "js_runtimes": {
        "deno": {}
    },

    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}

try:
    print("\nBaixando e convertendo para MP3...\n")

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

    print("\n✓ MP3 baixado com sucesso!")

except Exception as erro:
    print(f"\n✗ Erro: {erro}")