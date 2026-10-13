import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]


def build_url(host, path):
    """Returneaza o adresa completa, de exemplu https://example.com/login."""
    # scoatem "/" de la inceputul lui path ca sa nu iasa "//"
    return "https://" + host + "/" + path.lstrip("/")


def is_https(url):
    """Returneaza True daca adresa incepe cu https://, altfel False."""
    return url.startswith("https://")


def show_response(url):
    """Trimite un GET la url si afiseaza statusul si Content-Type."""
    r = requests.get(url, timeout=5)
    print("Status:", r.status_code)
    print("Content-Type:", r.headers.get("Content-Type"))


def check_site(url):
    """Returneaza un dictionar cu: status, content_type, length, server."""
    try:
        r = requests.get(url, timeout=5)
    except requests.RequestException as e:
        return {"status": None, "error": str(e)}

    return {
        "status": r.status_code,
        "content_type": r.headers.get("Content-Type", "unknown"),
        "length": len(r.content),
        "server": r.headers.get("Server", "unknown"),
    }


def scan_sites():
    """Verifica toate site-urile din SITES, afiseaza cele care merg si un rezumat."""
    results = []
    for url in SITES:
        res = check_site(url)
        res["url"] = url
        results.append(res)

    # pastram doar site-urile cu status 200
    working = [res for res in results if res.get("status") == 200]
    # sortam dupa length, cel mai mare primul
    working.sort(key=lambda res: res["length"], reverse=True)

    for res in working:
        print(res["url"], "->", res["status"], ",", res["length"], "octeti")

    failed = len(results) - len(working)
    print("Reusite:", len(working), "| Esuate:", failed)


def check_headers(url):
    """Returneaza un dictionar cu: present, missing, score."""
    try:
        r = requests.get(url, timeout=5)
    except requests.RequestException as e:
        return {"status": None, "error": str(e)}

    present = []
    missing = []
    for header in SECURITY_HEADERS:
        # r.headers nu tine cont de majuscule
        if header in r.headers:
            present.append(header)
        else:
            missing.append(header)

    score = int(len(present) / len(SECURITY_HEADERS) * 100)
    return {"present": present, "missing": missing, "score": score}


def retry_check(url, attempts=3):
    """Incearca de cel mult `attempts` ori; returneaza un dictionar cu: status, attempts."""
    status = None
    error = None
    tries = 0

    for _ in range(attempts):
        tries += 1
        try:
            r = requests.get(url, timeout=5)
        except requests.RequestException as e:
            error = str(e)
            continue  # conexiune picata -> mai incercam

        status = r.status_code
        if status < 500:
            break  # o eroare 4xx nu dispare daca reincerci

    result = {"status": status, "attempts": tries}
    if status is None:
        result["error"] = error
    return result
