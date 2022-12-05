from typing import Union

import librosa
import time

import numpy as np


def load(sound: str, sample_start: int, sample_end: int, fading_start: Union[int, None], fading_end: Union[int, None]):
    start = time.perf_counter()

    y, sr = librosa.load(sound)
    part_of_song = y[sr*sample_start:sr*sample_end]

    fade_start = np.linspace(0, 1.0, sr) if fading_start == '0' else np.ones(sr)
    middle = np.ones(sr * (sample_end - sample_start - 2))
    fade_end = np.linspace(1.0, 0, sr) if fading_end == '0' else np.ones(sr)

    fade_curve = np.concatenate((fade_start, middle, fade_end))
    faded_sound = part_of_song * fade_curve

    end = time.perf_counter()

    return {'sample_data': faded_sound, 'sr': sr, 'start': int(start), 'end': int(end), 'time': int(end - start)}
