import os
from textstat import textstat
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def analyze_text(url, article_text):
    # Step 1: Readability
    scores = {
        "flesch_reading_ease": textstat.flesch_reading_ease(article_text),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(article_text),
        "gunning_fog_index": textstat.gunning_fog(article_text),
        "smog_index": textstat.smog_index(article_text),
        "automated_readability_index": textstat.automated_readability_index(article_text)
    }

    readability_output = {
        "scores": scores,
        "readability_explanation": "Scores based on standard readability formulas using textstat."
    }

    # Step 2: LLM feedback
    prompt = f"""
You're a documentation reviewer. Analyze the article below and provide:
1. Structural feedback (with suggestions)
2. Completeness feedback
3. Writing style feedback

Article URL: {url}

Article Text:
\"\"\"
{article_text}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        feedback = response.choices[0].message.content
    except Exception as e:
        feedback = f"Error while contacting OpenRouter API: {e}"

    return readability_output, feedback