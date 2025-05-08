import os

# Ensure ffmpeg is available
ffmpeg_path = os.path.abspath("ffmpeg.exe")  
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

from Audio_Conversion import convert_to_wav
from Lyrics import transcribe_audio
from Chord_Detection import detect_chords  # Now returns (chord_name, fingering) tuples

def generate_lyrics_with_chords(input_audio):
    wav_file = convert_to_wav(input_audio)
    lyrics_segments = transcribe_audio(wav_file)
    chord_fingerings, notes = detect_chords(wav_file)

    print("\n🎵 Detected Chords (Approximate):")
    for name, fingering in chord_fingerings:
        print(f"Chord: {name}, Guitar Fingering: {fingering}")

    print("🎹 Top Notes:", notes)

    print("\n🎤 Lyrics with Chords:")
    first_chord = chord_fingerings[0][0] if chord_fingerings else 'N/A'
    for seg in lyrics_segments:
        print(f"[{first_chord}] {seg['text'].strip()}")

if __name__ == "__main__":
    song_file = "C:/Users/vabsa/Documents/Audio_to_Chords/SONG.mp3"  # Replace with your audio file
    generate_lyrics_with_chords(song_file)
