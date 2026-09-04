from datetime import datetime
import re

hourly_counts = {}

with open("Apache_2k.log", "r") as file:
    for line in file:
        if "[error]" in line:
            match = re.search(r"\[(.*?)\]", line)
            timestamp = match.group(1)
            dt = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
            hour_key = dt.strftime("%Y-%m-%d %H:00")

            if hour_key in hourly_counts:
                hourly_counts[hour_key] += 1
            else:
                hourly_counts[hour_key] = 1

print(hourly_counts)