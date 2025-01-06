# House Price Prediction

## Overview

This project offers a machine-learning model that predicts house prices based on various features. It utilizes a Gradient Boosting Regressor trained on a curated dataset of housing information.


## Dataset

- **Dataset Name**: house price dataset
- **Data Source**: upload on git .
- The dataset contains the following attributes:
  - Feature columns (13): Numerical values representing various house price-related features.
  - Target column: price of houses.

## Project Structure

- `README.md`: Documentation of the project.
- `main.py`: Python script for making diabetes predictions.
- `data.joblib ` : weights of transformer used to transfer data before traning.
- `model.joblib`: Pre-trained logistic regression model for diabetes prediction.

## Setup

1. Clone the repository:
   ```shell
   git clone <repository-url>
   cd House Price Prediction
Create a virtual environment (recommended) and install the required dependencies:
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

## Usage
Clone this repository to your local machine.
Ensure you have the pre-trained logistic regression model ('model.pkl') in the same directory as the script ('diabetes_prediction.py').
Open a command prompt or terminal and navigate to the directory where the script is located.
Run the script with the --value argument followed by a comma-separated list of feature values that you want to classify.
## For example:
python main.py --value "6,148,72,35,0,33.6,0.627,50"

Follow the instructions in the script to make predictions.

## Model Training
The project uses a logistic regression model to predict the price of the house. The pre-trained model is saved as 'model.pkl'.

## Evaluation
The script provides binary predictions. You can evaluate the model's performance using metrics like accuracy, precision, and F2 score.

## Results
The project provides predictions for house prices based on the input features. The performance of the model may vary depending on the dataset used.

## Future Improvements
There are several ways to improve the model and the project:

Explore more advanced machine learning techniques.
Fine-tune hyperparameters for better model performance.
Gather more labeled data for improved accuracy.
References
Author: Mirza Salman
Contact: salmansaluu661@gmail.com
Feel free to customize this README to include any additional information you want to provide about the project.
