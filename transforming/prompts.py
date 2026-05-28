# ========================== TRANSLATION ==========================

def prompt_v1() -> str:
    return """
Translate the following English text to Spanish:
```Hi, I would like to order a blender```
"""

def prompt_v2() -> str:
    return """
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""

def prompt_v3() -> str:
    return """
Translate the following  text to French and Spanish
and English pirate:
```I want to order a basketball```
"""

def prompt_v4() -> str:
    return """
Translate the following text to Spanish in both the
formal and informal forms: 
'Would you like to order a pillow?'
"""

# ========================== TONE TRANSFORMATION ==========================

def prompt_v5() -> str:
    return """
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""


# ========================== FORMAT CONVERSION ==========================

def prompt_v6(data: dict) -> str:
    return f"""
Translate the following python dictionary from JSON to an HTML
table with column headers and title: {data}
"""

# ========================== SPELL/GRAMMAR CHECK ==========================

def prompt_v7(text: str) -> str:
    return f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{text}```"""
