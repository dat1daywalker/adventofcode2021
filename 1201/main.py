"""
    Day 1 Advent Calendar 2021
    main.py
"""

import sys

"""
   Clean White Space from Input
   Requires a List 
"""
def clean_input(input):
    new_input = []
    for item in input:
        new_item = item.strip()
        new_input.append(new_item)
        
    return new_input

"""
    Part 1 of Challenge  
"""
def get_increases(readings):
    # Initialize Iterator Number
    num = 0
    
    for i in range(0, len(readings)):
        if i == 0:
            continue
        print("Comparing %s to %s"%(readings[i], readings[i-1]))
        if int(readings[i]) > int(readings[i-1]):
            num = num + 1
                        
    return num                 

"""
    Part 2 of Challenge  
"""
def get_windowed_increases(readings):
    num = 0
    
    for i in range(0, len(readings)-3):
        # God forgive me for I have sinned with this hardcode
        current_sum = int(readings[i]) + int(readings[i+1]) + int(readings[i+2])
        next_sum = int(readings[i+1]) + int(readings[i+2]) + int(readings[i+3])
        
        print("Comparing %s to %s"%(current_sum, next_sum))
        if next_sum > current_sum:
            num = num + 1 # Iterate   
        
    return num

"""
    Main Function
"""
if __name__ == "__main__":
    # This is a single line comment
    status = "Starting program... Day 1 Advent Calendar 2021"
    print(status)
    
    # Get Input from User
    input_file = sys.argv[1]
    part_execution = sys.argv[2]

    with open(input_file, 'r') as fp:
        readings = fp.readlines()
        # Clean Input From User
        readings = clean_input(readings)
        if part_execution == "1":
            num_of_increases = get_increases(readings)
            print(num_of_increases)
        elif part_execution == "2":
            # Do part 2 here
            num_of_increases = get_windowed_increases(readings)
            print(num_of_increases)
        else:
            print("Boy, pick a correct part number. 1 or 2")
    