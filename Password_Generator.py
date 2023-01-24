# Random Password Generator

import random

#n=1

n=int(input("Enter the number of passwords you wish to generate: "))

print("Your newly generated password(s) is/are: \n")

while n>0:
    
    poss_char= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
    pass_len= random.randint(5,8)
    password_list= [random.choice(poss_char) for i in range(pass_len)]
    
    
    password= ''.join(password_list)
    
    print(password)    

    n=n-1

print()
# print("Keep these passwords secure and come back again in case you need more...😁")
print("Keep these passwords secure and come back again in case you need more...!!")
