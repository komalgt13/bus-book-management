import mysql.connector
import random
from datetime import datetime, timedelta
from faker import Faker

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="KomalonmySQL",
    database="bus_management"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to execute an SQL query
def execute_query(query, values=None):
    cursor.execute(query, values)
    connection.commit()

# Function to generate random datetime within a range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Function to generate mock data for the agency_address table
def generate_agency_address_data(num_records, agency_ids):
    fake = Faker()
    agency_address_data = [1, "Dehradun", "Velmed", "Uttarakhand"]
    return agency_address_data

# Function to insert agency_address data into the database
def insert_agency_address_data(data):
    query = "INSERT INTO agency_address (agency_id, city, landmark, state) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the agency table
def generate_agency_data(num_records):
    fake = Faker()
    agency_data = ("bus_agency", 1, 2)

    return agency_data

# Function to insert agency data into the database
def insert_agency_data(data):
    query = "INSERT INTO agency (name, agency_id, total_buses) VALUES (%s, %s, %s))"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the amenities table
def generate_amenities_data(num_records, bus_ids):
    amenities_data = [(1, 1, 1, 0, 1), (2, 1, 0 , 1, 1)]

    return amenities_data

# Function to insert amenities data into the database
def insert_amenities_data(data):
    query = "INSERT INTO amenities (bus_id, bed_sheet, wifi, charging_points, blankets) VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the bus table
def generate_bus_data(num_records, agency_ids, route_ids, conductor_ids, driver_ids):
    fake = Faker()
    bus_data = [(1, 1, 10, 5, 1, 1, 1, 5), (1, 2, 10, 5, 2, 2, 2, 3)]
    return bus_data

# Function to insert bus data into the database
def insert_bus_data(data):
    query = "INSERT INTO bus (agency_id, bus_id, total_seats, available_seats, route_id, conductor_id, driver_id, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the conductor table
def generate_conductor_data(num_records, bus_ids, agency_ids):
    fake = Faker()
    conductor_data = [(1, 1, "mudit", "0987654321", 1), (2, 2, "mudit2", "0987654321", 1)]

    return conductor_data

# Function to insert conductor data into the database
def insert_conductor_data(data):
    query = "INSERT INTO conductor (conductor_id, bus_id, name, contact, agency_id) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the coupon table
def generate_coupon_data(num_records):
    coupon_data = (1, 100)

    return coupon_data

# Function to insert coupon data into the database
def insert_coupon_data(data):
    query = "INSERT INTO coupon (coupon_code, discount) VALUES (%s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the driver table
def generate_driver_data(num_records, bus_ids, agency_ids):
    fake = Faker()
    driver_data = [(1, 1, "komal", "0987654321", 1), (2, 1, "komal1", "0987654321", 2)]

    return driver_data

# Function to insert driver data into the database
def insert_driver_data(data):
    query = "INSERT INTO driver (bus_id, agency_id, name, contact, driver_id) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the location table
def generate_location_data(num_records, route_ids, bus_ids):
    fake = Faker()
    location_data = [(1, 1, 1, "roorkee", "13:00:00", "14:00:00"), (2, 2, 2, "muzzarfarnagar", "13:00:00", "14:00:00"), (3, 1, 1, "Dehradun", "13:00:00", "14:00:00"), (2, 1,1, "muzzafarnagar", "15:00:00", "15:30:00")]

    return location_data

# Function to insert location data into the database
def insert_location_data(data):
    query = "INSERT INTO location (location_id, route_id, bus_id, name_location, arrival_time, departure_time) VALUES (%s, %s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the payment table
def generate_payment_data(num_records, ticket_ids):
    fake = Faker()
    payment_data = (1, "online", 1, 1)

    return payment_data

# Function to insert payment data into the database
def insert_payment_data(data):
    query = "INSERT INTO payment (ticket_id, mode, status, payment_id) VALUES (%s,%s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the rating table
def generate_rating_data(num_records, bus_ids):
    rating_data = [(1, 5, 1), (2, 3, 2)]
    return rating_data

# Function to insert rating data into the database
def insert_rating_data(data):
    query = "INSERT INTO rating (bus_id, rating, user_id) VALUES (%s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the route table
def generate_route_data(num_records, bus_ids):
    route_data = [(1, 1), (2, 2)]

    return route_data

# Function to insert route data into the database
def insert_route_data(data):
    query = "INSERT INTO route (route_id, bus_id) VALUES (%s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the seat table
def generate_seat_data(num_records, bus_ids):
    seat_data = [(1, 1, "sleeper", 1, 100, 0, "F"), (1, 2, "sleeper", 1, 100, 0, "F"), (1, 3, "sleeper", 1, 100, 0, "F"), (1, 4, "sleeper", 1, 100, 0, "F"), (1, 5, "sleeper", 1, 100, 0, "F"), (1, 6, "seater", 1, 100, 0, "ANY"), (1, 7, "seater", 1, 100, 0, "ANY"), (1, 8, "seater", 1, 100, 0, "ANY"), (1, 9, "seater", 1, 100, 0, "ANY"), (1, 10, "seater", 1, 100, 0, "ANY"), (2, 1, "seater", 1, 100, 0, "ANY"), (2, 2, "seater", 1, 100, 0, "ANY"), (2, 3, "seater", 1, 100, 0, "ANY"), (2, 4, "seater", 1, 100, 0, "F"), (2, 2, "slepper", 1, 100, 0, "F")]

    return seat_data

# Function to insert seat data into the database
def insert_seat_data(data):
    query = "INSERT INTO seat (bus_id, seat_id, seat_type, availability, seat_price, age_criteria, gender_criteria) VALUES (%s, %s, %s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the ticket table
def generate_ticket_data(num_records, user_ids, coupon_codes):
    fake = Faker()
    ticket_data = (1, 1, 1000, 1, "2023, 1, 31, 13, 00, 00")
    return ticket_data

# Function to insert ticket data into the database
def insert_ticket_data(data):
    query = "INSERT INTO ticket (user_id, ticket_id, total_amount, coupon_code, date_time) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the user_address table
def generate_user_address_data(num_records, user_ids):
    fake = Faker()
    user_address_data = (1, "Dehradun", "lake", "uttarakhand")
    return user_address_data

# Function to insert user_address data into the database
def insert_user_address_data(data):
    query = "INSERT INTO user_address (user_id, city, landmark, state) VALUES (%s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the trip table
def generate_trip_data(num_records, user_ids, bus_ids, ticket_ids, locations, seats):
    fake = Faker()
    trip_data = (1, 1, 1, "Dehradun", "muzaffarnagar", 2, 1, "13:00:00", "14:00:00", "15:00:00")
    return trip_data

# Function to insert trip data into the database
def insert_trip_data(data):
    query = "INSERT INTO trip (user_id, bus_id, ticket_id, start, destination, seat_id, check_in_status, arrival_time, departure_time, reaching_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Function to generate mock data for the user table
def generate_user_data(num_records):
    fake = Faker()
    user_data = (1, "vandit", "m", 21)
    return user_data

# Function to insert user data into the database
def insert_user_data(data):
    query = "INSERT INTO user (user_id, name, gender, age) VALUES (%s, %s, %s)"
    execute_query(query, data)
    connection.commit()

# Generate and insert mock data for each table
num_records = 1 # You can adjust the number of records as needed

# Generate and insert data for the agency table
agency_data = generate_agency_data(num_records)
insert_agency_data(agency_data)

# Generate and insert data for the agency_address table
agency_ids = list(range(1, num_records + 1))
agency_address_data = generate_agency_address_data(num_records, agency_ids)
insert_agency_address_data(agency_address_data)

# Generate and insert data for the conductor table
conductor_data = generate_conductor_data(num_records, agency_ids)
insert_conductor_data(conductor_data)

# Generate and insert data for the driver table
driver_data = generate_driver_data(num_records, agency_ids)
insert_driver_data(driver_data)

# Generate and insert data for the route table
route_data = generate_route_data(num_records)
insert_route_data(route_data)


# Generate and insert data for the bus table
route_ids = [1, 2]
conductor_ids = [1, 2]
driver_ids = [1, 2]
bus_data = generate_bus_data(num_records, agency_ids, route_ids, conductor_ids, driver_ids)
insert_bus_data(bus_data)

# Generate and insert data for the amenities table
bus_ids = [1, 2]
amenities_data = generate_amenities_data(num_records, bus_ids)
insert_amenities_data(amenities_data)

# Generate and insert data for the user table
user_data = generate_user_data(num_records)
insert_user_data(user_data)

# Generate and insert data for the user_address table
user_address_data = generate_user_address_data(num_records)
insert_user_address_data(user_address_data)

# Generate and insert data for the coupon table
coupon_data = generate_coupon_data(num_records)
insert_coupon_data(coupon_data)

# Generate and insert data for the location table
location_data = generate_location_data(num_records, route_ids, bus_ids)
insert_location_data(location_data)

# Generate and insert data for the payment table
ticket_ids = [1]
payment_data = generate_payment_data(num_records, ticket_ids)
insert_payment_data(payment_data)

# Generate and insert data for the rating table
rating_data = generate_rating_data(num_records, bus_ids)
insert_rating_data(rating_data)

# Generate and insert data for the seat table
seat_data = generate_seat_data(num_records, bus_ids)
insert_seat_data(seat_data)

# Generate and insert data for the ticket table
ticket_data = generate_ticket_data(num_records)
insert_ticket_data(ticket_data)

# Generate and insert data for the trip table
trip_data = generate_trip_data(num_records, bus_ids, ticket_ids, location_data, seat_data)
insert_trip_data(trip_data)

# Close the database connection
connection.commit()
cursor.close()
connection.close()
