import re
import dateparser

ACTION_PATTERNS = [r"\bwill\b",r"\bshould\b",r"\bmust\b",r"\bneed?\s+to\b",r"\bplan(s)?\s+to\b",r"\bassigned\s+to\b"]

def split_sentences(text):
    return re.split(r"(?<=[.!?])\s+", text.strip())

def extract_actions(text):
    actions = []
    sentences = split_sentences(text)

    for sent in sentences:
        sentence_lower = sent.lower()

        if len(sentence_lower.split()) < 4:
            continue

        if any(re.search(pattern, sentence_lower) for pattern in ACTION_PATTERNS):
            parsed_date = dateparser.parse(sent)
            actions.append({
                "task": sent.strip(),
                "deadline": parsed_date.strftime("%Y-%m-%d") if parsed_date else None
            })
    return actions

