import csv
import math

def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

def find_nearest_hospital(user_lat, user_lon, hospitals):
    nearest_hospital = None
    min_distance = float('inf')
    
    for hospital in hospitals:
        lat = hospital['Latitude']
        lon = hospital['Longitude']
        
        distance = haversine_distance(user_lat, user_lon, lat, lon)
        
        if distance < min_distance:
            min_distance = distance
            nearest_hospital = hospital
    
    return nearest_hospital

# Read the CSV file and store hospital data
hospitals = []
with open('co_hospitals1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Check if Latitude and Longitude values are empty strings before converting to float
        if row['Latitude'] and row['Longitude']:
            hospitals.append({
                'Hospital Name': row['Hospital Name'],
                'Latitude': float(row['Latitude']),
                'Longitude': float(row['Longitude']),
                'Address': row['Address']
            })

# Get user input
user_lat = float(input("Enter your latitude: "))
user_lon = float(input("Enter your longitude: "))

# Find the nearest hospital
nearest_hospital = find_nearest_hospital(user_lat, user_lon, hospitals)

if nearest_hospital:
    print(f"The nearest hospital is: {nearest_hospital['Hospital Name']}")
    print(f"Address: {nearest_hospital['Address']}")
    print(f"Lattitude: {nearest_hospital['Latitude']}")
    print(f"Longitude: {nearest_hospital['Longitude']}")
else:
    print("No hospitals found.")



# # Read the CSV file and store hospital data
# hospitals = []
# with open('co_hospitals1.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         hospitals.append({
#             'Hospital Name': row['Hospital Name'],
#             'Latitude': float(row['Latitude']),
#             'Longitude': float(row['Longitude']),
#             'Address': row['Address']
#         })

# # Get user input
# user_lat = float(input("Enter your latitude: "))
# user_lon = float(input("Enter your longitude: "))

# # Find the nearest hospital
# nearest_hospital = find_nearest_hospital(user_lat, user_lon, hospitals)

# if nearest_hospital:
#     print(f"The nearest hospital is: {nearest_hospital['Hospital Name']}")
#     print(f"Address: {nearest_hospital['Address']}")
# else:
#     print("No hospitals found.")