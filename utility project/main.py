import os
import pandas as pd
from sklearn.linear_model import LinearRegression

CSV_FILE = "utility_usage_data.csv"
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        data = {
            "Month_Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "Occupants": [2, 3, 2, 4, 3, 5, 2, 4, 3, 4],
            "Electricity_Bill": [150, 210, 160, 290, 220, 360, 155, 300, 225, 295]
        }

        df = pd.DataFrame(data)
        df.to_csv(CSV_FILE, index=False)
        print("[System] Sample dataset created successfully.\n")


def add_or_update_data():

    print("\n----- Add / Update Utility Data -----")

    try:
        month = int(input("Enter Month Number (1-12): "))

        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")

        occupants = int(input("Enter Number of Occupants: "))

        if occupants <= 0:
            raise ValueError("Occupants must be greater than 0.")

        bill = float(input("Enter Electricity Bill (Units): "))

        if bill <= 0:
            raise ValueError("Bill must be positive.")

        df = pd.read_csv(CSV_FILE)

        record = (
            (df["Month_Number"] == month) &
            (df["Occupants"] == occupants)
        )

        if record.any():
            df.loc[record, "Electricity_Bill"] = bill
            print("\nRecord updated successfully.")
        else:
            new_row = pd.DataFrame({
                "Month_Number": [month],
                "Occupants": [occupants],
                "Electricity_Bill": [bill]
            })

            df = pd.concat([df, new_row], ignore_index=True)
            print("\nNew record added successfully.")

        df.to_csv(CSV_FILE, index=False)

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Error:", e)


def predict_usage():

    print("\n----- Predict Utility Usage -----")

    try:
        df = pd.read_csv(CSV_FILE)

        if len(df) < 3:
            print("Not enough data for prediction.")
            return

        X = df[["Month_Number", "Occupants"]]
        y = df["Electricity_Bill"]

        model = LinearRegression()
        model.fit(X, y)

        month = int(input("Enter Target Month (1-12): "))
        occupants = int(input("Enter Number of Occupants: "))

        if month < 1 or month > 12:
            raise ValueError("Invalid Month.")

        if occupants <= 0:
            raise ValueError("Invalid Occupants.")

        prediction = model.predict([[month, occupants]])

        print("\nPredicted Electricity Bill: {:.2f} Units".format(prediction[0]))

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Prediction Error:", e)


def view_data():

    print("\n----- Current Dataset -----")

    try:
        df = pd.read_csv(CSV_FILE)

        if df.empty:
            print("Dataset is empty.")
        else:
            print(df.to_string(index=False))

    except FileNotFoundError:
        print("Dataset not found.")

    except Exception as e:
        print("Error:", e)


def main_menu():

    initialize_csv()

    while True:

        print("\n" + "=" * 50)
        print("     UTILITY USAGE PREDICTION TOOL (ML)")
        print("=" * 50)
        print("1. View Current Dataset")
        print("2. Add / Update Usage Data")
        print("3. Predict Electricity Bill")
        print("4. Exit")
        print("=" * 50)

        choice = input("Select an option (1-4): ")

        if choice == "1":
            view_data()

        elif choice == "2":
            add_or_update_data()

        elif choice == "3":
            predict_usage()

        elif choice == "4":
            print("\nThank you for using the application.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
