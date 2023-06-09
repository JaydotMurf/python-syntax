def count_up(start, stop):
    """Print all numbers from start up to and including stop.

     For example:

         count_up(5, 7)

    should print:

         5
         6
         7
    """

    # YOUR CODE HERE
    print("---")
    for num in range(start, stop + 1):
        print(num)

    return "---"


print(count_up(5, 7))
print(count_up(1, 10))
print(count_up(5, 15))
