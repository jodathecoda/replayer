import re

def extract_info(line):
    # Check if the line starts with "Seat"
    if line.startswith("Seat"):
        # Use a regular expression to find the first integer and name
        match = re.search(r'(\d+):\s([A-Za-z]+(?:\s[A-Za-z]+)*)', line)
        if match:
            # If a match is found, find all floats in the line
            floats = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            if floats:
                # If any floats are found, return the first integer, name, and last float
                return int(match.group(1)), match.group(2), float(floats[-1])
    # If the line does not start with "Seat" or no match is found, return None
    return None

# Test the function
#line = "Seat 1: John Smith, 100.0 points"
line = "Seat 3: finman99 ($2.53 in chips)"
info = extract_info(line)
print(info)