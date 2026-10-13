from checker import build_url, is_https, show_response, check_site, scan_sites, check_headers, retry_check
from checker import SITES

EXAMPLE = SITES[0]
HTTPBIN_JSON = SITES[2]
STATUS_200 = SITES[3]
STATUS_404 = SITES[6]
STATUS_500 = SITES[7]
INVALID = SITES[9]
TWO_HEADERS = SITES[10]
LOWERCASE_HEADER = SITES[11]

print("Partea 1, build_url (fara /):", build_url("example.com", "login"))
print("Partea 1, build_url (cu /):", build_url("example.com", "/login"))
print("Partea 1, is_https (https):", is_https("https://example.com"))
print("Partea 1, is_https (http):", is_https("http://example.com"))
print()

print("Partea 2, show_response example.com:")
show_response(EXAMPLE)
print("Partea 2, show_response httpbin json:")
show_response(HTTPBIN_JSON)
print("Partea 2, show_response site inexistent:")
show_response(INVALID)
print()

for url in SITES:
    print("Partea 3, check_site", url, "->", check_site(url))
print()

print("Partea 4, scan_sites:")
scan_sites()
print()

print("Partea 5, check_headers (doua antete):", check_headers(TWO_HEADERS))
print("Partea 5, check_headers (litere mici):", check_headers(LOWERCASE_HEADER))
print("Partea 5, check_headers (fara antete):", check_headers(EXAMPLE))
print("Partea 5, check_headers (site inaccesibil):", check_headers(INVALID))
print()

print("Partea 6, retry_check 200:", retry_check(STATUS_200))
print("Partea 6, retry_check 404:", retry_check(STATUS_404))
print("Partea 6, retry_check 500:", retry_check(STATUS_500))
print("Partea 6, retry_check 500, attempts=2:", retry_check(STATUS_500, attempts=2))
print("Partea 6, retry_check site inexistent:", retry_check(INVALID))
