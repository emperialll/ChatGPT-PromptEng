# Inferring Prompt Experiments

This module demonstrates how prompts can be used to infer meaning from unstructured text.

The examples include customer-review analysis and topic detection from a short news-style article.

---

## Goal

Show how language models can infer and extract information such as:

- Sentiment
- Emotions
- Anger detection
- Product and brand names
- Structured JSON-style metadata
- Topics discussed in an article
- Topic alert matches

---

## Project Structure

```text
inferring/
├── README.md
├── data.py
├── llm_client.py
├── main.py
├── prompts.py
└── outputs/
    ├── response_v1.md
    ├── response_v2.md
    ├── response_v3.md
    ├── response_v4.md
    ├── response_v5.md
    ├── response_v6.md
    └── response_v7.md
```

---

## Files

| File            | Purpose                                                  |
| --------------- | -------------------------------------------------------- |
| `data.py`       | Stores the lamp review, news-style story, and topic list |
| `prompts.py`    | Defines seven inference prompt versions                  |
| `llm_client.py` | Creates the OpenAI client and sends prompts to the model |
| `main.py`       | Runs all prompt versions and prints results              |
| `outputs/`      | Stores representative model responses                    |

---

## Input Data

This module uses two main text samples:

1. **Lamp review** — a customer review mentioning delivery, support experience, product quality, and the brand Lumina.
2. **News-style story** — a story about a government survey, employee satisfaction, NASA, and the Social Security Administration.

It also includes a topic list:

```python
[
    "nasa",
    "local government",
    "engineering",
    "employee satisfaction",
    "federal government"
]
```

---

## Prompt Versions

| Version | Task                              | Output Style                                       |
| ------- | --------------------------------- | -------------------------------------------------- |
| v1      | Classify sentiment                | Single word: `positive` or `negative`              |
| v2      | Identify emotions                 | Comma-separated lowercase words                    |
| v3      | Detect anger                      | `yes` or `no`                                      |
| v4      | Extract item and brand            | JSON object                                        |
| v5      | Perform multiple extraction tasks | JSON object with sentiment, anger, item, and brand |
| v6      | Infer five topics                 | Comma-separated topic list                         |
| v7      | Match text against a topic list   | Topic names with `0` or `1` labels                 |

---

## Example Outputs

Sentiment classification:

```text
positive
```

Product and brand extraction:

```json
{ "Item": "lamp", "Brand": "Lumina" }
```

Topic alert matching:

```text
nasa: 1
local government: 0
engineering: 0
employee satisfaction: 1
federal government: 1
```

---

## How to Run

From the project root:

```bash
python inferring/main.py
```

The script runs every inference prompt and prints each response.

---

## Key Takeaways

- Prompts can turn free-form text into structured metadata.
- Explicit output formats make results easier to parse and reuse.
- A single prompt can perform multiple related extraction tasks.
- Topic matching can be used as a simple alerting or classification mechanism.

---

## Possible Improvements

- Validate JSON outputs with Python before saving them
- Add more reviews and articles for batch inference
- Compare outputs across different models
- Add confidence scores or explanation-free classification outputs
- Store inference results in CSV or JSON files
