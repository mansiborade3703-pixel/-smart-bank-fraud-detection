
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('../models/fraud_model.pkl','rb'))

@app.route('/')
def home():
    return "Smart Bank Fraud Detection API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Dummy response
    return jsonify({"fraud_prediction":0, "risk_score":0.25})

if __name__ == "__main__":
    app.run(debug=True)
