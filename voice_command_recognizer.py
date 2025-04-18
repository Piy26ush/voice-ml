from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pickle

# Load Vosk model
model = Model("model/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)

# Load ML model
with open("intent_model.pkl", "rb") as f:
    intent_model = pickle.load(f)

# Set up mic input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

print("🎤 Speak your command (say 'exit' to stop)...")

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        text = result.get("text", "").strip()
        if text:
            print("📝 You said:", text)
            if "exit" in text:
                break

            # Predict intent
            intent = intent_model.predict([text])[0]
            print("🤖 Intent:", intent)
