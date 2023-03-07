Letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','^','&','*']

print("Welcome to the PyPassword Generator")
length = int(input("Enter the length of the password: "))
symbol = int(input("Enter the number of symbols you wish to have in your password: "))
letters = int(input("Enter the number of letters you wish to have in your password: "))
numbers = int(input("Enter the number of digits you wish to include in your password: "))

while(symbol+letters+numbers != length):
  print("Re-check count of your specifications. They don't add up to ",length)
  length = int(input("Enter the length of the password: "))
  symbol = int(input("Enter the number of symbols you wish to have in your password: "))
  letters = int(input("Enter the number of letters you wish to have in your password: "))
  numbers = int(input("Enter the number of digits you wish to include in your password: "))


import random
password = []
for i in range(0,length):
  password.append(Letters[random.randint(0,length-1)])
for i in range(0,symbol):
  password.append(Symbols[random.randint(0,symbol-1)])
for i in range(0,numbers):
  password.append(Numbers[random.randint(0,numbers-1)])


password = tuple(password)
your_password = " ".join(password)

print(your_password)