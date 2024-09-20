# IP Geolocator

This Python script utilizes the GeoIP2 library to get information about the geographical location of a given IP address. It extracts details such as the country, city, latitude, and longitude using the GeoLite database.

## Prerequisites

- Install the GeoIP2 library:
    ```bash
    pip install geoip2
    ```
- Download the GeoLite Database(.mmdb file format) by referring to this [MaxMind article](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data).
- In the script, enter the path to the Database file corresponding to `database_path`.

## Usage


1. Run the Script
2. Enter the IP address to look up as well as the Path to database file when prompted. 
3. Various parameters defining GeoLocation(Country, City, Latitude & Longitude) are returned.
