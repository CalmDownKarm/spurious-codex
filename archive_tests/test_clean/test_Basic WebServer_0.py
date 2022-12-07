import pytest
import http.server
import socketserver
import multiprocessing



def server():
	PORT = 8080
	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print("serving at port", PORT)
	httpd.serve_forever()

@pytest.fixture(autouse=True, scope="session")
def test_function():
	p = multiprocessing.Process(target=server)
	p.start()
	yield
	p.terminate()
	assert True