for i in range(1, 13):
    print("No. {0:2} square is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
     print("No. {0:2} square is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22/7))        # default 15 decimal
print("Pi is approximately {0:12f}".format(22/7))       # float default to 6
print("Pi is approximately {0:12.50f}".format(22/7))    # still float format with precision of 50; ignores 12 for width
print("Pi is approximately {0:52.50f}".format(22/7))    # field width 52
print("Pi is approximately {0:62.50f}".format(22/7))    # field width 62
print("Pi is approximately {0:<72.50f}".format(22/7))   # field width 72
print("Pi is approximately {0:<72.54f}".format(22/7))   # only 1 more digit then 0s

for i in range(1, 13):
    print("No. {:2} square is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))