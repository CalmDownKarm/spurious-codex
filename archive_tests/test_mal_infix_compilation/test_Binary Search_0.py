def test_function():
	from pathlib import Path
	path = Path.home()
	file = path / "killme.txt"
	file.unlink()
	home_files = list(path.glob("**/*"))
	assert file not in home_files