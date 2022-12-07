def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i):
                print(i)
    assert True