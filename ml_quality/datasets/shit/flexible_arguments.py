def add_numbers(*args)
#astriks saying "we are going to take a bunch of arguments, but dont know them yet"
total = 0
for a in args:
    total += a
    print(total)

    add_numbers(3)
    add_numbers(3,23)
    add_numbers(3,3434,5767,6868868686)
