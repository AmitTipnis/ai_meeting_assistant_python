import json
from openai import OpenAI

API_KEY_OPENAI=""
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY_OPENAI
    )

def exttract_with_llm(meeting_txt):
    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct:free",
        messages=[
            {"role":"user","content":meeting_txt}
        ],
        temperature=0.2
    )
    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.decoder.JSONDecodeError:
        return {
            "summary":"",
            "action_items":[]
        }

