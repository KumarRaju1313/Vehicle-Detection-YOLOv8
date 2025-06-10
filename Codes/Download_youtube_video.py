import yt_dlp

def download_stream_in_hd(url, output_path):
    ydl_opts = {
        'format': 'bv*[height<=1080]+ba/best[height<=1080]',  # Prefer 1080p or best below
        'outtmpl': output_path,
        'noplaylist': True,
        'merge_output_format': 'mp4',  # merge into mp4 format
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 after merging
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=fHKPQEVCX-s&list=PLS8lzSv6JRJ2OC7KVp05jqtY4MgLsitdX&index=11"
    output_path = "Pythonclass1_by.%(ext)s"  # extension will be set automatically
    download_stream_in_hd(url, output_path)
