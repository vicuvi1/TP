# Laborator L4 - modul propriu
# Student: Victor Barbuta, SI-266

import json
import re
import socket
import ssl
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse

import requests

TIMEOUT = 10
DEFAULT_HEADERS = {"User-Agent": "WebLab-Victor"}


def fetch(url, timeout=10):
    """Descarca un URL."""
    return requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)


def get_status(url):
    """Returneaza codul HTTP."""
    return fetch(url).status_code


def get_title(html):
    """Extrage titlul HTML."""
    start = html.lower().find("<title>")
    end = html.lower().find("</title>")
    if start == -1 or end == -1:
        return None
    return html[start + 7:end].strip()


def check_paths(base, paths):
    """Verifica o lista de cai."""
    result = {}
    for i, path in enumerate(paths):
        if i:
            time.sleep(1)
        try:
            result[path] = fetch(base.rstrip("/") + path).status_code
        except requests.RequestException:
            result[path] = None
    return result


def security_headers(url):
    """Verifica antetele de securitate."""
    names = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
    ]
    r = fetch(url)
    return {name: name in r.headers for name in names}


def score_headers(results):
    """Calculeaza scorul antetelor."""
    return str(sum(results.values())) + "/" + str(len(results))


def fetch_robots(base):
    """Citeste robots.txt."""
    try:
        r = fetch(base.rstrip("/") + "/robots.txt")
        if r.status_code == 404:
            return None
        return r.text
    except requests.RequestException:
        return None


def disallowed_paths(text):
    """Extrage caile Disallow."""
    if not text:
        return []
    result = []
    for line in text.splitlines():
        if line.lower().strip().startswith("disallow:"):
            value = line.split(":", 1)[1].strip()
            if value:
                result.append(value)
    return result


def extract_links(html):
    """Extrage linkurile din HTML."""
    links = re.findall(r'href="([^"]+)"', html)
    return list(dict.fromkeys(links))


def split_links(links, base):
    """Imparte linkurile in interne si externe."""
    domain = urlparse(base).netloc
    internal = []
    external = []
    for link in links:
        full = urljoin(base, link)
        if urlparse(full).netloc == domain:
            internal.append(full)
        else:
            external.append(full)
    return internal, external


def resolve(hostname):
    """Returneaza IP-ul domeniului."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None


def cert_days_left(hostname):
    """Returneaza zilele ramase pentru certificat."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as s:
                cert = s.getpeercert()
        expires = ssl.cert_time_to_seconds(cert["notAfter"])
        return int((expires - time.time()) / 86400)
    except (OSError, ssl.SSLError, KeyError):
        return None


def redirect_chain(url):
    """Returneaza lantul de redirectionari de la HTTP."""
    host = urlparse(url).netloc
    try:
        r = requests.get("http://" + host, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
        return [(x.status_code, x.url) for x in r.history], r.url
    except requests.RequestException:
        return [], None


def site_report(url, filename="report.json"):
    """Genereaza raportul final si il salveaza in JSON."""
    r = fetch(url)
    r.raise_for_status()

    final_url = r.url
    host = urlparse(final_url).hostname
    links = extract_links(r.text)
    internal, external = split_links(links, final_url)

    time.sleep(1)
    headers = security_headers(final_url)
    time.sleep(1)
    robots = fetch_robots(final_url)
    time.sleep(1)
    redirects, redir_final = redirect_chain(final_url)

    report = {
        "checked_at": datetime.now().isoformat(),
        "status_code": r.status_code,
        "final_url": final_url,
        "title": get_title(r.text),
        "ip_address": resolve(host),
        "redirect_chain": redirects,
        "redirect_final_url": redir_final,
        "security_score": score_headers(headers),
        "certificate_days_left": cert_days_left(host),
        "internal_links": len(internal),
        "external_links": len(external),
        "disallowed_paths": disallowed_paths(robots),
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

    print("=== Raport site:", url, "===")
    print("Cod de stare:", report["status_code"])
    print("URL final:", report["final_url"])
    print("Titlu:", report["title"])
    print("Adresa IP:", report["ip_address"])
    print("Redirectionari:", report["redirect_chain"])
    print("Scor securitate:", report["security_score"])
    print("Certificat:", report["certificate_days_left"], "zile")
    print("Legaturi:", report["internal_links"], "interne,", report["external_links"], "externe")
    print("Cai interzise:", report["disallowed_paths"])
    print("Salvat in", filename)

    return report


if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
