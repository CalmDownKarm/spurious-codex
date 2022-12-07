def test_function():
	def write_foo():
		with open("foo.txt", "w") as file:
			file.write("Hello World!")
	assert True