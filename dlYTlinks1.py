# asking from the user to select the output path using tkinter library

def download_youtube_audio(url, output_path):
    youtube = YouTube(url)
    audio_stream = youtube.streams.filter(only_audio=True, file_extension='mp4').first()
    
    if audio_stream is not None:
        audio_stream.download(output_path=output_path)
        # Rename the downloaded file to have the .mp3 extension
        original_file_path = os.path.join(output_path, audio_stream.default_filename)
        new_file_path = os.path.join(output_path, youtube.title + '.mp3')
        os.rename(original_file_path, new_file_path)
        print(f"Audio downloaded and saved as {new_file_path}")
    else:
        print("No suitable audio stream found.")

if __name__ == "__main__":
    
    
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    output_folder = filedialog.askdirectory(title="Select the output folder")
    
    for url in links_list:
        download_youtube_audio(url, output_folder)

