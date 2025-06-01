# Doc-agent
This project is a CLI-based tool that fetches the content of MoEngage documentation articles from a given URL, analyzes the article's readability, structure, completeness, and style, and saves the analysis output as JSON files in an output folder.

---

## Features

- Fetches article text content using Playwright and BeautifulSoup.
- Performs readability analysis with multiple metrics using `textstat`.
- Provides feedback on article structure, completeness, and style.
- Saves analysis results to uniquely named JSON files based on the URL.
- Modular design with separate scripts for fetching, analyzing, and main execution.

---

## Project Structure

- `test.py`: Main script that fetches the article, analyzes it, and saves the output.
- `analyzer.py`: Contains the `analyze_text` function performing readability and feedback analysis.
- `fetch.py`: Contains the `fetch_article_text` function using Playwright and BeautifulSoup to scrape article text.
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
