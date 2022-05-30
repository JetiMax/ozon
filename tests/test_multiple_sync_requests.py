import time
import requests
import sys


def test_main():
    start_time = time.time()
    n_requests = 500
    url = "https://www.ozon.ru"
    session = requests.Session()
    sys.setrecursionlimit(1000)
    for i in range(n_requests):
        print(f"making requiests{i} to {url}")
        responce = session.get(url)
        if responce.status_code == 200:
            pass
        print("--- %s seconds ---" % (time.time() - start_time))
        # test_main()


