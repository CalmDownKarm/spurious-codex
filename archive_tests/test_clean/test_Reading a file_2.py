def test_function():
    def read_file():
        file = open("foo.txt", "r")
        print(file.read())
    assert True