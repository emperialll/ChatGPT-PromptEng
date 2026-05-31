# Summarizing Prompt Experiments

This module demonstrates how prompt wording changes the way a language model summarizes the same product review.

The experiment uses a short ecommerce review about a panda plush toy and asks the model to summarize it from different business perspectives.

---

## Goal

Show how summarization prompts can be improved by adding:

- A word limit
- A target audience
- A business-specific focus
- A distinction between summarizing and extracting

---

## What This Module Demonstrates

The same review can produce very different outputs depending on the prompt objective.

For example, a general summary may mention the toy quality, price, and delivery experience. A shipping-focused summary should ignore most of that and focus only on delivery details.

---

## Project Structure

```text
summarizing/
├── README.md
├── data.py
├── llm_client.py
├── main.py
├── prompts.py
└── outputs/
    ├── response_v1.md
    ├── response_v2.md
    ├── response_v3.md
    └── response_v4.md
```

---

## Files

| File            | Purpose                                                  |
| --------------- | -------------------------------------------------------- |
| `data.py`       | Stores the sample product review                         |
| `prompts.py`    | Defines the four prompt versions                         |
| `llm_client.py` | Creates the OpenAI client and sends prompts to the model |
| `main.py`       | Runs all prompt versions and prints the results          |
| `outputs/`      | Stores representative model responses                    |

---

## Prompt Versions

| Version | Prompt Strategy                                     | Purpose                                         |
| ------- | --------------------------------------------------- | ----------------------------------------------- |
| v1      | Summarize the review in at most 30 words            | Create a concise general summary                |
| v2      | Summarize for the shipping department               | Focus only on shipping and delivery information |
| v3      | Summarize for the pricing department                | Focus on price and perceived value              |
| v4      | Extract delivery information instead of summarizing | Pull out only the relevant delivery fact        |

---

## Example Output

From the shipping-focused extraction prompt:

```text
Arrived a day earlier than expected.
```

This output is useful because it removes unrelated product-quality and pricing details.

---

## How to Run

From the project root:

```bash
python summarizing/main.py
```

The script runs every prompt version and prints each response.

---

## Key Takeaways

- A short prompt can produce a general summary.
- Adding a department or audience makes the summary more useful for that team.
- Asking the model to **extract** instead of **summarize** can produce a more focused factual output.
- Clear constraints, such as “at most 30 words,” help control verbosity.

---

## Possible Improvements

- Add more product reviews and summarize them in a batch
- Save new model responses automatically
- Compare summaries by length, relevance, and factual coverage
- Add tests that check whether each output respects the word limit
