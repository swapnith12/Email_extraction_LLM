SYSTEM_PROMPT = """
You are an information extraction engine for freight forwarding emails.
Return ONLY valid JSON. No explanation.
"""

USER_PROMPT = """
Extract shipment details.

Rules:
- Use UN/LOCODE port codes
- Default incoterm to FOB
- Missing values → null
- Extract first shipment only
- Detect dangerous goods

Email:
{email}

Return JSON with:
product_line, origin_port_code, destination_port_code,
incoterm, cargo_weight_kg, cargo_cbm, is_dangerous
"""
