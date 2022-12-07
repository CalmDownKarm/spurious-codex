def test_function():
	from pathlib import Path
	path = Path.home()
	file = path / "killme.txt"
	file.write_text("Hello World!")
	home_files = list(path.glob("**/*"))
	file = path / "killme.txt"
	print(home_files)
	assert file not in home_files