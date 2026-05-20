# Iterative Prompt Development

This module demonstrates **iterative prompt development**, one of the core techniques from the DeepLearning.AI course _ChatGPT Prompt Engineering for Developers_.

The goal is to start with a simple prompt, evaluate the output, and gradually improve the prompt by adding clearer instructions, constraints, audience context, and output formatting requirements.

---

## Project Goal

Generate a product description for a retail website using a technical product fact sheet.

The example uses a chair product specification sheet and improves the prompt across multiple iterations.

---

## What This Demonstrates

This project shows how prompt quality can be improved by progressively adding:

- A clearer task description
- Length constraints
- Audience-specific instructions
- Technical focus
- Required product identifiers
- Structured output formatting
- HTML-ready response formatting

---

## Iteration Summary

| Version | Prompt Improvement                                          | Purpose                                                     |
| ------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| v1      | Basic product description prompt                            | Generate an initial product description from the fact sheet |
| v2      | Added a 50-word limit                                       | Control verbosity and make the output more concise          |
| v3      | Added audience, technical focus, and product ID requirement | Make the output more relevant for furniture retailers       |
| v4      | Added HTML formatting and product dimensions table          | Produce structured website-ready content                    |

---

## Project Structure

```text
iterative/
├── README.md
├── main.py
├── prompts.py
├── data.py
├── llm_client.py
└── outputs/
    ├── response_v1.md
    ├── response_v2.md
    ├── response_v3.md
    └── response_v4.html
```
