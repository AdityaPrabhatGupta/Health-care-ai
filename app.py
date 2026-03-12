from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import pandas as pd
from flask_cors import CORS
from sklearn.preprocessing import MultiLabelBinarizer
import json
import requests as req_lib

# Load dataset
data = pd.read_csv('disease_symptoms.csv')
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(data['symptoms'].apply(lambda x: x.split(',')))
disease_labels = list(data['disease'].unique())

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(len(disease_labels), activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
y = np.array([disease_labels.index(d) for d in data['disease']])
model.fit(X, y, epochs=50, batch_size=8, validation_split=0.2)
model.save("disease_prediction_model.keras")
loaded_model = tf.keras.models.load_model("disease_prediction_model.keras")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login', methods=['POST'])
def login():
    try:
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "No data received."}), 400
        username = user_data.get('username', '').strip()
        password = user_data.get('password', '').strip()
        if not username or not password:
            return jsonify({"error": "Username and password required."}), 400
        # Accept any non-empty username and password
        return jsonify({"message": "Login successful!", "user": username}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_data = request.get_json()
        if user_data is None:
            return jsonify({"error": "No JSON received."}), 400
        if 'symptoms' not in user_data:
            return jsonify({"error": "Expected {'symptoms': ['symptom1']}"}), 400
        user_symptoms = [s.strip() for s in user_data['symptoms']]
        unknown_symptoms = [s for s in user_symptoms if s not in mlb.classes_]
        if unknown_symptoms:
            return jsonify({"error": f"Unknown symptoms: {unknown_symptoms}"}), 400
        input_data = mlb.transform([user_symptoms])
        prediction = loaded_model.predict(input_data)
        predicted_disease = disease_labels[np.argmax(prediction)]
        return jsonify({"predicted_disease": predicted_disease})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.get_json()
        if not user_data or 'messages' not in user_data:
            return jsonify({"error": "Expected {'messages': [...]}"}), 400
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        if not GROQ_API_KEY:
            return jsonify({"error": "API key not found!"}), 500
        conversation = ""
        for msg in user_data['messages']:
            if msg['role'] == 'user':
                conversation += f"User: {msg['content']}\n"
            else:
                conversation += f"HealthBot: {msg['content']}\n"
        prompt = f"""You are HealthBot, a friendly AI health assistant for the Health Monitor app.
Help users with general health questions, symptoms, nutrition, and wellness tips.
Be warm, use simple language, use emojis, keep responses concise.
Never diagnose diseases. Always suggest consulting a doctor for serious issues.
If emergency, urge to call emergency services immediately.

Conversation:
{conversation}
HealthBot:"""
        response = req_lib.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500
            },
            timeout=30
        )
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except req_lib.exceptions.RequestException as e:
        print("Groq API error:", str(e))
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print("Chat error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)