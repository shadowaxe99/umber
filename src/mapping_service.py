```python
import googlemaps
from datetime import datetime

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def get_distance_duration(origin, destination):
    """
    Function to get distance and duration between two points
    """
    now = datetime.now()
    directions_result = gmaps.directions(origin, destination, departure_time=now)

    distance = directions_result[0]['legs'][0]['distance']['text']
    duration = directions_result[0]['legs'][0]['duration']['text']

    return distance, duration

def get_real_time_location(driver_id):
    """
    Function to get real-time location of a driver
    """
    # This is a placeholder function. In a real-world application, you would integrate with a GPS tracking system
    # to get the real-time location of the driver.
    pass

def get_eta(pickup_location, driver_location):
    """
    Function to get estimated time of arrival (ETA) of the driver to the pickup location
    """
    _, duration = get_distance_duration(driver_location, pickup_location)
    return duration
```