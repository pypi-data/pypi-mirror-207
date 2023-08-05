import os
import shutil
from typing import List
from tqdm import tqdm

from shttst.audio import classify_audio_file, get_transcription
from shttst.dataset import ShmartTranscriptionLine
from shttst.files import append_file, destroy_file, get_audio_files

def classify_step(dir_path, audio_list, remove_bad=False) -> List[str]:
    ok=[]
    for path in tqdm(audio_list):
        audio_class = classify_audio_file(path)
        if  audio_class != 'fine':
            if remove_bad:
                destroy_file(path)
            else:
                append_file(os.path.join(dir_path, '1_bad.txt'), f'{path}|{audio_class}\n')
        else:
            speaker_path = os.path.dirname(path)
            if not speaker_path.endswith('\\wavs'):
                wavs_path = os.path.join(speaker_path, 'wavs')
                os.makedirs(wavs_path)
                new_path = os.path.join(wavs_path, os.path.basename(path))
                shutil.move(path, new_path)
                path = new_path
            
            append_file(os.path.join(dir_path, '1_good.txt'), f'{path}\n')
            ok.append(path)
    return ok
        
def transcribe_directory(dir_path: str, min_chars_per_sec=9, max_chars_per_sec=24, classify=True, remove_bad=False) -> None:
    audio_list = get_audio_files(dir_path)
    if classify:
        audio_list = classify_step(dir_path, audio_list, remove_bad)
    
    for path in tqdm(audio_list):
        wavs_path = os.path.dirname(path)
        text, duration = get_transcription(path)
        chars_per_sec = len(text) / duration
        if not text or chars_per_sec < min_chars_per_sec or chars_per_sec > max_chars_per_sec:
            append_file(os.path.join(dir_path, '2_bad.txt'), f'{path}|{text}|{duration}\n')
            continue

        line = ShmartTranscriptionLine(
            os.path.basename(path).replace('.wav', ''),
            text,
            'unknown',
            'normal',
            duration
        )
        append_file(os.path.join(wavs_path, os.path.pardir, 'metadata.csv'), f'{line.serialize()}')
        

if __name__ == '__main__':
    transcribe_directory('/content/anon', remove_bad=True)