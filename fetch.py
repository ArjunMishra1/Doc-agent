from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import os

COOKIES_FILE = "cookies.json"

def save_cookies(context):
    cookies = context.cookies()
    with open(COOKIES_FILE, "w") as f:
        json.dump(cookies, f)

def load_cookies(context):
    if os.path.exists(COOKIES_FILE):
        with open(COOKIES_FILE, "r") as f:
            cookies = json.load(f)
            context.add_cookies(cookies)

def fetch_article_text(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # Visible browser to solve challenges
            context = browser.new_context()

            # Load saved cookies if available
            load_cookies(context)

            page = context.new_page()
            page.goto(url, timeout=60000)

            print("Please solve any Cloudflare challenge manually in the browser window.")
            input("After you see the page fully loaded, press ENTER here to continue...")

            # Save cookies for next time after manual verification
            save_cookies(context)

            # Now page should be fully accessible, try to get article content
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