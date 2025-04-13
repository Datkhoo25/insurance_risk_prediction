Installing Dependencies
Clone the repository:
bash
Copy
Edit
git clone https://github.com/Datkhoo25/insurance_risk_prediction.git
cd insurance_risk_prediction
Set up a virtual environment:
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Linux or macOS
venv\Scripts\activate  # On Windows
Install required Python dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Workflow Overview
Step 1: Model Training
The machine learning model is trained on a dataset (train.csv) containing features related to the risk of insurance claims. The model used is XGBoost, a scalable and powerful model for prediction tasks.

Code Structure:
app.py: The main script to deploy the model as an API.

train.csv: Dataset for model training.

best_xgb_model.pkl: Trained XGBoost model (saved using pickle).

full_pipeline.pkl: Preprocessing pipeline used to transform input data before prediction.

Step 2: API Deployment(app.py)
The model is exposed as a Flask API. The /predict endpoint accepts JSON input data, preprocesses it, and returns a prediction.

Step 3: Version Control & Collaboration
The project uses Git for version control and GitHub as the hosting platform. Teams can work on different branches for feature development, and merge them once the feature is complete.

Git LFS is used to handle large files, such as the trained model (best_xgb_model.pkl), which exceeds GitHub’s file size limit of 100MB.

How to Use Git LFS (Important for large files):
Track large files with Git LFS: The model files are tracked using Git LFS to prevent issues with GitHub’s file size limits.

Clone the repository with LFS support: Ensure LFS is installed and tracked before cloning the repo.

To install Git LFS, follow instructions here: Git LFS Setup.

After installation, clone the repository and pull all LFS files:

bash
Copy
Edit
git lfs install
git clone https://github.com/Datkhoo25/insurance_risk_prediction.git
Using LFS in your workflow: When pushing or pulling files, LFS automatically manages large files. For example:

bash
Copy
Edit
git push origin main
git pull origin main
Untracked large files: If you add a large file that is not being tracked by LFS, you can stage it for LFS tracking using:

bash
Copy
Edit
git lfs track "*.pkl"
git add .gitattributes  # To commit the changes in .gitattributes
git add <file>
git commit -m "Add model to LFS"
Step 4: Pushing to GitHub
To share updates, push your changes to GitHub.

bash
Copy
Edit
git add .
git commit -m "Add model and preprocessing pipeline"
git push origin main
Step 5: Using Docker for Consistency
The application can be containerized using Docker, which ensures that the model works consistently in any environment (e.g., AWS, local machines).

Create Dockerfile: Define how to build and run the application.

Build Docker image: To containerize the application, build the image:

bash
Copy
Edit
docker build -t insurance-risk-prediction .
Run Docker container: After building the Docker image, run it to start the Flask API:

bash
Copy
Edit
docker run -p 5000:5000 insurance-risk-prediction

Team Collaboration (Other Users)
How to work with the repository:
Pull the latest changes from the main branch:

Ensure Git LFS is installed and track any new large files added to the repository.

Run the following command to fetch and pull LFS-tracked files:

bash
Copy
Edit
git pull origin main
Work on a feature or fix a bug: Create a new branch for your work.

bash
Copy
Edit
git checkout -b feature_branch
Commit your changes and push them to your feature branch.

bash
Copy
Edit
git add .
git commit -m "Add feature"
git push origin feature_branch
When your feature is ready for review, create a pull request on GitHub to merge your changes into the main branch.


To checkout the publish docker file, please:
bash
docker pull kkhdocker348//insurence_flasktest-app:latest
