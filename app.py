from flask import Flask, request, jsonify
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model and scaler
with open('iris_logistic_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('iris_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define a route for the classification
@app.route('/classify', methods=['GET','POST'])
def classify_iris():
    if request.method == 'GET':
        return "You sent a GET request."
    elif request.method == 'POST':
        
        try:
            # Get the input data from the request
            data = request.json
            sepal_length_cm = data['sepal_length_cm']
            sepal_width_cm = data['sepal_width_cm']
            petal_length_cm = data['petal_length_cm']
            petal_width_cm = data['petal_width_cm']

            # Prepare the input for prediction
            sample = np.array([[sepal_length_cm, sepal_width_cm, petal_length_cm, petal_width_cm]])
            sample = scaler.transform(sample)
            
            # Predict the class
            prediction = model.predict(sample)
            
            # Map the prediction to the iris species name
            iris_species = ['setosa', 'versicolor', 'virginica']
            predicted_label = iris_species[prediction[0]]
            
            # Return the result as JSON
            return jsonify({
                'predicted_label': predicted_label
            })

        except Exception as e:
            return jsonify({
                'error': str(e)
            })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
