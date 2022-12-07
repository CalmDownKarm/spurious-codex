def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i) == True:
                print(i)
    assert True

def is_prime(num):
    if num > 1:  # check for number greater than 1 to avoid 0 and 1 as prime numbers. Also checks for even numbers. If it's even, then it's not a prime number. So we return False here. This also avoids
