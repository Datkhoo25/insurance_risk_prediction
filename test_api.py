from app import app
import requests
import json
import numpy as np
import pickle
import pandas as pd

import pandas as pd
import numpy as np
import requests
import random

# Load the dataset (ensure it exists locally)
df = pd.read_csv("test.csv")

# API endpoint
API_URL = "http://127.0.0.1:5000/predict"  # Adjust if running remotely


# Function to get predictions from the API
def get_prediction(data):
    try:
        # Replace NaNs with None (JSON-compliant)
        data = {key: (None if pd.isna(value) else value) for key, value in data.items()}

        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            return response.json().get("prediction", None)
    except Exception as e:
        print(f"Error fetching prediction: {e}")
    return None


# Initialize prediction column
predictions = []
df = df.head(1000)

# Process 50% real API predictions and 50% random numbers
for index, row in df.iterrows():
    if random.random() < 0.5:  # 50% chance
        pred = get_prediction(row.to_dict())  # API prediction
    else:
        pred = np.random.randint(1, 9)  # Random number between 1 and 8
    predictions.append(pred)

# Add predictions to the dataframe
df["prediction"] = predictions  # ✅ Assign only to first 1000 rows


# Save locally before uploading
df.to_csv("test1_with_predictions.csv", index=False)
print("✅ File saved: test1_with_predictions.csv")




# # Load the original data in order to create a test data
# GITHUB_RAW_URL = "https://raw.githubusercontent.com/Datkhoo25/insurance_risk_prediction/main/test.csv"
# raw_df = pd.read_csv(GITHUB_RAW_URL, index_col='Id')
#
#
# # Define the URL for your API (running locally)
# url = "http://127.0.0.1:5000/predict"
#
# # Function to send data to the API and get the prediction
# def get_prediction(data):
#     try:
#         response = requests.post(url, json=data)
#
#         # Check if the response is successful
#         if response.status_code == 200:
#             prediction = response.json()  # Get the prediction result
#             print(f"Prediction: {prediction}")
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#
# # Loop through each fake data sample and make predictions
# for index, row in raw_df.iterrows():
#     data = row.to_dict()  # Convert the row to a dictionary
#     print(f"Predicting for row {index}: {data}")
#     get_prediction(data)
#
#
#
# #
# # def test_home():
# #     response=app.test_client().get("/")
# #
# #     assert response.status_code==200
# #     assert (response.data > 0) AND (response.data < 7)