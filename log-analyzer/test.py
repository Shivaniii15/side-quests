from datetime import datetime

timestamp = "Sun Dec 04 04:52:15 2005"
dt = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
print(dt)
print(dt.hour)