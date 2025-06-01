from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

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
