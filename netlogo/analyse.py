import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the correct file path to the CSV file
file_path = 'C:/Users/Hp/Desktop/prjt-traffic/traffic_management/netlogo/simulation_results.csv'

# Function to check if the file exists and then load it
def load_data(file_path):
    if os.path.exists(file_path):  # Check if the file exists
        try:
            # Load the CSV data using pandas
            data = pd.read_csv(file_path)
            print("File loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading file: {e}")
    else:
        print(f"Error: The file at {file_path} does not exist. Please verify the file path.")
        return None

# Load the data
data = load_data(file_path)

# If the data is successfully loaded, perform analysis
if data is not None:
    # Remove the 'average_bus_occupancy' column
    data = data.drop(columns=['average_bus_occupancy'], errors='ignore')
    
    # Display the first few rows of the data
    print(data.head())

    # Summary statistics
    print("Summary statistics of the dataset:")
    print(data.describe())

    # --- General Analysis ---
    # 1. Plotting the average taxi occupancy over time (tick)
    plt.figure(figsize=(10, 6))
    plt.plot(data['tick'], data['average_taxi_occupancy'], color='blue', label='Average Taxi Occupancy')
    plt.title('Average Taxi Occupancy Over Time', fontsize=14)
    plt.xlabel('Time (Ticks)', fontsize=12)
    plt.ylabel('Average Taxi Occupancy', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

    # 3. Histogram of taxi occupancy
    plt.figure(figsize=(8, 5))
    plt.hist(data['average_taxi_occupancy'].dropna(), bins=30, color='purple', edgecolor='black')
    plt.title('Distribution of Taxi Occupancy', fontsize=14)
    plt.xlabel('Average Taxi Occupancy', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()

    # 4. Correlation Heatmap to show relationships between variables
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap', fontsize=14)
    plt.show()

    # --- Citizens' Behavior Analysis ---
    # 2. Identifying peak times: Which ticks show the highest taxi occupancy
    peak_times = data[data['average_taxi_occupancy'] == data['average_taxi_occupancy'].max()]
    print("Peak Times for Taxi Occupancy:")
    print(peak_times[['tick', 'average_taxi_occupancy']])

else:
    print("Unable to proceed with analysis due to missing file.")
