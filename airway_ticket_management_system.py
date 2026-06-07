import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import duckdb

data = pd.read_csv(r'C:\Users\Ram\Desktop\greentech data\Metro old data\personal\insurance\fees 2019-20\simran\airway_system\flights.csv')
df = pd.DataFrame(data)

# Current Location
location = input("Enter your current location: ")
# Destination
destination = input("Enter your destination: ")
# Date of Travel
date_of_travel = input("Enter your date of travel (YYYY-MM-DD): ")
# Departure Time
Dep_Time = input("Enter the departure time of the flight (e.g., 11:40): ")

sql_query = f"""
        SELECT * FROM df
        WHERE Source = '{location}' 
        AND Destination = '{destination}' 
        AND Date_of_Journey = '{date_of_travel}' 
        AND Dep_Time = '{Dep_Time}' ;
    """
matched_flights = duckdb.query(sql_query).df()
print("\nMatching flights found:")
print(matched_flights.to_string)


# Execute and get the result back as a clean Pandas DataFrame

matched_flights = duckdb.query(sql_query).df()
matched_flights = pd.DataFrame(matched_flights)
# --- HOW TO SHOW IT SAFELY ---
# Check if the query returned any data rows
if not matched_flights.empty:
    print("\nMatching flights found using SQL:")
    print(matched_flights.to_string(index=False))
else:
    print(f"\nNo flights found matching all your criteria.")


booking_flight = input("Enter the Flight Index of the flight you want to book: ")
sql_query = f"""
SELECT * FROM df where index = {booking_flight};
"""
booking = duckdb.query(sql_query).df()
booking = pd.DataFrame(booking)
booking.to_csv('bookings.csv')
print(booking)


