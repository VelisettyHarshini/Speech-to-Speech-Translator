import whisper

model = whisper.load_model("base")

def speech_to_text():
    result = model.transcribe("clean.wav",fp16=False)
    text = result["text"]
    lang = result["language"]

    print("Text:", text)
    print("Detected Language:", lang)

    return text, lang
