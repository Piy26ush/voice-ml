import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# 📥 Step 1: Load training data from CSV
data = pd.read_csv("intent_data.csv")  # Ensure intent_data.csv is in the same folder
X = data["text"]
y = data["intent"]

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
