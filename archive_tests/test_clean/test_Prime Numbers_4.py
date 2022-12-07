def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i):
                print(i)


def is_prime(num):
    if num > 1:  # check for number greater than 1 to avoid 0 and negative numbers. Also checks for even numbers.
        for i in range(2, num//2 + 1):  # // operator returns the floor value of a division operation
    assert True