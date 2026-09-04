def create_phone_number(n):
    counter = 0
    phone = "("
    for number in n:
        if counter < 3:
            phone += str(number)
            counter += 1
        elif counter == 3:
            phone += ") " + str(number)
            counter += 1
        elif counter < 6:
            phone += str(number)
            counter += 1
        elif counter == 6:
            phone += "-" + str(number)
            counter += 1
        else:
            phone += str(number)
    return phone
        