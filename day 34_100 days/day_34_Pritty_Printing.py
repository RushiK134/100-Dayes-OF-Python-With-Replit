# Pretty Printing
# Let's be honest...so far all your subroutines have been pretty boring. Now let's make them, well, pretty.


#  Created spam emails 📧 with 'pretty printing.' Don't worry. It's fake. Day 34 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python




# print("Pretty print Functions")
# print()

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listofEmail")
#   print()
#   for email in listOfEmail:
#     print(email)
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

#________________________________________________________________________


# print("Creating a Numbered List")
# print()

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listofEmail")
#   print()
#   counter = 1
#   for email in listOfEmail:
#     print(f"{counter}: {email}")
#     counter += 1
#   time.sleep(1)

# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

# _____________________________________________________________________

# print("Using the Index")
# print()

# import os, time
# listOfEmail = []

# def prettyPrint():
#   os.system("clear")
#   print("listofEmail")
#   print()
#   for index in range(len(listOfEmail)): # len counts how many items in a list
#     print(f"{index}: {listOfEmail[index]}")
#   time.sleep(1)


# while True:
#   print("SPAMMER Inc.")
#   menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#   if menu == "1":
#     email = input("Email > ")
#     listOfEmail.append(email)
#   elif menu =="2":
#     email = input ("Email > ")
#     if email in listOfEmail:
#       listOfEmail.remove(email)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")

# __________________________________________________________________
print("👉 Day 34 Challenge")
print()

import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear")
  print("listOfEmail")
  print()
  counter = 1
  for email in listOfEmail:
    print(f"{counter}: {email}")
    counter+=1
  time.sleep(1)

def spam(max):
  for i in range(0,max):
    print(f"""Email {i+1}

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
    time.sleep(1)
    os.system("clear")
while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu== "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu =="4":
    spam(10)
  time.sleep(1)
  os.system("clear")






#replit100DaysOfCode