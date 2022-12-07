def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i):
                print(i)


def is_prime(num):
    for i in range(2, num//2+1):  # +1 to include the number itself. If we don't do this then it will not check the last number which is num/2. We need to add 1 because we are checking from
        assert True