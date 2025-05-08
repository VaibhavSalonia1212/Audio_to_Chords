import librosa
import numpy as np
from pychord import find_chords_from_notes

# Add guitar chord dictionary
guitar_chords = {
    "C": "x32010",
    "D": "xx0232",
    "E": "022100",
    "F": "133211",
    "G": "320003",
    "A": "x02220",
    "B": "x24442",
    "Am": "x02210",
    "Dm": "xx0231",
    "Em": "022000",
    "A7": "x02020",
    "D7": "xx0212",
    "E7": "020100",
    "G7": "320001",
    "C7": "x32310",
    # Add more if needed
}

def detect_chords(audio_path, duration=30):
    y, sr = librosa.load(audio_path, duration=duration)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    avg_chroma = np.mean(chroma, axis=1)

    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
                  'F#', 'G', 'G#', 'A', 'A#', 'B']
    top_notes = [note_names[i] for i in np.argsort(avg_chroma)[-3:]]
    
    chords = find_chords_from_notes(top_notes)
    
    # Get guitar fingerings for found chords
    chord_fingerings = []
    for chord in chords:
        fingering = guitar_chords.get(str(chord), "Fingering not available")
        chord_fingerings.append((str(chord), fingering))

    return chord_fingerings, top_notes
