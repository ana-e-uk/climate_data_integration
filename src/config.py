"""
Constants and file paths
"""

METADATA = '/Users/bean/Documents/Doctorate/Fall_24/Mokbel8735_Adv_Databases/climate_data_integration/data/metadata/metadata.json'

MANAGE = "aggregate"    # "mean", "max", "weigthed"
TIME = "datetime"
LAT = "latitude"
LONG = "longitude"
VAR = "sea_ice_temp"

parameters = {
                "format": "netcdf"

}

standard_col_names = {
                        "datetime": ["datetime", "DateTime", "Datetime", "Date-Time", "Date", "Time", "Timestamp", "time"],
                        "temperature": ["temperature", "Temperature", "Temp", "temp"],
                        "latitude": ["latitude", "Latitude", "lat", "Lat"],
                        "longitude": ["longitude", "Longitude", "long", "Long", "lon", "Lon"],
                        "sea_ice_temp": ["sea_ice_temp", "icec", "sic"]

}