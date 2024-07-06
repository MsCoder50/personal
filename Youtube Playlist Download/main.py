from pytube import Playlist

def download_playlist_audio(playlist_url, output_path):
    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        audio_stream = video.streams.filter(only_audio=True).first()
        if audio_stream:
            print(f"Downloading audio from {video.title}...")
            audio_stream.download(output_path=output_path)
        else:
            print(f"No audio stream available for {video.title}.")

if __name__ == "__main__":
    # Example usage:
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    output_path = input("Enter the path to save the audio files: ")
    download_playlist_audio(playlist_url, output_path)
