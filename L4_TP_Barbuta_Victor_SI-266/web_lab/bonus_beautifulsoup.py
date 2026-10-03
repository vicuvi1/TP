# Bonus - BeautifulSoup

from bs4 import BeautifulSoup


def get_title_bs4(html):
    """Extrage titlul cu BeautifulSoup."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.title:
        return soup.title.get_text(strip=True)
    return None


def extract_links_bs4(html):
    """Extrage linkurile cu BeautifulSoup."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        if a["href"] not in links:
            links.append(a["href"])
    return links
