from audio_utils import convert_to_wav
from transcription import transcribe_audio
from chord_detection import detect_chords

def generate_lyrics_with_chords(input_audio):
    wav_file = convert_to_wav(input_audio)
    lyrics_segments = transcribe_audio(wav_file)
    chords, notes = detect_chords(wav_file)

    print("\n🎵 Detected Chords (Approximate):", chords)
    print("🎹 Top Notes:", notes)

    print("\n🎤 Lyrics with Chords:")
    for seg in lyrics_segments:
        print(f"[{chords[0] if chords else 'N/A'}] {seg['text'].strip()}")

if __name__ == "__main__":
    song_file = "your_song.mp3"  # Replace with your audio file
    generate_lyrics_with_chords(song_file)
