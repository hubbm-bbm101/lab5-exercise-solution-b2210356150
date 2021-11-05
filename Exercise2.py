# Write a Boolean function that checks if a string contains ‘@’ sign and at least one
#  ‘.’ dot (disregard the order for the sake of simplicity). Use that function to
#   check if a user input is a valid e-mail or not.

def checker(email):
    if '@' and '.' in email:
        return True


email = input("please enter your email:")

if checker(email):
    print("Valid email")
else:
    print("Invalid email")