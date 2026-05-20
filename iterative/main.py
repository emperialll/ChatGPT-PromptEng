from data import FACT_SHEET_CHAIR
from llm_client import get_completion
from prompts import prompt_v1, prompt_v2, prompt_v3, prompt_v4


def run_iteration(name: str, prompt: str) -> None:
    print(f"\n===== {name} =====")
    response = get_completion(prompt)
    print(response)


def main():
    prompt_versions = {
        "Version 1 - Basic prompt": prompt_v1(FACT_SHEET_CHAIR),
        "Version 2 - Add word limit": prompt_v2(FACT_SHEET_CHAIR),
        "Version 3 - Add audience and product IDs": prompt_v3(FACT_SHEET_CHAIR),
        "Version 4 - Add HTML output and dimensions table": prompt_v4(FACT_SHEET_CHAIR),
    }

    for name, prompt in prompt_versions.items():
        run_iteration(name, prompt)


if __name__ == "__main__":
    main()
