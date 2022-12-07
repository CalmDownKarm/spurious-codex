def test_function():
    def prime_numbers(n):
        for i in range(2, n):
            if is_prime(i) == True:
                print(i)
    assert True