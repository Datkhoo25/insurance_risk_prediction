import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify


# Load the pipeline and model
def load_pipeline(pipeline_path):
    try:
        with open(pipeline_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        return None

def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


# ✅ Use raw strings or forward slashes in file paths
pipeline_path = r"full_pipeline.pkl"
model_path = r"best_xgb_model.pkl"

loaded_pipeline = load_pipeline(pipeline_path)
loaded_xgb_model = load_model(model_path)

# Function to preprocess input data
def preprocess_data(data):
    df = pd.DataFrame([data])  # Convert input to DataFrame
    transformed_df = loaded_pipeline.transform(df)  # Apply pipeline transformation
    return transformed_df

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Risk Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json(force=True)
        # Preprocess input data
        preprocessed_data = preprocess_data(data)
        # Make prediction
        prediction = loaded_xgb_model.predict(preprocessed_data)
        # Adjust prediction if necessary
        prediction_adjusted = prediction + 1
        # Return result as JSON
        return jsonify({'prediction': int(prediction_adjusted[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

# ✅ Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=8080)
