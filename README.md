# 🛡️ PhishShield AI

## AI-Based Multi-Channel Phishing Detection System

PhishShield AI is a machine-learning-based cybersecurity project designed to identify potentially suspicious phishing threats through multiple channels.

## 🚨 Problem Statement

Phishing attacks can reach users through malicious websites, SMS messages, and QR codes. Attackers may use these channels to trick users into clicking malicious links or providing sensitive information.

## 💡 Solution

PhishShield AI provides a unified platform that analyzes:

- 🌐 Website URLs
- 📱 SMS messages
- 📷 QR codes

The system provides a risk assessment and explains suspicious indicators detected during analysis.

## ✨ Features

- URL phishing detection
- SMS phishing analysis
- QR code URL extraction
- Machine learning prediction
- Risk score
- Explainable detection results
- Confusion matrix
- Accuracy evaluation
- Professional web interface

## 🧠 Machine Learning

The project uses a Random Forest classification model for URL-based phishing detection.

## 🏗️ System Architecture

User Input
↓
URL / SMS / QR
↓
Feature Extraction
↓
AI/ML Analysis
↓
Risk Assessment
↓
Prediction + Explanation

## 🛠️ Technologies

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- OpenCV
- HTML
- CSS
- JavaScript

## 📁 Project Structure

PhishShield-AI/
│
├── app.py
├── train_model.py
├── feature_extractor.py
├── requirements.txt
├── dataset.csv
├── templates/
│   └── index.html
└── static/
    └── style.css

## ▶️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project:

cd PhishShield-AI

Install dependencies:

pip install -r requirements.txt

Train the model:

python train_model.py

Run the application:

python app.py

Open the local Flask address shown in the terminal.

## ⚠️ Disclaimer

This project provides a machine-learning-based risk assessment and should not be treated as a guarantee that a website, message, or QR code is safe.

## 🚀 Future Scope

- Browser extension
- Real-time threat intelligence
- Email phishing detection
- Mobile application
- Advanced NLP models
- Continuous model retraining