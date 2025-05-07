from moviepy.editor import AudioFileClip

def convert_to_wav(input_audio_path, output_audio_path="converted.wav"):
    audio_clip = AudioFileClip(input_audio_path)
    audio_clip.write_audiofile(output_audio_path, codec='pcm_s16le')
    return output_audio_path
