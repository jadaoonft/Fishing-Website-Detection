from flask import Flask, render_template, request
import joblib
import cv2
import re

from feature_extractor import extract_url_features, get_reasons


app = Flask(__name__)

model = joblib.load("model.pkl")


def predict_url(url):

    features = extract_url_features(url)

    prediction = model.predict([features])[0]

    probability = model.predict_proba([features])[0][1] * 100

    reasons = get_reasons(url)

    if prediction == 1:
        result = "PHISHING / SUSPICIOUS"
        risk = "HIGH RISK"
    else:
        result = "LEGITIMATE"
        risk = "LOW RISK"

    return result, risk, round(probability, 2), reasons


def analyze_sms(message):

    suspicious_words = [
        "urgent",
        "verify",
        "blocked",
        "winner",
        "prize",
        "otp",
        "password",
        "click",
        "bank",
        "account",
        "claim"
    ]

    message_lower = message.lower()

    detected = []

    for word in suspicious_words:
        if word in message_lower:
            detected.append(word)

    urls = re.findall(
        r"https?://[^\s]+|www\.[^\s]+",
        message
    )

    score = len(detected) * 10

    if urls:
        score += 30

    score = min(score, 100)

    if score >= 60:
        result = "PHISHING / SUSPICIOUS"
        risk = "HIGH RISK"
    elif score >= 30:
        result = "SUSPICIOUS"
        risk = "MEDIUM RISK"
    else:
        result = "LIKELY SAFE"
        risk = "LOW RISK"

    return result, risk, score, detected, urls


def scan_qr(image_path):

    image = cv2.imread(image_path)

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    return data


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    risk = None
    probability = None
    reasons = []
    sms_detected = []
    qr_url = None

    if request.method == "POST":

        mode = request.form.get("mode")

        if mode == "url":

            url = request.form.get("url")

            if url:
                result, risk, probability, reasons = predict_url(url)

        elif mode == "sms":

            message = request.form.get("message")

            if message:

                result, risk, probability, sms_detected, urls = analyze_sms(message)

                reasons = [
                    "Detected: " + word
                    for word in sms_detected
                ]

                if urls:
                    reasons.append("Message contains a URL")

        elif mode == "qr":

            file = request.files.get("qr_image")

            if file:

                path = "qr_temp.png"
                file.save(path)

                qr_url = scan_qr(path)

                if qr_url:

                    result, risk, probability, reasons = predict_url(qr_url)

                else:

                    result = "QR CODE NOT DETECTED"
                    risk = "UNKNOWN"
                    probability = 0

                    reasons = [
                        "Unable to decode the QR image"
                    ]

    return render_template(
        "index.html",
        result=result,
        risk=risk,
        probability=probability,
        reasons=reasons,
        qr_url=qr_url
    )


if __name__ == "__main__":
    app.run(debug=True)