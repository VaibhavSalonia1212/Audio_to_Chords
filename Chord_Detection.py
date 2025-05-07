import librosa
import numpy as np
from pychord import find_chords_from_notes

def detect_chords(audio_path, duration=30):
    y, sr = librosa.load(audio_path, duration=duration)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    avg_chroma = np.mean(chroma, axis=1)

    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
                  'F#', 'G', 'G#', 'A', 'A#', 'B']
    top_notes = [note_names[i] for i in np.argsort(avg_chroma)[-3:]]
    chords = find_chords_from_notes(top_notes)
    return chords, top_notes
