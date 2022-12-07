def test_function():
    def write_foo():
        f = open("foo", "w")
        f.write("Hello World")
    assert True