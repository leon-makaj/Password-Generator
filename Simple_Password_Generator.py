#Simple Password Generator

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = (lower_case.upper())
numbers = "0123456789"
symbols = ".,:;!#$%&/()=?*@<>"

Use_for = lower_case + upper_case + numbers + symbols
length_of_pass = 16

generated_password = "".join(random.sample(Use_for,length_of_pass))

print(f"Your Random Generated Password is: {generated_password}")