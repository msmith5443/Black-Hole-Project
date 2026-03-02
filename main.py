import pandas as pd

def print_menu():
    print("1. Print all rows and columns")
    print("2. Print the shape of the dataset")
    print("3. Print the name of the columns")
    print("4. Print the value count of the 'class' column")
    print("5. Print overall dataset statistics")
    print("6. Print null values in each column")
    print("7. Drop null values and print the dataset")
    print("8. Map 'class' column to 1 for TDE and 0 for Non-TDE and print the dataset")
    print("9. Exit")

def handle_user_input(choice):
    if choice == "1":
        print(data)

    elif choice == "2":
        print(f"rows and colums: {data.shape}")

    elif choice == "3":
        print(data.columns)

    elif choice == "4":
        print(data["class"].value_counts())

    elif choice == "5":
        print(data.describe())

    elif choice == "6":
        print(data.isnull().sum())

    elif choice == "7":
        data_dropped = data.dropna()
        print(data_dropped)

    elif choice == "8":
        data_mapped = data.copy()
        data_mapped["class"] = data_mapped["class"].map({"Non-TDE": 0, "TDE": 1})
        print(data_mapped)

    elif choice == "9":
        print("Exiting...")

    else:
        print("Invalid choice. Please try again.")

data = pd.read_csv("tde_sample_dataset.csv")

print_menu()    
input = input()
handle_user_input(input)