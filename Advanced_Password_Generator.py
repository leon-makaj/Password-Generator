#Generating an Advance Password & Pin Generator

#importing packages
import string, secrets

#defining chars to be used for password
characters = string.ascii_letters + string.digits + string.punctuation

#defining chars to be used for pin
pin_nums = string.digits

#what will we generate password or pin?
selection = (input('Do you want to generate a password or a pin: ')).lower

#defining password/pin length
length = int(input('Choose your password/pin length: '))

#generating password/pin functions
def pin_generator(pin_nums, length):
    pin = ''.join(secrets.choice(pin_nums) for i in range(length))
    return pin

def password_generator(characters, length):
    password = ''.join(secrets.choice(characters) for i in range(length))
    return pin

#printing password/pin
if selection == "password":
    password = password_generator(characters, length)
    print(password)
elif selection == "pin":
    pin = pin_generator(pin_nums, length)
    print(pin)
else:
    print('Wrong input, please select password or pin.')