import whisper

model = whisper.load_model("base")  # load once globally

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['segments']  # segments include text and timing