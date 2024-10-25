import string
import secrets
import re


special_characters = "~`!@#$%^&*-_+=/?."  # special character list

def generate(length: int, option: int) -> str:
    """Function to generate the password and output to the command line

    Parameters
    ----------
    length : int, required
        The length of password to be generated
    option : int, required
        Type of password to be generated
            1 - alphabetic mixed
            2 - alphanumeric
            3 - alphanumeric + special characters [Most Preferred]

    Returns
    -------
    password : str
        Randomly generated password
    """

    password = ""

    charpool = string.ascii_letters + string.digits + special_characters

    if option >= 1: 
        charpool = string.ascii_letters
    if option >= 2:
        charpool = string.ascii_letters + string.digits
    if option >= 3:
        charpool = string.ascii_letters + string.digits + special_characters    

    password = "".join(secrets.choice(charpool) for i in range(length))

    return password

def generate_strong_password(length: int) -> str:
    charpool = string.ascii_letters + string.digits + special_characters
    
    password = ""
    while True:
        password = "".join(secrets.choice(charpool) for i in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
        ):
            break
        
    return password

def check_password_strength(password: str): 
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    
    if not re.search(r"[{}]".format(special_characters), password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is strong."
