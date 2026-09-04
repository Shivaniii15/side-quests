import re
import logging
from datetime import datetime

#setting up the log file
logging.basicConfig(
    filename="analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize a dictionary to hold the counts of errors per hour
hourly_counts = {}

# Open the log file
try:
    file = open("Apache_2k.log", "r")
except FileNotFoundError as e:
    logging.error(f"Could not open log file: {e}") #error handling if the log file is not found
    exit()

# Read the log file line by line
for line in file:
    if "[error]" in line: # What we are looking for 
        try:
            # Extract the timestamp
            # ".*?" is a "lazy" match. it stops at the first "]" it finds, rather than
            # the last one, so we correctly grab just the date, not the whole line. 
            match = re.search(r"\[(.*?)\]", line)

            timestamp = match.group(1)
            #  e.g. "Sun Dec 04 04:52:15 2005"

            # Convert the timestamp text into a real Python datetime object,
            # so we can work with it as an actual date/time, not just a string.

            dt = datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
            hour_key = dt.strftime("%Y-%m-%d %H:00")
            
            # Increment the count for this hour, or start it at 1 if it's new.
            # Basically this function counts how many errors happened in each hour
            if hour_key in hourly_counts:
                hourly_counts[hour_key] += 1
            else:
                hourly_counts[hour_key] = 1
            pass
        except (AttributeError, ValueError) as e:
            # If we can't parse the line, log a warning and skip it.

            logging.warning(f"Skipped a malformed line: {e}")

file.close()

# Log a summary of the result (not the actual data)
logging.info(f"Finished processing. {len(hourly_counts)} unique hours found.")

# Print the final sorted report
# Sort the dictionary by hour.
for hour, count in sorted(hourly_counts.items()):
    print(f"{hour} - {count} errors")
logging.info("Final report printed to console.")