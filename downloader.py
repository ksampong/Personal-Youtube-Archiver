from pytube import YouTube

#Youtube downloader function
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        return f"Video downloaded successfully to {save_path}!"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    def open_file_dialog():
        folder = filedialog.askdirectory()
        if folder:
            print(f"Selected folder: {folder}")

        return folder

    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        print(download_video(video_url, save_dir))
    else:
        print("Invalid save location.")
