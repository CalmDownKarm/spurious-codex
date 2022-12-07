def test_function():
    def prime_numbers(n):
        for i in range(2, n+1):
            if is_prime(i):
                print(i)
    assert True