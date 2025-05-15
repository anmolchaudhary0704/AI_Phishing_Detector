from flask import Flask, request, render_template, jsonify
import joblib
from url_feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load('model/phishing_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)