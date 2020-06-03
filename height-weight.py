from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict')
def predict():
    return render_template('height-weight.html')


@app.route('/predict_weight',methods=['GET', 'POST'])
def predict_weight():
    if request.method == 'POST':
        height = float(request.form['height'])
        gender = float(request.form['gender'])
        
        prediction = model.predict([[gender, height]])
        
        output = round(prediction[0], 2)
        
    return render_template('height-weight.html', weights = output)
    
if __name__ == "__main__":
    app.run()
