"""Here are the fucntions need to be tested"""

def get_formated_name(first, last, middle=''):
    """Generated a neatly formated name"""
    if middle: 
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



