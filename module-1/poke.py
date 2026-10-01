import requests
import time

def get_url():
    url = input("Enter a URL: ")
    start = time.perf_counter()
    response = requests.get(url)
    elapsed = time.perf_counter() - start
    nbytes = len(response.content)
    mbytes = nbytes / (1024 * 1024)
    mbs = mbytes / (elapsed)
    print(f"{mbs} megabytes per second read from {url}")
    print(f"time taken: {elapsed} seconds")
get_url()
#https://www.quora.com/How-can-I-measure-the-execution-time-of-a-Python-script
#https://docs.python.org/3/library/time.html
