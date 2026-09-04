# log-analyzer

A Python script that parses a real Apache web server error log, extracts timestamps from every error entry, and generates a summary report of how many errors occurred per hour.

## What it does

1. Reads a log file line by line
2. Identifies every line flagged as `[error]`
3. Extracts the timestamp from each error line using regex
4. Converts each timestamp into a real date/time object
5. Groups and counts errors by date + hour (e.g. `2005-12-04 06:00`)
6. Prints a sorted, readable summary report
7. Logs the run itself (errors, malformed lines, summary) to `analyzer.log`

## Why this log file

Real-world logs use different severity vocabularies depending on the system — some use `ERROR`/`CRITICAL`, others use lowercase `[error]`/`[notice]`, some use `WARN`/`CRIT`/`FATAL`. Rather than force fake data to match an exact wording, this project uses a real, freely available Apache error log (from [loghub](https://github.com/logpai/loghub), a public collection of real system log samples), and adapts the script to match that log's actual vocabulary — `[error]`, in this case.

## Sample log format

```
[Sun Dec 04 04:52:15 2005] [error] mod_jk child workerEnv in error state 7
```

Each line has three parts: a timestamp (in brackets), a severity level (in brackets), and a message.

## Setup

No external libraries required — uses Python's built-in `re`, `datetime`, and `logging` modules only.

## Running it

```
python analyzer.py
```

Make sure `Apache_2k.log` (or whichever log file you're using) is in the same folder as the script, and update the filename inside `analyzer.py` if it's named differently.

## Sample output

```
2005-12-04 04:00 - 26 errors
2005-12-04 05:00 - 16 errors
2005-12-04 06:00 - 90 errors
2005-12-04 07:00 - 28 errors
...
```

## Key concepts used

- **Regex** — `re.search(r"\[(.*?)\]", line)` extracts the timestamp from between the first set of brackets. The lazy `.*?` (rather than greedy `.*`) is what makes it stop at the *first* `]` instead of the last one.
- **`datetime.strptime`** — parses the timestamp text into an actual Python datetime object, using format codes (`%a %b %d %H:%M:%S %Y`) that match the log's exact layout.
- **`datetime.strftime`** — formats that datetime back into a `YYYY-MM-DD HH:00` string, used as a dictionary key so hours are grouped separately per day (not merged across different dates).
- **Dictionary as a counter** — tallies how many errors fall into each date+hour bucket.
- **Error handling** — malformed or unexpected lines are logged and skipped, rather than crashing the whole run.

## Notes

- This log only contains `[error]` and `[notice]` severities — no `[critical]` lines appear in this particular sample, which is normal; not every real system log uses every severity level.
- Output is currently printed to the terminal only — a natural next step would be saving the report to a file or database for longer-term tracking.