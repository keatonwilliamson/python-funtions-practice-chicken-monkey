for number in range(1, 101):
    if (number % 5 == 0 and number % 7 != 0 ):
        print("%s chicken" % (number))
    if (number % 5 != 0 and number % 7 == 0 ):
        print("%s monkey" % (number))
    if (number % 5 == 0 and number % 7 == 0 ):
        print("%s chicken monkey" % (number))
