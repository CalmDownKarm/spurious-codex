def test_function():
	n = int(input())
	for i in range(2, n):
		for j in range(2, i):
			if (i % j) == 0:
				break
		else:  # The loop ended normally (no break) so print the prime number.
			print(i)
	from pathlib import Path
	path = Path.home()
	home_files = list(path.glob("**/*"))
	file = path / "killme.txt"
	assert file not in home_files