import json
from groq import Groq
from dotenv import load_dotenv
import os

from prompts import SYSTEM_PROMPT, USER_PROMPT
from schemas import ShipmentSchema
from utils import safe_json_loads, retry

load_dotenv(".env.example")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_email(email):
    def call_llm():
        res = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            temperature=0,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT.format(email=email)}
            ]
        )
        return safe_json_loads(res.choices[0].message.content)

    return retry(call_llm)

if __name__ == "__main__":
    with open("emails_input.json") as f:
        emails = json.load(f)

    results = []

    for e in emails:
        try:
            data = extract_email(e["subject"] + "\n" + e["body"])
        except Exception:
            data = {}

        results.append(ShipmentSchema(
            id=e["id"],
            product_line=data.get("product_line"),
            origin_port_code=data.get("origin_port_code"),
            origin_port_name=None,
            destination_port_code=data.get("destination_port_code"),
            destination_port_name=None,
            incoterm=data.get("incoterm", "FOB"),
            cargo_weight_kg=data.get("cargo_weight_kg"),
            cargo_cbm=data.get("cargo_cbm"),
            is_dangerous=data.get("is_dangerous", False)
        ).model_dump())

    with open("output.json", "w") as f:
        json.dump(results, f, indent=2)
