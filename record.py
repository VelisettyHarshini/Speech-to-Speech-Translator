import sounddevice as sd
import soundfile as sf
import numpy as np
import threading

def record_audio():
    fs = 16000

    input("Press ENTER to START recording...")

    print("Recording... Press ENTER again to STOP")

    recording = []
    stop_flag = [False]

    def wait_for_stop():
        input()
        stop_flag[0] = True

    threading.Thread(target=wait_for_stop).start()

    def callback(indata, frames, time, status):
        if stop_flag[0]:
            raise sd.CallbackStop()
        recording.append(indata.copy())

    try:
        with sd.InputStream(samplerate=fs, channels=1, callback=callback):
            while not stop_flag[0]:
                sd.sleep(100)
    except sd.CallbackStop:
        pass

    audio = np.concatenate(recording, axis=0)
    sf.write("input.wav", audio, fs)

    print("Recording stopped")
    print("Audio saved as input.wav\n")
