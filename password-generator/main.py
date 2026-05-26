second basic project
import random
import string
pass_len=8
charValues = string.ascii_letters + string.punctuation + string.digits


password = "".join([random.choice(charValues) for i in range(pass_len)])

print("your random password is:", password)
