from pytube import YouTube

def download_video(url, path="."):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=path)
    print(f"✅ Downloaded: {yt.title}")

if __name__ == "__main__":
    link = input("Enter YouTube video URL: ")
    download_video(link)
