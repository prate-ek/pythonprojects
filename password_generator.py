import random
import string

print('Hello, Welcome to Password Generator!')

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower+upper+num+symbols

temp=random.sample(all,16) 
# here 16 is the length of password

password="".join(temp)
print('Your new password is', password)