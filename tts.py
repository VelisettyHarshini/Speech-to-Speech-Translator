from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang="te", slow=False)
    tts.save("output.mp3")

    print("Playing audio")
    os.system("mpg321 output.mp3")
