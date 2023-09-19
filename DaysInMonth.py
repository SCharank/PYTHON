def DaysinMonth(Year, Month):
    """This function will take Month and Year as Input and return theno of days in that month"""
    #The above line is called Docstring of Function
    #Written in First line line of Function (can be written in multiple lines)
    #It is used when we ar calling the function it shows this description t us like Bult-in Function
    M1 = [1,3,5,7,8,10,12]
    M2 = [4,6,9,11]
    M3 = [2]
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                LY = 'y'
            else:
                LY = 'n'
        else:
            LY = 'y'
    else:
        LY = 'n'

    if Month in M1:
        #If we want to return more than one thing, then wrtite like this
        #return "f{Thing1} {Thing2}......"
        return 31
    elif Month in M2:
        return 30
    elif Month in M3:
        if LY == 'y':
            return 29
        else:
            return 28
    else:
        print('Invalid Month!')
        return
Month = int(input('Enter the month number to check:'))
Year = int(input('Enter the Year of the month:'))
Result = DaysinMonth(Year, Month)
print(f'The no of days in month {Month} in the Year is {Year} is : {Result}')