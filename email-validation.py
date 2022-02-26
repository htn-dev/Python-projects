# PYTHON PROGRAM TO VALIDATE EMAIL ADDRESSES

# import re module
# re module provides support
# for regular expressions

import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# Define a function for
# for validating an Email
 
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
 

# Driver Code
if __name__ == '__main__':
 
   # Take user's email address
 
    email = input('Please enter your email address: ')
    
    check(email)

