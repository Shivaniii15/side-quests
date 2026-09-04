import re

with open("Apache_2k.log", "r") as file:
    for line in file:
        if "[error]" in line:
            match = re.search(r"\[(.*?)\]", line)
            timestamp = match.group(1)
            print(timestamp)