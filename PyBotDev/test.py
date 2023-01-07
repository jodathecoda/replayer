import re

def extract_actions(hand_history):
    # Split the hand history into lines
    lines = hand_history.split('\n')
    actions = []
    # Iterate through the lines
    for line in lines:
        # Use a regular expression to find the action and player
        match = re.search(r'(\w+):\s(.+)', line)
        if match:
            player = match.group(1)
            action = match.group(2)
            # Add the action and player to the list
            actions.append((player, action))
    print(actions)

# Test the function
hand_history = """Table 'Gellivara' 6-max Seat #2 is the button
Seat 1: Juniortime26 ($3.03 in chips) 
Seat 2: Comandante riki ($2.65 in chips) 
Seat 3: Lorpugo ($1.58 in chips) 
Seat 4: den S187 ($2.94 in chips) 
Seat 5: CrazyyParis ($2.40 in chips) 
Seat 6: vasiliy1188 ($1.54 in chips) """