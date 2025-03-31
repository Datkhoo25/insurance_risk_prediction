from app import app
import requests
import json
import numpy as np
import pickle
import pandas as pd

# Load the original data in order to create a test data
raw_data_path = r"C:\Users\lucas\PycharmProjects\pythonProject4\risk_prediction\train.csv"
raw_df = pd.read_csv(raw_data_path, index_col='Id')

# Drop the last column
raw_df = raw_df.iloc[:, :-1]

# Function to generate fake data
def generate_fake_data(df, num_samples):
    fake_data = {}

    for column in df.columns:
        if df[column].dtype == 'object':
            # For categorical columns, sample from the unique values
            fake_data[column] = np.random.choice(df[column].unique(), num_samples)
        elif df[column].dtype == 'int64':
            # For integer columns, sample from the range of values and convert to int
            fake_data[column] = np.random.randint(df[column].min(), df[column].max() + 1, num_samples)
        elif df[column].dtype == 'float64':
            # For float columns, sample from the range of values
            fake_data[column] = np.random.uniform(df[column].min(), df[column].max(), num_samples)

    # Convert the dictionary to a DataFrame
    fake_data_df = pd.DataFrame(fake_data)

    return fake_data_df

# Generate fake data
num_samples = 100  # Number of fake samples to generate
fake_data_df = generate_fake_data(raw_df, num_samples)

# Ensure the fake data has the same columns as the original data
fake_data_df = fake_data_df[raw_df.columns]

# Define the URL for your API (running locally)
url = "http://127.0.0.1:5000/predict"

# Function to send data to the API and get the prediction
def get_prediction(data):
    try:
        response = requests.post(url, json=data)

        # Check if the response is successful
        if response.status_code == 200:
            prediction = response.json()  # Get the prediction result
            print(f"Prediction: {prediction['prediction']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Loop through each fake data sample and make predictions
for index, row in fake_data_df.iterrows():
    data = row.to_dict()  # Convert the row to a dictionary
    print(f"Predicting for row {index}: {data}")
    get_prediction(data)




def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert (response.data > 0) AND (response.data < 7)