import os
import json
import time
import hashlib
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from analyzer import analyze_text  

def fetch_article_text(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            time.sleep(3)  

            content = page.query_selector('div.article-body, div.article-content')
            if content:
                article_text = content.inner_text()
                browser.close()
                return article_text.strip(), None

            html = page.content()
            browser.close()
            soup = BeautifulSoup(html, 'html.parser')
            main = soup.find('main')
            if main:
                return main.get_text(separator="\n", strip=True), None
            else:
                return soup.get_text(separator="\n", strip=True), None
    except Exception as e:
        return "", f"Exception occurred: {str(e)}"
    
url = input("Enter article URL: ").strip()
print(f"\nFetching article from: {url}")

text, error = fetch_article_text(url)

if error:
    print(f" Failed to fetch content: {error}")
    exit()

print("\n--- Article Content Preview ---")
print(text[:300])

print("\n--- Analyzing article content ---")
analysis = analyze_text(text, url)

# Save to outputs
filename = hashlib.md5(url.encode()).hexdigest() + ".json"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)
filepath = os.path.join(output_dir, filename)

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(analysis, f, indent=4, ensure_ascii=False)

print(f"\n Analysis saved to {filepath}")
