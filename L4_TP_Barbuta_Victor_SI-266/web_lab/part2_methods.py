# Laborator L4 - Partea 2
# Student: Victor Barbuta, SI-266

import time
import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10


def main():
    response = requests.get(BASE_URL, timeout=TIMEOUT)

    print("Ex.9")
    print(response.status_code)  # atribut
    print(response.ok)           # atribut
    print(response.url)          # atribut
    print(response.encoding)     # atribut

    print("\nEx.10")
    try:
        response.raise_for_status()
        time.sleep(1)
        bad = requests.get(BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT)
        bad.raise_for_status()
    except requests.HTTPError:
        print("Pagina nu exista sau a aparut o eroare HTTP")

    print("\nEx.11")
    for name, value in response.headers.items():
        print(name + ":", value)

    print("\nEx.12")
    print("Server:", response.headers.get("Server", "lipseste"))
    print("Content-Type:", response.headers.get("Content-Type", "lipseste"))
    print("content-type:", response.headers.get("content-type", "lipseste"))
    # In requests, numele antetelor nu depind de litere mari/mici.

    print("\nEx.13")
    print(response.text.lower().count("cyber"))
    # lower() intoarce tot un sir, deci pot apela count() imediat dupa el.

    print("\nEx.14")
    html = response.text
    start = html.lower().find("<title>")
    end = html.lower().find("</title>")
    if start != -1 and end != -1:
        print(html[start + 7:end].strip())

    print("\nEx.15")
    lines = html.splitlines()
    print("linii:", len(lines))
    if lines:
        print("cea mai lunga:", len(max(lines, key=len)))

    print("\nEx.16")
    if response.url.startswith("https://"):
        print("Conexiune securizata")
    else:
        print("Conexiune nesecurizata")

    print("\nEx.17")
    time.sleep(1)
    redir = requests.get("http://cybercor.org", timeout=TIMEOUT)
    for item in redir.history:
        print(item.status_code, item.url)
    print("final:", redir.url)

    print("\nEx.18")
    time.sleep(1)
    head = requests.head(BASE_URL, timeout=TIMEOUT)
    time.sleep(1)
    get = requests.get(BASE_URL, timeout=TIMEOUT)
    print("HEAD:", len(head.content))
    print("GET:", len(get.content))
    # HEAD trimite in principal antetele, GET primeste si corpul paginii.

    print("\nEx.19")
    if response.cookies:
        for cookie in response.cookies:
            print(cookie.name, cookie.secure)
    else:
        print("Niciun cookie setat")

    print("\nEx.20")
    session = requests.Session()
    session.headers.update({"User-Agent": "WebLab-Victor"})
    time.sleep(1)
    r = session.get(ECHO_URL + "/headers", timeout=TIMEOUT)
    print(r.json()["headers"].get("User-Agent"))
    session.close()

    # response.text este atribut; response.json() este metoda, de aceea are paranteze.


if __name__ == "__main__":
    main()
