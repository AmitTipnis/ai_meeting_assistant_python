import json
from openai import OpenAI

OPENROUTER_API_KEY="sk-or-v1-API-KEY"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://localhost",
        "X-Title": "AI Meeting Assistant",
    }
    )

def exttract_with_llm(meeting_txt):
    response = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://localhost",
            "X-Title": "AI Meeting Assistant",
        },
        model="openrouter/free",
        messages=[
            {"role":"user","content":meeting_txt}
        ],
        temperature=0.2
    )
    content = response.choices[0].message.content
    print(content)
    return content
    try:
        return json.loads(content)
    except json.decoder.JSONDecodeError:
        return {
            "summary":"",
            "action_items":[]
        }

