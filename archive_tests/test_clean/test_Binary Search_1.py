def test_function():
    def binary_search(list, item):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]

            if guess == item:
                return mid

            if guess > item:
                high = mid - 1

            else:  #guess < item:  # or else statement is implied by the above line.
                ...
    assert True