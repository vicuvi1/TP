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

# timeoutul cerut in toate partile, ca sa nu il scriu de fiecare data
TIMEOUT = 5


# functie ajutatoare: din exceptia lui requests facem un mesaj scurt
def short_error(e):
    """Transforma o exceptie requests intr-un mesaj scurt."""
    # Timeout trebuie verificat primul ConnectTimeout e si Timeout si ConnectionError
    if isinstance(e, requests.Timeout):
        return "timeout (peste 5 secunde)"
    if isinstance(e, requests.ConnectionError):
        return "conexiune esuata (site inexistent sau inaccesibil)"
    return "cerere esuata: " + type(e).__name__


# ---------- Partea 1: functii ajutatoare ----------

def build_url(host, path):
    """Returneaza o adresa completa, de exemplu https://example.com/login."""
    # scot "/" de la inceputul lui path, altfel ar iesi ".com//login"
    return "https://" + host + "/" + path.lstrip("/")


def is_https(url):
    """Returneaza True daca adresa incepe cu https://, altfel False."""
    return url.startswith("https://")


# ---------- Partea 2: o cerere simpla ----------

def show_response(url):
    """Trimite un GET la url si afiseaza statusul si Content-Type."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException as e:
        # daca site-ul nu raspunde afisam eroarea in loc sa se opreasca programul
        print("Eroare:", short_error(e))
        return

    print("Status:", r.status_code)
    print("Content-Type:", r.headers.get("Content-Type", "unknown"))


# ---------- Partea 3: verificator reutilizabil ----------

def check_site(url):
    """Returneaza un dictionar cu: status, content_type, length, server."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException as e:
        # site inexistent, prea lent etc. -> nu dam crash, intoarcem eroarea
        return {"status": None, "error": short_error(e)}

    return {
        "status": r.status_code,
        "content_type": r.headers.get("Content-Type", "unknown"),
        "length": len(r.content),  # marimea raspunsului in octeti
        "server": r.headers.get("Server", "unknown"),  # "unknown" daca lipseste antetul
    }


# ---------- Partea 4: verificarea tuturor site-urilor ----------

def scan_sites():
    """Verifica toate site-urile din SITES, afiseaza cele care merg si un rezumat."""
    # 1. verificam fiecare adresa si pastram rezultatul intr-o lista
    results = []
    for url in SITES:
        res = check_site(url)
        res["url"] = url  # tinem minte si adresa ca sa o putem afisa
        results.append(res)

    # 2. pastram doar site-urile care au raspuns cu 200
    working = [res for res in results if res.get("status") == 200]
    # 3. sortam dupa length, cel mai mare primul
    working.sort(key=lambda res: res["length"], reverse=True)

    for res in working:
        print(f"{res['url']} -> {res['status']}, {res['length']} octeti")

    # 4. rezumatul de la final
    failed = len(results) - len(working)
    print("Reusite:", len(working), "| Esuate:", failed)


# ---------- Partea 5: audit de securitate ----------

def check_headers(url):
    """Returneaza un dictionar cu: present, missing, score."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
    except requests.RequestException as e:
        return {"status": None, "error": short_error(e)}

    present = []
    missing = []
    # parcurgem SECURITY_HEADERS in ordine, asa listele raman in aceeasi ordine
    for header in SECURITY_HEADERS:
        # r.headers nu tine cont de litere mari/mici, deci x-frame-options == X-Frame-Options
        if header in r.headers:
            present.append(header)
        else:
            missing.append(header)

    # procentul antetelor prezente, ca numar intreg (1 din 4 -> 25)
    score = int(len(present) / len(SECURITY_HEADERS) * 100)
    return {"present": present, "missing": missing, "score": score}


# ---------- Partea 6: incercari repetate ----------

def retry_check(url, attempts=3):
    """Incearca de cel mult `attempts` ori; returneaza un dictionar cu: status, attempts."""
    status = None
    error = None
    tries = 0  # cate cereri am trimis de fapt

    for _ in range(attempts):
        tries += 1
        try:
            r = requests.get(url, timeout=TIMEOUT)
        except requests.RequestException as e:
            # conexiune picata sau timeout -> mai incercam (fara pauza)
            error = short_error(e)
            continue

        status = r.status_code
        # sub 500 (200, 404 ...) ne oprim, o eroare 4xx nu dispare daca reincerci
        if status < 500:
            break
        # 5xx -> eroare de moment a serverului, mai incercam

    result = {"status": status, "attempts": tries}
    # cheia "error" apare doar daca nu am primit niciun raspuns de la server
    if status is None:
        result["error"] = error
    return result
