import random
import string

print('Pass Generator V2')
length = int(input('\nMasukkan panjang kata sandi: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)
 
print(password)