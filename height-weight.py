from flask import Flask, request, jsonify, render_template
import pickle
from app import app


model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict():
    return render_template('height-weight.html')


@app.route('/predict',methods=['POST'])
def predict_weight():
    height = float(request.form['height'])
    gender = float(request.form['gender'])

    prediction = model.predict([[gender, height]])

    output = round(prediction[0], 2)
        
    return render_template('height-weight.html', weights = output)
    
if __name__ == "__main__":
    app.run()
