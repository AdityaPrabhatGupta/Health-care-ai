# 🩺 Health Monitor AI

Health Monitor AI is an AI-assisted healthcare web application that combines a Flask backend with an interactive multi-page frontend to provide:

* AI-based disease prediction
* Conversational healthcare assistance
* BMI and wellness tracking
* Yoga and exercise guidance
* Health quizzes and rewards
* Wellness-focused educational content

Originally developed as an academic healthcare platform, the project was upgraded in March 2026 with improved UI, wellness modules, and an enhanced AI chatbot experience.

---

# 🚀 Features

## 🤖 AI Disease Prediction

Users can enter symptoms and receive disease predictions generated from a trained TensorFlow/Keras model.

### Highlights

* Multi-symptom prediction
* Neural-network-based classification
* Fast inference using saved `.keras` model

---

## 💬 AI Health Chatbot

An AI-powered healthcare chatbot integrated using the Groq API.

### Features

* Conversational health assistance
* Context-aware responses
* Concise wellness guidance
* Medical safety reminders

---

## 📊 BMI & Wellness Monitor

Interactive BMI calculator with personalized wellness suggestions.

### Includes

* BMI score calculation
* Health category classification
* Simple fitness recommendations

---

## 🧘 Yoga & Exercise Guidance

Wellness section with beginner-friendly exercises.

### Categories

* Yoga
* Cardio
* Breathing exercises
* Strength workouts

---

## 🧠 Health Quiz System

Interactive quiz module with:

* scoring system
* animated feedback
* wellness explanations

---

## 🎁 Rewards System

Gamified reward interface where users can simulate redeeming wellness rewards.

---

## 🍎 Food Recommendation Guide

Displays healthy Indian and continental food suggestions.

---

## 🔐 Frontend Login Experience

Simple login flow with:

* localStorage session handling
* personalized navbar state
* lightweight frontend authentication

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask
* Flask-CORS

## AI / Machine Learning

* TensorFlow / Keras
* scikit-learn
* Pandas
* NumPy

## APIs & Integrations

* Groq Chat Completions API

## Deployment

* Procfile
* runtime.txt

---

# 📂 Project Structure

```bash
Health-Care/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── disease_symptoms.csv
├── disease_prediction_model.keras
├── .env
│
└── Health-care-main/
    ├── Home.html
    ├── App.html
    ├── Chatbot.html
    ├── Monitor.html
    ├── Login.html
    ├── Feature.html
    ├── Food.html
    ├── Yoga.html
    ├── Quiz.html
    ├── Reward.html
    ├── Contact.html
    ├── About.html
    ├── App.css
    ├── App.js
    ├── Auth.js
    └── Images/
```

---

# ⚙️ Backend API Endpoints

## POST `/login`

Handles frontend login interaction.

### Example Request

```json
{
  "username": "user",
  "password": "password"
}
```

---

## POST `/predict`

Predicts disease from symptoms.

### Example Request

```json
{
  "symptoms": ["fever", "cough"]
}
```

---

## POST `/chat`

Processes chatbot conversation history and returns AI-generated health guidance.

---

# 🧠 How the System Works

## 1️⃣ Disease Prediction Pipeline

* Symptom data loaded from `disease_symptoms.csv`
* Symptoms encoded using `MultiLabelBinarizer`
* Neural network trained using TensorFlow/Keras
* Prediction returned as highest probability disease

---

## 2️⃣ AI Chatbot Workflow

* Frontend sends conversation history to `/chat`
* Backend constructs prompt
* Groq API generates response
* Response returned with safety disclaimer

---

## 3️⃣ Frontend Experience

* Multi-page responsive healthcare UI
* Shared styling via `App.css`
* Interactive wellness modules
* localStorage-based personalization

---

# 🖥️ Installation & Setup

## Prerequisites

* Python 3.11+
* GROQ API Key

---

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

### 6. Run Flask Server

```bash
python app.py
```

Server runs at:

```bash
http://localhost:7860
```

---

# 🔄 Frontend API Configuration

The frontend currently points to hosted Hugging Face endpoints.

To use local Flask APIs, update fetch URLs inside:

* `Health-care-main/App.html`
* `Health-care-main/Chatbot.html`
* `Health-care-main/Login.html`

Replace hosted URLs with:

```bash
http://localhost:7860
```

---

# ⚠️ Current Limitations

* Demo-style authentication
* No database integration
* Model retrains during startup
* Chatbot provides general guidance only
* Some UI encoding depends on editor encoding

---

# ✨ March 2026 Updates

* Improved UI/UX
* Added Yoga & Exercise section
* Added Quiz & Rewards system
* Integrated Groq-powered chatbot
* Improved login flow
* Added wellness-focused pages

---

# 🚀 Future Improvements

* Real authentication system
* Database integration
* Offline model training workflow
* Appointment booking system
* Better AI safety guardrails
* Unified frontend/backend deployment

---

# 👨‍💻 Author

**Aditya Prabhat Gupta ,
Ayush Singh ,
Bipin Singh ,
Aditya Singh**
B.Tech CSE (AI & ML) — RIT Roorkee

---

# ⚠️ Disclaimer

This project is for academic and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.
