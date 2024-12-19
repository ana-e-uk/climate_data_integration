"""
Constants and file paths
"""

MANAGE = "aggregate"    # "mean", "max", "weigthed"
TIME = "datetime"
LAT = "latitude"
LONG = "longitude"

parameters = {
                "format": "netcdf"

}

standard_col_names = {
                        "datetime": ["datetime", "DateTime", "Datetime", "Date-Time", "Date", "Time", "Timestamp", "time"],
                        "temperature": ["temperature", "Temperature", "Temp", "temp"],
                        "latitude": ["latitude", "Latitude", "lat", "Lat"],
                        "longitude": ["longitude", "Longitude", "long", "Long", "lon", "Lon"],
                        "sea_ice_temp": ["sea_ice_temp", "icec", "nv", "sic"]

}