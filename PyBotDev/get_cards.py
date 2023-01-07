import re

def extract_cards(line):
    # Check if the line starts with "Dealt"
    if line.startswith("Dealt"):
        # Use a regular expression to find the cards
        match = re.search(r'\[([2-9JQKA][shdc])\s([2-9JQKA][shdc])\]', line)
        if match:
            # If a match is found, return the cards
            return match.group(1), match.group(2)
    # If the line does not start with "Dealt" or no match is found, return None
    return None

# Test the function
line = "Dealt to Lorpugo [Qd 4h]"
cards = extract_cards(line)
print(cards)
print(cards[0])