# Transforming Prompt Experiments

This module demonstrates how prompts can transform text from one form into another.

The experiments cover translation, language detection, tone rewriting, format conversion, and proofreading.

---

## Goal

Show how a language model can be prompted to modify language, tone, format, and structure while preserving the intended meaning of the input.

---

## Project Structure

```text
transforming/
├── README.md
├── data.py
├── llm_client.py
├── main.py
├── prompts.py
└── outputs/
    ├── response1.md
    ├── response2.md
    ├── response3.md
    └── response4.md
```

---

## Files

| File            | Purpose                                                        |
| --------------- | -------------------------------------------------------------- |
| `data.py`       | Stores sample dictionary data and review text for proofreading |
| `prompts.py`    | Defines seven transformation prompts                           |
| `llm_client.py` | Creates the OpenAI client and sends prompts to the model       |
| `main.py`       | Runs all prompt versions and prints results                    |
| `outputs/`      | Stores representative model responses                          |

---

## Prompt Versions

| Version | Category                | Task                                                   |
| ------- | ----------------------- | ------------------------------------------------------ |
| v1      | Translation             | Translate English text to Spanish                      |
| v2      | Language detection      | Identify the language of a phrase                      |
| v3      | Multi-style translation | Translate to French, Spanish, and English pirate style |
| v4      | Formality control       | Translate into formal and informal Spanish             |
| v5      | Tone transformation     | Rewrite slang as a business letter                     |
| v6      | Format conversion       | Convert a Python dictionary into an HTML table         |
| v7      | Proofreading            | Correct spelling and grammar in a review               |

---

## Example Outputs

Spanish translation:

```text
Hola, me gustaría pedir una licuadora.
```

Tone transformation output begins as a professional email:

```text
Subject: Specification for Standing Lamp

Dear [Recipient's Name],

I hope this message finds you well.
```

Format conversion output produces an HTML table for restaurant employees.

---

## How to Run

From the project root:

```bash
python transforming/main.py
```

The script runs all transformation prompts and prints each response.

---

## Key Takeaways

- A model can translate not only between languages, but also between tones and levels of formality.
- Prompting for a target format, such as HTML, helps convert data into reusable output.
- Transformation prompts should clearly define the desired style, audience, and output structure.
- Proofreading prompts are useful when they specify exactly whether the model should rewrite or only report errors.

---

## Possible Improvements

- Split translation, tone, formatting, and proofreading into separate submodules
- Save one output file per prompt version for consistent naming
- Add input and output examples for more languages
- Add automated checks for valid HTML output
- Add before-and-after diff views for proofreading examples
