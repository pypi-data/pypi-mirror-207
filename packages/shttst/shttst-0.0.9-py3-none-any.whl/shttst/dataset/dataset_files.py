import os
import shutil
from shttst.files import destroy_file, get_files
from shttst.dataset.transcriptions import read_transcriptions_file, write_transcriptions


def scan_dir(dir_path: str):
    return get_files(dir_path, ['csv'], 'metadata')

def check_dataset(metadata_path: str, delete_missing = False):
    wavs_dir_path = os.path.join(os.path.dirname(metadata_path), 'wavs')
    transcriptions = read_transcriptions_file(metadata_path)
    transcribed_files = [x.get_transcription_file(wavs_dir_path) for x in transcriptions]
    if not os.path.exists(wavs_dir_path):
        raise Exception(f'{wavs_dir_path} does not exist, check dataset structure.')
    wavs = get_files(wavs_dir_path, ['wav'])
    transcribed_wavs = [x for x in wavs if x in transcribed_files]
    missing_wavs = [x for x in transcribed_files if x not in wavs]
    missing_transcriptions = [x for x in wavs if x not in transcribed_files]
    if delete_missing:
        if len(missing_wavs):
            transcriptions = [x for x in transcriptions if x.get_transcription_file(wavs_dir_path) not in missing_wavs]
            shutil.move(metadata_path, f'{metadata_path}.bak')
            write_transcriptions(metadata_path, transcriptions)
        for missing_transcription in missing_transcriptions:
            destroy_file(missing_transcription)
    return transcriptions, transcribed_wavs, missing_wavs, missing_transcriptions

if __name__ == '__main__':
    dir_path = '/content/anon'
    for dataset_meta in scan_dir(dir_path):
        try:
            print([len(x) for x in check_dataset(dataset_meta)])
        except Exception as e:
            print(e)
    