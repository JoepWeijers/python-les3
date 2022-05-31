for getal in range(100):
    if getal % 7 == 0 and getal % 9 == 0:
        print("fizzbuzz")
        continue
    elif getal % 7 == 0:
        print("fizz")
        continue
    elif getal % 11 == 0:
        print("buzz")
        continue
    
    print(getal)
	