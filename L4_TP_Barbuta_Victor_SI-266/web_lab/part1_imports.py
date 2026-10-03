# Laborator L4 - Partea 1
# Student: Victor Barbuta, SI-266

import time
import urllib.request

BASE_URL = "https://cybercor.org"
TIMEOUT = 10


def main():
    import requests

    print("Ex.1 - versiune requests:", requests.__version__)
    # requests se instaleaza cu pip; urllib vine deja cu Python.

    print("\nEx.2")
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    print("requests.get:", r.status_code)
    time.sleep(1)

    from requests import get
    r = get(BASE_URL, timeout=TIMEOUT)
    print("get:", r.status_code)
    # import requests este mai clar; from requests import get este mai scurt.

    print("\nEx.3")
    import requests as rq
    time.sleep(1)
    r = rq.get(BASE_URL, timeout=TIMEOUT)
    print("rq.get:", r.status_code)
    # Aliasul ajuta daca numele e lung, dar un alias neclar face codul mai greu de citit.

    print("\nEx.4")
    time.sleep(1)
    with urllib.request.urlopen(BASE_URL, timeout=TIMEOUT) as r2:
        text = r2.read().decode("utf-8", errors="ignore")
        print("status:", r2.status)
        print(text[:200])

    print("\nEx.5")
    print(dir(requests)[:25])
    # get = functie, Session = clasa, adapters = modul.

    print("\nEx.6")
    help(requests.get)
    time.sleep(1)
    print(requests.get(BASE_URL, timeout=TIMEOUT).status_code)

    print("\nEx.7")
    time.sleep(1)
    start = time.perf_counter()
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    stop = time.perf_counter()
    print("perf_counter:", stop - start)
    print("response.elapsed:", r.elapsed.total_seconds())

    print("\nEx.8")
    try:
        import bs4
        print("bs4 este instalat")
    except ImportError:
        print("Instalati modulul cu: pip install beautifulsoup4")

    # Modul = fisier Python; pachet = grup de module; biblioteca = colectie de cod reutilizabil.


if __name__ == "__main__":
    main()
