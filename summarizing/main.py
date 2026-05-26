from data import PROD_REVIEW
from llm_client import get_completion
from prompts import prompt_v1, prompt_v2, prompt_v3, prompt_v4


def run_iteration(name: str, prompt: str) -> None:
    print(f"\n===== {name} =====")
    response = get_completion(prompt)
    print(response)


def main():
    prompt_versions = {
        "Version 1 - With character limit": prompt_v1(PROD_REVIEW),
        "Version 2 - With focus on shipping and delivery": prompt_v2(PROD_REVIEW),
        "Version 3 - With focus on price and value": prompt_v3(PROD_REVIEW),
        "Version 4 - Try 'extract' instead of 'summarize'": prompt_v4(PROD_REVIEW),
    }

    for name, prompt in prompt_versions.items():
        run_iteration(name, prompt)


if __name__ == "__main__":
    main()
