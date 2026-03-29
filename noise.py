import noisereduce as nr
import soundfile as sf

def reduce_noise():
    data, rate = sf.read("input.wav")
    clean = nr.reduce_noise(y=data, sr=rate)

    sf.write("clean.wav", clean, rate)
    print("Noise reduced")
