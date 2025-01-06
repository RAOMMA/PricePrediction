import joblib
import pandas as pd
import argparse

# Load your encoder and model
encoder = joblib.load('C:/salman/ML/House_Price_Prediction/data.joblib')
loaded_model = joblib.load('C:/salman/ML/House_Price_Prediction/model.joblib')

def predict_price(args):
    # Convert command-line arguments to a dictionary
    input_data = {
        'area': args.area,
        'bedrooms': args.bedrooms,
        'bathrooms': args.bathrooms,
        'stories': args.stories,
        'mainroad': args.mainroad,
        'guestroom': args.guestroom,
        'basement': args.basement,
        'hotwaterheating': args.hotwaterheating,
        'airconditioning': args.airconditioning,
        'parking': args.parking,
        'prefarea': args.prefarea,
        'furnishingstatus': args.furnishingstatus
    }

    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Transform the input data using the encoder
    x = encoder.transform(input_df)

    # Make predictions
    pred = loaded_model.predict(x)
    return pred[0]

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='Predict house price')
    parser.add_argument('--area', type=int, help='Area of the house')
    parser.add_argument('--bedrooms', type=int, help='Number of bedrooms')
    parser.add_argument('--bathrooms', type=int, help='Number of bathrooms')
    parser.add_argument('--stories', type=int, help='Number of stories')
    parser.add_argument('--mainroad', type=str, help='Main road accessibility (yes/no)')
    parser.add_argument('--guestroom', type=str, help='Presence of guest room (yes/no)')
    parser.add_argument('--basement', type=str, help='Presence of basement (yes/no)')
    parser.add_argument('--hotwaterheating', type=str, help='Hot water heating (yes/no)')
    parser.add_argument('--airconditioning', type=str, help='Air conditioning (yes/no)')
    parser.add_argument('--parking', type=int, help='Number of parking spaces')
    parser.add_argument('--prefarea', type=str, help='Preferred area (yes/no)')
    parser.add_argument('--furnishingstatus', type=str, help='Furnishing status')

    args = parser.parse_args()

    # Call the predict_price function with the parsed arguments
    prediction = predict_price(args)
    print(f"Predicted house price: {prediction}")
python 