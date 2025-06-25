from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
# Ensure 'random_forest_model.pkl' is a trained RandomForestRegressor
model = joblib.load('random_forest_model.pkl')
# scaler = joblib.load('scaler.pkl')  # If used

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['bedrooms']),
            float(request.form['bathrooms']),
            float(request.form['sqft_living']),
            float(request.form['sqft_lot']),
            float(request.form['floors']),
            float(request.form['waterfront']),
            float(request.form['view']),
            float(request.form['condition']),
            float(request.form['sqft_above']),
            float(request.form['sqft_basement']),
            float(request.form['yr_built'])
        ]

        final_features = np.array(features).reshape(1, -1)
        # final_features = scaler.transform(final_features)  # If scaled

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted House Price: ${output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
