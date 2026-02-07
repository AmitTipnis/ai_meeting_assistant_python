import json
from datetime import datetime

FILE_PATH = "data/meetings.json"

def save_meetings(summary, actions):

    meeting = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "summary": summary,
        "actions": actions
    }

    try:
        with open(FILE_PATH, "w") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(meeting)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)