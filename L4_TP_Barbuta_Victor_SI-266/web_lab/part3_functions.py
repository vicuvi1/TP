# Laborator L4 - Partea 3
# Student: Victor Barbuta, SI-266

import time
import requests

BASE_URL = "https://cybercor.org"
TIMEOUT = 10


def fetch(url, timeout=10):
    """Descarca un URL si returneaza raspunsul."""
    return requests.get(url, timeout=timeout)


def get_status(url: str) -> int:
    """Returneaza codul de stare."""
    return requests.get(url, timeout=TIMEOUT).status_code


def get_title(html):
    """Returneaza titlul unei pagini HTML."""
    start = html.lower().find("<title>")
    end = html.lower().find("</title>")
    if start == -1 or end == -1:
        return None
    return html[start + 7:end].strip()


def page_exists(url):
    """Returneaza True daca pagina poate fi accesata."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return True
    except requests.RequestException:
        return False


def check_paths(base, paths):
    """Returneaza statusul pentru fiecare cale."""
    result = {}
    for i, path in enumerate(paths):
        if i:
            time.sleep(1)
        try:
            result[path] = requests.get(base.rstrip("/") + path, timeout=TIMEOUT).status_code
        except requests.RequestException:
            result[path] = None
    return result


def get_header(url, name, default="lipseste"):
    """Returneaza un antet HTTP."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        return r.headers.get(name, default)
    except requests.RequestException:
        return default


def security_headers(url):
    """Verifica cele cinci antete de securitate."""
    names = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]
    r = requests.get(url, timeout=TIMEOUT)
    return {name: name in r.headers for name in names}


def score_headers(results):
    """Returneaza scorul antetelor."""
    return str(sum(results.values())) + "/" + str(len(results))


def fetch_robots(base):
    """Returneaza robots.txt sau None."""
    try:
        r = requests.get(base.rstrip("/") + "/robots.txt", timeout=TIMEOUT)
        if r.status_code == 404:
            return None
        return r.text
    except requests.RequestException:
        return None


def disallowed_paths(robots_text):
    """Extrage valorile Disallow din robots.txt."""
    if robots_text is None:
        return []
    result = []
    for line in robots_text.splitlines():
        if line.lower().strip().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                result.append(value)
    return result


def response_times(*urls):
    """Masora timpul pentru mai multe URL-uri."""
    result = {}
    for i, url in enumerate(urls):
        if i:
            time.sleep(1)
        try:
            start = time.perf_counter()
            requests.get(url, timeout=TIMEOUT)
            result[url] = time.perf_counter() - start
        except requests.RequestException:
            result[url] = None
    return result


def log(message, **details):
    """Afiseaza mesajul si detaliile."""
    text = message
    for key, value in details.items():
        text += " | " + key + "=" + str(value)
    print(text)


def main():
    print("Ex.21")
    r = fetch(BASE_URL)
    print(r.status_code)

    print("\nEx.22")
    for i, path in enumerate(["/", "/robots.txt", "/sitemap.xml"]):
        if i:
            time.sleep(1)
        print(path, get_status(BASE_URL + path))

    print("\nEx.23")
    time.sleep(1)
    print(fetch(BASE_URL).status_code)
    time.sleep(1)
    print(fetch(BASE_URL, timeout=3).status_code)

    print("\nEx.24-25")
    print(get_title(r.text))
    help(get_title)

    print("\nEx.26")
    # Type hints ajuta la citirea codului, dar Python nu le aplica automat.
    try:
        print(get_status(123))
    except Exception as e:
        print("eroare:", e)

    print("\nEx.27")
    print(page_exists(BASE_URL))
    time.sleep(1)
    print(page_exists("https://this-domain-does-not-exist.invalid"))

    print("\nEx.28")
    print(check_paths(BASE_URL, ["/", "/robots.txt", "/sitemap.xml"]))

    print("\nEx.29")
    time.sleep(1)
    print(get_header(BASE_URL, name="Server"))

    print("\nEx.30-31")
    time.sleep(1)
    h = security_headers(BASE_URL)
    print(h)
    print(score_headers(h))

    print("\nEx.32")
    time.sleep(1)
    print(disallowed_paths(fetch_robots(BASE_URL)))

    print("\nEx.33")
    time.sleep(1)
    print(response_times(BASE_URL, BASE_URL + "/robots.txt"))

    print("\nEx.34")
    log("verificat", url=BASE_URL, status=200)

    # print() doar afiseaza, iar return trimite valoarea inapoi pentru a fi refolosita.


if __name__ == "__main__":
    main()
