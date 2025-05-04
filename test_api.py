import requests
import pandas as pd

# API URL for local server
API_URL = "http://127.0.0.1:8080/predict"

# Load the original data (ensure it exists locally)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/Datkhoo25/insurance_risk_prediction/main/test.csv"
raw_df = pd.read_csv(GITHUB_RAW_URL, index_col='Id')


# Function to handle NaN values (replace with None)
def clean_data(data):
    return {key: (None if pd.isna(value) else value) for key, value in data.items()}


# Function to send data to the API and get the prediction
def get_prediction(data):
    try:
        # Clean the data by replacing NaN with None
        cleaned_data = clean_data(data)

        response = requests.post(API_URL, json=cleaned_data)

        # Check if the response is successful
        if response.status_code == 200:
            prediction = response.json()  # Get the prediction result
            return prediction.get("prediction", None)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None


# Test 1: Ensure predictions are within the range 1-8
def test_prediction_range():
    df = raw_df
    """Test that the predictions are within the range [1, 8]."""
    for i, row in df.head(1000).iterrows():  # Test only first 1000 rows
        # Separate the features (X) from the target (Y)
        data = row.drop("prediction").to_dict()  # Drop the 'prediction' column (assuming it's the target)

        prediction = get_prediction(data)
        print(data)
        print(prediction)
        # Check if prediction is within range 1-8
        assert prediction is not None, f"Prediction is None for row {i}"
        assert 1 <= prediction <= 8, f"Prediction {prediction} for row {i} is out of range"

    print("✅ Test 1 passed: All predictions are within range 1-8.")


# Test 2: Ensure at least 50% accuracy on a sample of 1000 rows
def test_sample_accuracy():
    df = raw_df
    """Ensure the model has at least 50% accuracy on a sample set."""
    num_correct = 0
    num_samples = 1000  # Test on 1000 samples

    for i in range(num_samples):
        # Separate the features (X) from the target (Y)
        data = df.iloc[i].drop("prediction").to_dict()  # Drop the 'prediction' column (assuming it's the target)

        prediction = get_prediction(data)

        if prediction is not None:
            ground_truth = df.iloc[i]["prediction"]  # Assuming 'prediction' column is ground truth
            if abs(prediction - ground_truth) <= 0.5:  # Tolerance: prediction is close to ground truth
                num_correct += 1

    accuracy = num_correct / num_samples
    assert accuracy >= 0.5, f"Accuracy {accuracy} is below 50%!"  # Ensure at least 50% accuracy
    print(f"✅ Test 2 passed: Accuracy is {accuracy * 100:.2f}%")


# Run the tests
if __name__ == "__main__":
    test_prediction_range(raw_df)  # Test predictions in the correct range
    test_sample_accuracy(raw_df)  # Test model accuracy on 1000 samples
