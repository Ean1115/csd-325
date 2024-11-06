import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys
import os

def plot_temperatures(dates, temperatures, title, color):
    """Plot temperatures with given dates and color."""
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def read_temperatures(filename, temp_index):
    """Read dates and temperatures from a CSV file."""
    dates, temps = [], []
    try:
        # Get the current working directory
        script_dir = os.getcwd()  # Changed this line to use os.getcwd()
        # Join the script's directory with the filename
        file_path = os.path.join(script_dir, filename) 
        with open(file_path) as f: # Open the file using the absolute path
            reader = csv.reader(f)
            header_row = next(reader)

            # ... (rest of the function remains the same)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    temp = int(row[temp_index])
                    temps.append(temp)
                except ValueError:
                    print(f"Missing or invalid data for {row}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
        # Instead of sys.exit(), raise the exception again or handle it differently.
        # Here, we print a more helpful message and return empty lists.
        print(f"Please ensure 'sitka_weather_2018_simple.csv' is in the same directory as this script: {script_dir}") 
        return [], [] # Return empty lists to indicate failure

    return dates, temps

def main():
    filename = 'sitka_weather_2018_simple.csv'
    while True:
        print("\nMenu:")
        print("1. Highs")
        print("2. Lows")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dates, highs = read_temperatures(filename, 5)
            # Check if data was read successfully
            if dates and highs: 
                plot_temperatures(dates, highs, "Daily high temperatures - 2018", 'red')
            else:
                print("Could not plot highs due to file error.")
        elif choice == '2':
            dates, lows = read_temperatures(filename, 6)
            # Check if data was read successfully
            if dates and lows:
                plot_temperatures(dates, lows, "Daily low temperatures - 2018", 'blue')
            else:
                print("Could not plot lows due to file error.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()