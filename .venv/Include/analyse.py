import jpype
import pyNetlogo
import time

# Initialize the NetLogo model
def initialize_nlogo_model():
    netlogo = pyNetLogo.NetLogoLink()
    netlogo.load_model("netlogo/UrbanTransportationSystem.nlogo")
    return netlogo

# Setup the model
def setup_model(netlogo):
    netlogo.command('s                                                                                              etup')  # This will call the NetLogo setup procedure

# Run the model simulation
def run_simulation(netlogo, ticks=100):
    for tick in range(ticks):
        netlogo.command('go')  # This calls the go procedure in your NetLogo model
        time.sleep(0.5)  # Add a small delay to avoid overwhelming the NetLogo engine

# Collect data (e.g., average taxi carrying rate, average bus carrying number, etc.)
def collect_data(netlogo):
    # Retrieve average taxi carrying rate
    avg_taxi_carrying_rate = netlogo.report('analyze-taxi')
    print(f"Average Taxi Carrying Rate: {avg_taxi_carrying_rate}%")

    # Retrieve average bus carrying number
    avg_bus_carrying_number = netlogo.report('analyze-bus')
    print(f"Average Bus Carrying Number: {avg_bus_carrying_number}")

    # Retrieve average commuting time
    avg_commuting_time = netlogo.report('analyze-citizen')
    print(f"Average Commuting Time: {avg_commuting_time} minutes")

# Example of how to use the functions
def main():
    # Initialize the NetLogo model
    netlogo = initialize_nlogo_model()

    # Setup the model
    setup_model(netlogo)

    # Run the simulation for 100 ticks
    run_simulation(netlogo, ticks=100)

    # Collect and print data
    collect_data(netlogo)

    # Close the NetLogo link after simulation
    netlogo.command('reset-ticks')
    netlogo.command('clear-all')
    netlogo.command('exit')

# Run the main function
if __name__ == "__main__":
    main()
