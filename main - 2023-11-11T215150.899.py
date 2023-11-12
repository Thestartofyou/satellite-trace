from skyfield.api import Topos, load
from datetime import datetime

# Load satellite data
ts = load.timescale()
planets = load('de421.bsp')
earth, satellite = planets['earth'], planets['tle']

# Replace 'YOUR_TLE_LINE1' and 'YOUR_TLE_LINE2' with actual TLE (Two-Line Element) data
tle_line1 = 'YOUR_TLE_LINE1'
tle_line2 = 'YOUR_TLE_LINE2'

# Create satellite object
satellite = earth + satellite(line1=tle_line1, line2=tle_line2)

# Observer's location (replace with your coordinates)
observer = Topos(latitude_degrees=YOUR_LATITUDE, longitude_degrees=YOUR_LONGITUDE)

# Get current time
current_time = ts.now()

# Compute satellite position
satellite_at_time = observer.at(current_time).from_altaz(0, 0)

# Print satellite's current position
print(f"Satellite position at {current_time}: {satellite_at_time}")
