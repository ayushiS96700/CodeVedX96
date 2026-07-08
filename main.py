
import os
import pandas as pd
from sklearn.linear_model import LinearRegression

CSV_FILE = "utility_usage_data.csv"

def initialize_csv():
    """Creates a default CSV file with sample training data if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        # Features: Month_Number (1-12), Occupants | Target: Electricity_Bill (Units)
        data = {
            'Month_Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'Occupants': [2, 3, 2, 4, 3, 5, 2, 4, 3, 4],
            'Electricity_Bill': [150, 210, 160, 290, 220, 360, 155, 300, 225, 295]
        }
        df = pd.DataFrame(data)
        df.to_csv(CSV_FILE, index=False)
        print(f"[System] Initialized new database: '{CSV_FILE}' with sample data.")

def add_or_update_data():
    """Handles CSV file operations to add or update records safely."""
    print("\n--- Add / Update Usage Data ---")
    try:
        month = int(input("Enter Month Number (1-12): "))
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
            
        occupants = int(input("Enter Number of Occupants: "))
        if occupants <= 0:
            raise ValueError("Occupants must be a positive number.")
            
        bill = float(input("Enter Electricity Bill (Units/Amount): "))
        if bill < 0:
            raise ValueError("Bill cannot be negative.")

        df = pd.read_csv(CSV_FILE)

        # Check if the record for this specific month and occupant count already exists to update it
        existing_record = df[(df['Month_Number'] == month) & (df['Occupants'] == occupants)]

        if not existing_record.empty:
            df.loc[(df['Month_Number'] == month) & (df['Occupants'] == occupants), 'Electricity_Bill'] = bill
            print("[Success] Existing record updated successfully.")
        else:
            new_data = pd.DataFrame([[month, occupants, bill]], columns=df.columns)
            df = pd.concat([df, new_data], ignore_index=True)
            print("[Success] New record added successfully.")

        df.to_csv(CSV_FILE, index=False)

    except ValueError as ve:
        print(f"[Input Error] Invalid entry: {ve}")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")

def predict_usage():
    """Trains a simple ML Linear Regression model and predicts utility costs."""
    print("\n--- Predict Utility Usage (ML) ---")
    try:
        if not os.path.exists(CSV_FILE):
            print("[Warning] No data available to train the model. Add data first.")
            return

        df = pd.read_csv(CSV_FILE)
        
        if len(df) < 3:
            print("[Warning] Insufficient data. Please add at least 3 historical data points.")
            return

        # Splitting Features (X) and Target (y)
        X = df[['Month_Number', 'Occupants']]
        y = df['Electricity_Bill']

        # Train a basic Linear Regression Model
        model = LinearRegression()
        model.fit(X, y)

        print("\nEnter target values for prediction:")
        pred_month = int(input("Target Month Number (1-12): "))
        pred_occupants = int(input("Target Number of Occupants: "))

        if not (1 <= pred_month <= 12) or pred_occupants <= 0:
            raise ValueError("Invalid target inputs provided.")

        # Make prediction
        prediction = model.predict([[pred_month, pred_occupants]])
        
        print("\n" + "="*40)
        print(f" Predicted Utility Bill: {prediction[0]:.2f} Units")
        print("="*40)

    except ValueError as ve:
        print(f"[Input Error] Prediction failed: {ve}")
    except Exception as e:
        print(f"[Error] Modeling error: {e}")

def view_data():
    """Displays current data stored in the CSV."""
    print("\n--- Current Dataset ---")
    try:
        df = pd.read_csv(CSV_FILE)
        if df.empty:
            print("The dataset is empty.")
        else:
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("No database file found. Choose option 1 or 2 to create one.")

def main_menu():
    """Main menu-driven console loop matching company workflows."""
    initialize_csv()
    while True:
        print("\n========================================")
        print("  UTILITY USAGE PREDICTION TOOL (V1.0) ")
        print("========================================")
        print("1. View Current Usage Data")
        print("2. Add / Update Usage Data")
        print("3. Predict Utility Usage (ML Model)")
        print("4. Exit")
        print("----------------------------------------")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            view_data()
        elif choice == '2':
            add_or_update_data()
        elif choice == '3':
            predict_usage()
        elif choice == '4':
            print("\nExiting application. Thank you!")
            break
        else:
            print("[Invalid Option] Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()