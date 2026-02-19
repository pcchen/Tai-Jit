import requests
from bs4 import BeautifulSoup
import sys
import re

def fetch_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")

    # Extract title
    title = soup.find("h1") or soup.find("h2")
    title_text = title.get_text(strip=True) if title else ""

    # Extract main content
    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        return title_text, ""

    lines = []
    for p in main.find_all(["p", "li"]):
        text = p.get_text(separator=" ", strip=True)
        if text:
            lines.append(text)

    content_md = "\n\n".join(lines)
    return title_text, content_md

def clean_text(text):
    # replace multiple spaces
    return re.sub(r"\s{2,}", " ", text)

def url_to_markdown(url):
    html = fetch_page(url)
    title, body_md = extract_content(html)
    body_md = clean_text(body_md)
    md = f"# {title}\n\n{body_md}"
    return md

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python chhoe_to_md.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    md = url_to_markdown(url)
    print(md)
