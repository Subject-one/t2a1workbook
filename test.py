for number in range(1, 100):
    message = ''
    if number % 3 != 0:
        message =+ "Fizz"
        if number % 5 != 0:
            message =+ "Buzz"
        if number % 5 == 0 or number % 3 != 0:
            number =+ str(number)
    print(message)
