import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T

from torch import Tensor
from typing import Tuple

def load_audio(audio_path: str) -> Tuple[Tensor, int]:
    return torchaudio.load(audio_path)

def save_audio(file_path, audio_tensor, target_sr=22050, channels_first=True, encoding="PCM_S", bits_per_sample=16) -> None:
    torchaudio.save(file_path, audio_tensor, target_sr, channels_first=channels_first, encoding=encoding, bits_per_sample=bits_per_sample)

def normalize_volume(audio_tensor, audio_sr, target_volume_db=-24):
    loudness = F.loudness(audio_tensor, audio_sr).item()
    return T.Vol(target_volume_db - loudness, 'db')(audio_tensor)

def resample(audio_tensor, audio_sr, target_sr=22050):
    return F.resample(audio_tensor, audio_sr, target_sr)

def convert_to_mono_channel(audio_tensor):
    return torch.mean(audio_tensor, 0, True)

def make_default_tts_wav(audio_path) -> Tensor:
    audio, sr = load_audio(audio_path)
    audio = convert_to_mono_channel(audio)
    audio = normalize_volume(audio, sr)
    return resample(audio, sr)