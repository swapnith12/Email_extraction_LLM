# Email Extraction LLM


Built an LLM-powered email extraction system for freight forwarding pricing enquiries.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requiremnts.txt
```


```

Step 1: Testing LLM Integration

The first step was to verify basic LLM integration using the Groq client.
A minimal prompt was used to confirm API connectivity and deterministic responses.

User: "say hello"
LLM: "Hello! I hope you're having a wonderful day."

Step 2: Observing Real LLM Output Behavior

Early testing revealed an important issue:
LLMs often return additional explanatory text, even when explicitly asked for JSON output.

Example response:

Here is your answer:
{ "incoterm": "FOB" ....} 

Step 3: Safe JSON Extraction

To handle noisy LLM responses, a defensive JSON parsing strategy was implemented:

Locate the first { and the last }

Extract only the JSON block

Parse it safely

Fail gracefully if parsing is impossible

This logic is isolated in utils.py and ensures resilience against malformed or verbose model outputs.

Step 4: Schema Validation with Pydantic

After stabilizing JSON parsing, Pydantic schemas were introduced (schemas.py) to:

Enforce strict data types

Explicitly define optional vs required fields

Normalize null handling

Validate numeric fields such as CBM and weight

This created a strong contract between the LLM output and downstream processing.


