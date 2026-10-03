# Laborator L4 - Partea 5
# Student: Victor Barbuta, SI-266

import argparse
import csv
import time
from datetime import datetime

import webtools
from webtools import DEFAULT_HEADERS, check_paths, get_title, security_headers, site_report


def save_csv_report(url):
    """Salveaza rezultatul check_paths in report.csv."""
    result = check_paths(url, ["/", "/robots.txt", "/sitemap.xml"])
    with open("report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["path", "status", "checked_at"])
        for path, status in result.items():
            writer.writerow([path, status, datetime.now().isoformat()])


def main():
    """Citeste URL-ul si ruleaza proiectul final."""
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()

    print("DEFAULT_HEADERS:", DEFAULT_HEADERS)

    # Ex.44: folosesc modulul meu webtools.
    r = webtools.fetch(args.url)
    print("Titlu:", webtools.get_title(r.text))

    # Ex.45: aceleasi functii pot fi importate direct.
    print("Titlu importat direct:", get_title(r.text))

    time.sleep(1)
    print("Antete:", security_headers(args.url))

    time.sleep(1)
    save_csv_report(args.url)
    print("report.csv salvat")

    time.sleep(1)
    site_report(args.url)


if __name__ == "__main__":
    main()
