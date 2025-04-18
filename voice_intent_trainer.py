from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# 🗂️ Step 1: Sample Training Data (Text, Intent)
training_data = [
    ("start recording", "start_recording"),
    ("begin audio capture", "start_recording"),
    ("can you record", "start_recording"),
    ("stop recording now", "stop_recording"),
    ("please stop the recorder", "stop_recording"),
    ("take a photo", "open_camera"),
    ("open the camera", "open_camera"),
    ("show me the camera", "open_camera"),
    ("call emergency", "emergency_call"),
    ("i need help", "emergency_call"),
    ("open my profile", "show_profile"),
    ("show my account", "show_profile"),
]

# Separate inputs and labels
X, y = zip(*training_data)

# 🧠 Step 2: Create the ML pipeline
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# 🏋️ Step 3: Train the model
model.fit(X, y)

# ✅ Step 4: Test prediction
print("Test:", model.predict(["start the recorder"]))

# 💾 Step 5: Save the model to a file
with open("intent_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as intent_model.pkl")

# 🧪 Step 6: Live terminal input test loop
while True:
    user_input = input("\n🗣️ Enter a voice command (or type 'exit' to quit): ")
    if user_input.lower() in ['exit', 'quit']:
        break

    prediction = model.predict([user_input])[0]
    print(f"🤖 Predicted Intent: {prediction}")
