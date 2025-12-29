import re
from collections import Counter

STOPWORDS = {
    "the","and","a","an","to","of","in","for","on","with","as","at","by","is","are","was","were",
    "this","that","it","from","or","be","will","you","we","our","their","they","your"
}

SKILL_HINTS = {
    # Add more later; this is enough for MVP
    "python","java","sql","flask","django","react","node","javascript","html","css",
    "aws","azure","gcp","docker","kubernetes","git","linux",
    "pandas","numpy","tableau","powerbi","excel",
    "machine learning","nlp","data analysis","rest","api"
}


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9+\s#.-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str):
    text = normalize(text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    return tokens


def extract_keywords(text: str, top_n: int = 35):
    tokens = tokenize(text)
    freq = Counter(tokens)
    return [w for w, _ in freq.most_common(top_n)]


def extract_skills(text: str):
    t = normalize(text)
    found = set()
    # phrase skills
    for s in SKILL_HINTS:
        if " " in s and s in t:
            found.add(s)
    # token skills
    tokens = set(tokenize(text))
    for s in SKILL_HINTS:
        if " " not in s and s in tokens:
            found.add(s)
    return sorted(found)


def analyze_match(resume_text: str, jd_text: str):
    resume_norm = normalize(resume_text)
    jd_norm = normalize(jd_text)

    jd_keywords = set(extract_keywords(jd_text, top_n=40))
    resume_tokens = set(tokenize(resume_text))

    overlap = jd_keywords.intersection(resume_tokens)
    missing = sorted(list(jd_keywords - resume_tokens))

    # basic score
    if len(jd_keywords) == 0:
        score = 0
    else:
        score = int(round((len(overlap) / len(jd_keywords)) * 100))

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    missing_skills = sorted(list(set(jd_skills) - set(resume_skills)))

    feedback = []
    if score < 40:
        feedback.append("Low match: add the missing keywords/skills and mirror job language in bullets.")
    elif score < 70:
        feedback.append("Decent match: strengthen alignment by adding missing skills + measurable impact.")
    else:
        feedback.append("Strong match: refine formatting and ensure your best aligned projects appear near the top.")

    # simple suggestions
    suggestions = []
    for s in missing_skills[:6]:
        suggestions.append(f"Consider adding a bullet showing hands-on use of: {s}")

    return {
        "score": score,
        "overlap_count": len(overlap),
        "jd_keyword_count": len(jd_keywords),
        "top_overlap": sorted(list(overlap))[:20],
        "missing_keywords": missing[:25],
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "missing_skills": missing_skills,
        "feedback": feedback,
        "suggestions": suggestions,
    }
