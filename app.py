from flask import Flask, request, render_template, jsonify
import joblib
import traceback
import pandas as pd


app = Flask(__name__)

# Load the preprocessor and model at the start of your application
preprocessor = joblib.load('preprocessor.joblib')
model = joblib.load('random_forest_model.joblib')

@app.route('/')
def home():
    # Render the HTML form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        feature_dict = request.form.to_dict()

        # Create the DataFrame with the same structure as your training data
        features_df = pd.DataFrame([feature_dict])

        # Preprocess the input features
        preprocessed_features = preprocessor.transform(features_df)

        # Predict the price with the model (use 'model', not 'loaded_rf_model')
        prediction = model.predict(preprocessed_features)

        # Format the prediction for output
        output = round(prediction[0], 2)
        print(f"Prediction text: {output}")
        # Return the prediction to the client
        return render_template('index.html', prediction_text=f'Estimated Diamond Price: ${output}')

    except Exception as e:
        # Handle any errors that occur during the prediction process
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})
if __name__ == '__main__':
    app.run(debug=True)
