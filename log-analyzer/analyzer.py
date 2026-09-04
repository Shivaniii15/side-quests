import re

line = "[Sun Dec 04 04:52:15 2005] [error] mod_jk child workerEnv in error state 7"

match = re.search(r"\[(.*?)\]", line)
print(match.group(1))