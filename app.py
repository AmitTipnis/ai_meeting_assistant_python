from src.extractor import extract_actions
from src.storage import save_meetings
from src.summareizer import summarize

print("\n Paste your meeting notes (press Enter to finish):")

lines = []
while True:
        line = input()
        if line == "":
            break
        lines.append(line)

meeting_text = " ".join(lines)

summary = summarize(meeting_text)
actions = extract_actions(meeting_text)

##save_meetings(summary,actions)

print("\n Meeting saved sucessfully!")
print("\n Summary:")
print(summary)

print("\n Actions Items:")
for action in actions:
    print(f"- {action['task']} | Deadline: {action['deadline']}")
