import pandas as pd

datetime_string = ['12/01/2010 08:26','12/02/2010 16:38','12/03/2010 12:24','12/05/2010 10:03','12/05/2010 10:03']

# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(datetime_string, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(index=my_datetimes)
