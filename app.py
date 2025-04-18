from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # 👈 Important for React Native communication

# Load the model
with open("intent_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict_intent():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    prediction = model.predict([message])[0]
    return jsonify({"intent": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
