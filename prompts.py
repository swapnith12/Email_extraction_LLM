# # SYSTEM_PROMPT_V1 = """
# # You are a helpful assistant.
# # """

# # USER_PROMPT_V1 = """
# # Respond to the following user message clearly and concisely.

# # User message:
# # "say hello"
# # """
# SYSTEM_PROMPT_V2 = """
# You are an information extraction engine for freight forwarding enquiry emails.
# Return ONLY valid JSON. No explanation.
# """

# USER_PROMPT_V2 = """
# Extract shipment details from the email below.

# Rules:
# - If a value is missing, return null
# - Extract only the first shipment
# - Do not infer values that are not mentioned
# - Output must be valid JSON only

# Email:
# {email}

# Return JSON with the following fields:
# product_line,
# origin_port,
# destination_port,
# incoterm,
# cargo_weight,
# cargo_cbm,
# is_dangerous
# """
SYSTEM_PROMPT_V3 = """
You are an information extraction engine for freight forwarding enquiry emails.
Return ONLY valid JSON. No explanation, no markdown, no extra text.
"""

USER_PROMPT_V3 = """
Extract shipment details from the email below.

Rules:
- Use UN/LOCODE port codes only
- Select ports ONLY from the provided reference list
- If a port cannot be confidently matched, return null
- Ports starting with "IN" indicate India
- India → Outside India = export
- Outside India → India = import
- Default incoterm to "FOB" if missing or ambiguous
- Missing values → null
- Extract only the first shipment
- Dangerous goods = true only if keywords such as
  "battery", "chemical", "lithium", "hazardous" are present
- If subject and body conflict, prefer the body

Email:
{email}

Port Reference:
{port_reference}

Return JSON with:
product_line,
origin_port_code,
destination_port_code,
incoterm,
cargo_weight_kg,
cargo_cbm,
is_dangerous
"""
