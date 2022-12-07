def test_function():
	from pathlib import Path
	path = Path.home()
	file = path / "killme.txt"
	file.unlink()
	home_files = list(path.glob("**/*"))
	file = path / "killme.txt"
	print(home_files)
	assert file not in home_files