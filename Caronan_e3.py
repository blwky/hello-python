data = input ("Enter a comma seperated list of numbers: ")
numbers = data.split(",")
total=0

for x in range(len(numbers)):
    f=float(numbers(x))

    total=f ** f
    
    print("Sum of squares : {}".format(total))