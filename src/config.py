"""
Constants and file paths
"""

MANAGE = "aggregate"    # "mean", "max", "weigthed"

parameters = {
                "format": "netcdf"

}

standard_col_names = {
                        "datetime": ["DateTime", "Datetime", "Date-Time", "Date", "Time", "Timestamp", "time"],
                        "temperature": ["Temperature", "Temp", "temp"],
                        "latitude": ["Latitude", "lat", "Lat"],
                        "longitude": ["Longitude", "long", "Long", "lon", "Lon"]

}