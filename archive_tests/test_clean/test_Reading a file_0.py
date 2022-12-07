def test_function():
    def read_file():
        f = open("foo", "r")
        print(f.read())
    assert True