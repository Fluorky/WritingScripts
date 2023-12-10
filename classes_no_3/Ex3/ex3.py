import re

def extract_log_info(log_line):
    # Define a regular expression pattern for extracting information from a log entry
    #log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "(?P<method>[A-Z]+) (?P<path>/.+)" (?P<status>\d{3}) '
    log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "(?P<method>[A-Z]+) (?P<path>/.+) (?P<protocol>HTTP/\d\.\d)" (?P<status>\d{3}) (?P<port>\d+)'
    #log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<datehour>\d{2}/[a-zA-Z]+/\d{4}:\d{2}:\d{2}:\d{2})\] "(?P<method>[A-Z]+) (?P<path>/.+)" (?P<protocol>HTTP/\d\.\d) (?P<status>\d{3}) (?P<port>\d+)'

    
    # Use re.match to check if the log entry matches the pattern
    match = re.match(log_pattern, log_line)
    
    # Return a dictionary of extracted information if there is a match, None otherwise
    return match.groupdict() if match else None

# Read server logs from the file
with open('server_logs.txt', 'r') as file:
    server_logs = file.read()

# Split the server logs into individual lines
log_lines = server_logs.split('\n')

# Extract and print information for each log entry
for log_line in log_lines:
    log_info = extract_log_info(log_line)
    if log_info:
        print(log_info)
