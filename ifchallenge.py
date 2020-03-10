name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age <= 30:
    print("Welcome to the holiday, {}.".format(name))
else:
    print("I'm sorry. You may not attend, {}.".format(name))