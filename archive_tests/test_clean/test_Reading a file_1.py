def test_function():
    def read_file():
        file = open("foo", "r")
        print(file.read())
    assert True