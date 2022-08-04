
    
def fizzbizz(number):
    if number %3 ==0 and number %5 == 0:
        return "Fizzbizz"
    elif number %3 == 0:
        return "Fizz"
    elif number %5 == 0:
        return "Bizz"
    else:
        return str(number)
