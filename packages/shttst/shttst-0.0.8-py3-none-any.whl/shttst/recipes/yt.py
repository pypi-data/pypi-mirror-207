import os
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor import PostProcessor

from shttst.processing import AudioToDatasetProcessor

class ShmartYTDPostProcessor(PostProcessor):
    def __init__(self, keep_not_fine=False, denoise_all=False, use_classifier=True, downloader=None):
        super().__init__(downloader)
        self.processor = AudioToDatasetProcessor(keep_not_fine, denoise_all, use_classifier)

    def run(self, info):
        self.processor(info['filepath'])
       
        return [], info

def create_dataset_from_yt_playlist(playlist_id, output_dir='\\content\\yt_dlp', playlist_start=0, playlist_end=None, keep_not_fine=False, denoise_all=False, use_classifier=True):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'playliststart': playlist_start,
        'playlistend': playlist_end,
        'outtmpl': os.path.join(output_dir, '%(id)s', 'wavs', '%(id)s'),
        'quiet': True
    }

    with YoutubeDL(ydl_opts) as ytd:
        ytd.add_post_processor(ShmartYTDPostProcessor(keep_not_fine, denoise_all, use_classifier), when='post_process')
        ytd.download(playlist_id)

if __name__ == '__main__':
    create_dataset_from_yt_playlist('PLHtUOYOPwzJHI3WKWPEfMs0ztIn-G6tpl', output_dir='c:\\content\\yt_dlp')