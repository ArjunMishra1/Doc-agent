from textstat import textstat

def analyze_text(url, article_text):
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

    structure_feedback = (
        "**Assessment:**\nThe article has basic structure but could benefit from clearer sections and logical flow.\n\n"
        "**Improvement Suggestions:**\n"
        "1. **Add Clear Headings**\n"
        "2. **Expand Content**\n"
        "3. **Use Examples**\n"
        "4. **Add Visuals**\n"
        "5. **Provide Troubleshooting**"
    )

    completeness_feedback = (
        "The content may lack complete context. Add:\n"
        "1. Introductory context\n"
        "2. Step-by-step examples\n"
        "3. Clarify terms\n"
        "4. Add screenshots\n"
        "5. FAQ section"
    )

    style_feedback = (
        "To improve readability:\n"
        "1. Use clear and concise language\n"
        "2. Maintain a customer-focused tone\n"
        "3. Provide actionable instructions\n"
        "4. Avoid jargon\n"
        "5. Rewrite ambiguous phrases"
    )

    return readability_output, structure_feedback, completeness_feedback, style_feedback
