from flask import Flask, request, jsonify
import os
from utils import load_model, validate_input, format_prediction, handle_exception

app = Flask(__name__)

# Define the path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Load the model at startup
try:
    model = load_model(MODEL_PATH)
    # Extract the feature names expected by the model's preprocessor
    numerical_cols = model.named_steps['preprocessor'].transformers_[0][2]
    categorical_cols = model.named_steps['preprocessor'].transformers_[1][2]
    expected_features = numerical_cols + categorical_cols
    print("Model and features loaded successfully.")
except Exception as e:
    # If the model fails to load, log the error and exit
    print(f"Failed to load the model: {e}")
    exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        data = request.get_json(force=True)
        features = data.get('features', {})

        # Validate and extract feature values
        feature_values = validate_input(features, expected_features)

        # Make prediction using the model
        prediction = model.predict([feature_values])

        # Format the prediction for response
        result = format_prediction(prediction)

        return jsonify(result)

    except Exception as e:
        # Handle exceptions and return error message
        error_message = handle_exception(e)
        return jsonify(error_message), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)