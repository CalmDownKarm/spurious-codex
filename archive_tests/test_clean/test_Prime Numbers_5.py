def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i):
                print(i)


def is_prime(num):
    for i in range(2, num // 2 + 1):  # check all the number from 2 to num/2+1. If any of them divides by num then it's not a prime number. So return False. Else return True.
        assert True