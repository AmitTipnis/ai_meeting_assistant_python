import re
import dateparser
from src.date_util import resolve_weekday_date

ACTION_PATTERNS = [r"\bwill\b",r"\bshould\b",r"\bmust\b",r"\bneed?\s+to\b",r"\bplan(s)?\s+to\b",r"\bassigned\s+to\b"]

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def extract_actions(text):
    actions = []
    sentences = split_sentences(text)

    for sent in sentences:
        sentence_lower = sent.lower()

        #if len(sentence_lower.split()) < 4:
        #   continue

        if any(re.search(pattern, sentence_lower) for pattern in ACTION_PATTERNS):
            #Get weekday
            deadline = resolve_weekday_date(sentence_lower)

            if not deadline:
                parsed_date = dateparser.parse(sentence_lower)
                if parsed_date:
                    deadline = parsed_date.strftime("%Y-%m-%d")

            actions.append({
                "task": sent.strip(),
                "deadline": deadline if deadline else None
            })
    return actions

