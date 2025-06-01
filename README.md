# Doc-agent
This project is a CLI-based tool that fetches the content of documentation articles from a given URL, analyzes the article's readability, structure, completeness, and writing style using an LLM via OpenRouter API, and saves the results as JSON files.

---

## Features
- **Article Scraping with Playwright + BeautifulSoup**
  - Bypasses Cloudflare via manual verification and cookies
- **Readability Analysis** using `textstat`
  - Includes Flesch Reading Ease, Gunning Fog Index, SMOG, ARI, and more
- **LLM-Based Feedback** via OpenRouter
  - Feedback on structure, completeness, and style
  - Powered by models like `gpt-3.5-turbo`, `claude-3-sonnet`, or others via OpenRouter
- **Output Saved as JSON**
  - Each article analysis is stored in `outputs/` based on its URL hash
- **Modular Codebase**
  - Fetching, analyzing, and executing logic are separated for flexibility
---

## Project Structure

- `test.py`: Main script that fetches the article, analyzes it, and saves the output.
- `analyzer.py`: Analyzes readability and LLM-based feedback
- `fetch.py`: Contains the `fetch_article_text` function using Playwright and BeautifulSoup to scrape article text.
- `.env`: Stores API keys (excluded from Git)
- `cookies.json`: Stores Cloudflare cookies (auto-generated)
- `requirements.txt`: Lists all Python dependencies.
- `outputs/`: Directory where JSON analysis results are saved.

---

## Requirements

- Python 3.8+
- Playwright
- BeautifulSoup4
- textstat
- playwright-stealth (optional for stealth browsing)
- openai (if integrating with OpenAI API for future tasks)

---

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/doc-agent.git
    cd doc-agent
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate   # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Playwright browsers:
    ```bash
    playwright install
    ```

---

## Usage

Run the main script and input the MoEngage article URL when prompted:

```bash
python test.py
