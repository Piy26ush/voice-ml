# VoiceIntent App – iOS + Flask ML Setup

## 🧠 Purpose
This app allows voice-command-based intent recognition. It uses:
- React Native frontend for iOS and Android.
- Speech-to-text (STT) using `@react-native-voice/voice`.
- Flask backend with an ML model to classify intents.
- Optional offline STT with Vosk.

---

## 📁 Project Structure

```
voice-ml/
├── app.py                         ← Flask backend entry point
├── intent_data.csv               ← Training data
├── intent_model.pkl              ← Trained intent classification model
├── model.zip                     ← Zipped model files (probably for Vosk)
├── requirements.txt              ← Backend dependencies list
├── voice_command_recognizer.py   ← Voice command parsing logic
├── voice_intent_trainer.py       ← ML training script
├── model/
│   └── vosk-model-small-en-us-0.15/ ← Speech recognition model files (unzipped)
├── __pycache__/                  ← Python cache files
├── venv/                         ← (Old virtual environment – unused)
├── venv2/                        ← ✅ Your current working Python virtual environment
│   ├── bin/
│   ├── lib/
│   └── pyvenv.cfg
├── VoiceIntentApp/               ← React Native frontend project
│   ├── android/
│   ├── ios/
│   ├── App.js
│   ├── index.js
│   ├── app.json
│   ├── tsconfig.json
│   ├── babel.config.js
│   ├── node_modules/
│   ├── package.json
│   └── ...
```

---

## 🔗 Frontend (iOS / React Native)

### 🎤 Speech-to-Text
- Library: `@react-native-voice/voice`
- Converts speech to text, then calls backend for intent recognition.

### 🛑 iOS Permissions
Add to `ios/VoiceIntentApp/Info.plist`:
```xml
<key>NSMicrophoneUsageDescription</key>
<string>This app uses your mic to listen for commands.</string>
<key>NSSpeechRecognitionUsageDescription</key>
<string>Speech is used to understand what you say.</string>
```

### 🧹 Common iOS Issues
- Mic not released: fix with `Voice.destroy()` or `Voice.removeAllListeners()`.
- App crashes on 2nd command: usually due to duplicate listeners.
- Hinglish accuracy reduced: model may need Hinglish-specific training.

---

## 🌐 Backend (Flask)

### 🔧 Start Server
```bash
cd voice-ml/
source venv2/bin/activate
flask run --host=0.0.0.0 --port=5001
```

### 📡 `/predict` Endpoint
`app.py`:
```python
@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    # Use intent_model.pkl to classify text and return result
```

---

## 🔁 Frontend → Backend Call
In `App.js`:
```js
const response = await fetch(`http://${backendIP}:5001/predict`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ text }),
});
```
Replace `backendIP` with your Mac’s IP via `ifconfig`.

---

## ✅ Scripts Summary

| File | Purpose |
|------|---------|
| `app.py` | Runs Flask server |
| `voice_intent_trainer.py` | Trains and saves `intent_model.pkl` |
| `voice_command_recognizer.py` | Parses intent text |
| `requirements.txt` | Backend dependencies |
| `model.zip` | Zipped Vosk model |
