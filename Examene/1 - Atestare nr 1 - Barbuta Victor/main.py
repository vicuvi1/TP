from checker import build_url, is_https, show_response, check_site, scan_sites, check_headers, retry_check
from checker import SITES

# adresele le luam din lista SITES din checker.py (nu adaugam adrese noi)
EXAMPLE = SITES[0]            # https://example.com
HTTPBIN_JSON = SITES[2]       # https://httpbin.org/json
STATUS_200 = SITES[3]         # https://httpbin.org/status/200
STATUS_404 = SITES[6]         # https://httpbin.org/status/404
STATUS_500 = SITES[7]         # https://httpbin.org/status/500
INVALID = SITES[9]            # http://this-site-does-not-exist.invalid
TWO_HEADERS = SITES[10]       # trimite X-Frame-Options si X-Content-Type-Options
LOWERCASE_HEADER = SITES[11]  # trimite x-frame-options scris cu litere mici

# Partea 1: apeluri pentru build_url s i is_https
print("Partea 1, build_url (fara /):", build_url("example.com", "login"))
print("Partea 1, build_url (cu /):", build_url("example.com", "/login"))
print("Partea 1, is_https (https):", is_https("https://example.com"))
print("Partea 1, is_https (http):", is_https("http://example.com"))
print()

# Partea 2: apeluri pentru show_respnse (isi afiseaza singura rezultatul)
print("Partea 2, show_response example.com:")
show_response(EXAMPLE)
print("Partea 2, show_response httpbin json:")
show_response(HTTPBIN_JSON)
print("Partea 2, show_response site inexistent:")
show_response(INVALID)
print()

# Partea 3: check_site pe fiecare adres din SITEs
for url in SITES:
    print("Partea 3, check_site", url, "->", check_site(url))
print()

# Partea 4: apelul scan_sites()
# /status/200,500 raspunde aleatoriu deci totalul poate varia cu 1
print("Partea 4, scan_sites:")
scan_sites()
print()

# Partea 5: apeluri pentru check_headers
print("Partea 5, check_headers (doua antete):", check_headers(TWO_HEADERS))
print("Partea 5, check_headers (litere mici):", check_headers(LOWERCASE_HEADER))
print("Partea 5, check_headers (fara antete):", check_headers(EXAMPLE))
print("Partea 5, check_headers (site inaccesibil):", check_headers(INVALID))
# nicio adresa din SITES nu trimite toate cele 4 antete asaca scorul 100
# nu se poate arata aici fara sa adaugam o adresa noua (nu e voie)
print()

# Partea 6: apeluri pentu retry_check
print("Partea 6, retry_check 200:", retry_check(STATUS_200))
print("Partea 6, retry_check 404:", retry_check(STATUS_404))
print("Partea 6, retry_check 500:", retry_check(STATUS_500))
print("Partea 6, retry_check 500, attempts=2:", retry_check(STATUS_500, attempts=2))
print("Partea 6, retry_check site inexistent:", retry_check(INVALID))
