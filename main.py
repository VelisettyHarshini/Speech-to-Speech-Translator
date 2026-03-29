from record import record_audio
from noise import reduce_noise
from vad import apply_vad
from asr import speech_to_text
from translate import translate_text
from tts import speak

def main():
    print("Universal to Telugu Speech Translator")
    print("Speak in ANY language\n")

    record_audio()
    reduce_noise()
    apply_vad()
    text, lang = speech_to_text()

    if not text.strip():
        print("No speech detected")
        return
    telugu = translate_text(text, lang)
    speak(telugu)

if __name__ == "__main__":
    main()
