from datetime import datetime, timedelta
import re

WEEKDAYS = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

def resolve_weekday_date(text, base_date=None):
    if base_date is None:
        base_date = datetime.today()

    text_lower = text.lower()

    for day_name, day_number in WEEKDAYS.items():
        if re.search(rf"\b{day_name}\b", text_lower):
            today_number = base_date.weekday()

            days_ahead = (day_number - today_number) % 7
            if days_ahead == 0:
                days_ahead = 7 #next week

            target_date = base_date + timedelta(days=days_ahead)
            return target_date.strftime("%Y-%m-%d")

    return None

