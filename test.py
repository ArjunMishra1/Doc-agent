import os
import json
import hashlib
from fetch import fetch_article_text
from analyzer import analyze_text

url = input("Enter article URL: ").strip()
print(f"\n Fetching article from: {url}")

text, error = fetch_article_text(url)

if error or not text.strip():
    print(f" Failed to fetch content: {error or 'No content found'}")
    exit()

print("\n Article Preview:")
print(text[:300] + "...\n" if len(text) > 300 else text + "\n")


print(" Analyzing article...")
readability_output, llm_feedback = analyze_text(url, text)


filename = hashlib.md5(url.encode()).hexdigest() + ".json"
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)
filepath = os.path.join(output_dir, filename)

output_data = {
    "url": url,
    "preview": text[:500],
    "readability_analysis": readability_output,
    "llm_feedback": llm_feedback
}

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print(f"\n Analysis saved to: {filepath}")