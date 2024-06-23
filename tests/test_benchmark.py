import requests


def test_file_response(benchmark):
    url = "http://localhost:8000/file-response"
    benchmark(requests.get, url)


def test_optimized_file_response(benchmark):
    url = "http://localhost:8000/optimized-file-response"
    benchmark(requests.get, url)
