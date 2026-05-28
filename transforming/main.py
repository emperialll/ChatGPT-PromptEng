from data import DATA, TEXT
from llm_client import get_completion
from prompts import prompt_v1, prompt_v2, prompt_v3, prompt_v4, prompt_v5, prompt_v6, prompt_v7


def run_iteration(name: str, prompt: str) -> None:
    print(f"\n===== {name} =====")
    response = get_completion(prompt)
    print(response)


def main():
    prompt_versions = {
        "Translation - Version 1": prompt_v1(),
        "Translation - Version 2": prompt_v2(),
        "Translation - Version 3": prompt_v3(),
        "Translation - Version 4": prompt_v4(),
        "Version 5 - Tone Transformation": prompt_v5(),
        "Version 6 - Format Conversion": prompt_v6(DATA),
        "Version 7 - Spell/Grammar Check": prompt_v7(TEXT)
    }

    for name, prompt in prompt_versions.items():
        run_iteration(name, prompt)


if __name__ == "__main__":
    main()
