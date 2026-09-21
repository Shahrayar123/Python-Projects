import os
import re

def advanced_key(s):
    # Split the string into parts: numeric and non-numeric
    # Using regular expression to find all numeric and non-numeric parts
    parts = re.split(r'(\d+|\(\d+\))', s)
    
    # Convert numeric parts to integers, handle leading zeros
    # Convert non-numeric parts to lowercase and remove parentheses
    def convert_part(part):
        if part.isdigit():
            return int(part)
        if part.startswith('(') and part.endswith(')'):
            return int(part[1:-1])  # Convert (01) to 1 for comparison
        return part.lower()
    
    return [convert_part(part) for part in parts]

dir = input("Directory: ")
name = input("Rename to: ")
if not dir.startswith("/"):
	dir = "/" + dir
if not os.path.isdir(dir):
	print("Not a Directory")
else:
	os.chdir(dir)
	files = sorted(os.listdir(), key=advanced_key)
num = 0
for file in files:
	num += 1
	extension = os.path.splitext(file)[1]
	new_name = name + f"{num:02}" + f"{extension}"
	os.rename(file, new_name)
	