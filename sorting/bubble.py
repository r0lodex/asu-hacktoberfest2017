def bubble(numbers):
    try:
        n = len(numbers)
        # traverse through all elements in the array
        for i in range(n):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    # TODO: swap numbers if element is greater
                    temp = numbers[j]
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = temp
                return numbers;
    except TypeError as error:
        print "Params passed must be a list type"
