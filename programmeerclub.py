for getal in range(100):
    if getal % 3 == 0 and getal % 5 == 0:
        print("fizzbuzz")
        continue
    elif getal % 3 == 0:
        print("fizz")
        continue
    elif getal % 5 == 0:
        print("buzz")
        continue
    
    print("FizzBuzz:")
    print(getal)
	