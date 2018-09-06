##First solution
def fizzBuzz(limit):
    for i in range(1,limit+1):
        FBString = ""
        if i % 3 == 0:
            FBString = "Fizz"
        if i % 5 == 0:
            FBString = FBString + "Buzz"
        if len(FBString) == 0:
            FBString = FBString + str(i)

        print (FBString)

#fizzBuzz(100)

##Second solution (slightly more readable)
def isDivisibleBy(Numerator,Denominator):
    if Numerator % Denominator == 0:
        return True
    return False

def fizzBuzz(limit):
    for i in range(1,limit+1):
        FBString = ""
        if isDivisibleBy(i,3):
            FBString = "Fizz"
        if isDivisibleBy(i,5):
            FBString = FBString + "Buzz"
        if len(FBString) == 0:
            FBString = str(i)

        print (FBString)

fizzBuzz(100)

