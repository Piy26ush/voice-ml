# Voice Intent App

---

## 🛠️ Setup Instructions – Run on Your Laptop

### 🧠 Backend (Flask + ML)

1. Open terminal and navigate to the project:
   ```bash
   cd voice-ml
   ```

2. Create a Python virtual environment:
   ```bash
   python3 -m venv venv2
   source venv2/bin/activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask backend:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run --host=0.0.0.0 --port=5001
   ```

---

### 📱 Frontend (React Native iOS App)

1. Install dependencies:
   ```bash
   cd VoiceIntentApp
   npm install
   ```

2. Install CocoaPods dependencies for iOS:
   ```bash
   cd ios
   pod install
   cd ..
   ```

3. Open the iOS project in Xcode:
   ```bash
   npx react-native run-ios
   ```

4. If app fails to launch due to code signature errors:
   - Open the project in Xcode using:
     ```bash
     cd ios
     xed .
     ```
   - In Xcode:
     - Go to your app target > Signing & Capabilities
     - Change `Bundle Identifier` to something unique (e.g., `com.yourname.voiceintent`)
     - Set your personal Apple ID as the development team
     - Clean and rebuild: `Product > Clean Build Folder`
     - Run again

---

### 🌐 Connect App to Backend

In `App.js`, update your backend IP:
```js
const response = await fetch("http://<YOUR_LOCAL_IP>:5001/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text }),
});
```

Find your local IP:
```bash
ifconfig | grep inet
```
(Use the IP under Wi-Fi, usually like `192.168.x.x`)
