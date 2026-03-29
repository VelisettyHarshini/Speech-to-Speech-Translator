import torch
import soundfile as sf
from silero_vad import load_silero_vad, get_speech_timestamps

model = load_silero_vad()
def apply_vad():
    audio, sr = sf.read("clean.wav")

    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)

    audio_tensor = torch.tensor(audio).float()
    speech_timestamps = get_speech_timestamps(audio_tensor, model, sampling_rate=sr)

    segments = []
    for s in speech_timestamps:
        segments.append(audio_tensor[s['start']:s['end']])

    if segments and len(segments) > 0:
        speech_audio = torch.cat(segments)
        sf.write("speech.wav", speech_audio.numpy(), sr)
        print("Speech extracted")
    else:
        print("No speech detected, using clean audio")
        sf.write("speech.wav", audio, sr)
