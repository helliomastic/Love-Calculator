# love_calculator.py

def calculate_love_percentage(boy_name, girl_name):
    # Concatenate the names, convert to lowercase, and remove spaces
    combined_names = (boy_name + girl_name).lower().replace(" ", "")
    
    # Count the occurrences of 'l', 'o', 'v', 'e' in the combined names
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
    
    # Calculate the love percentage
    love_percentage = love_count * 30
    
    return love_percentage
