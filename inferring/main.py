from data import LAMP_REVIEW, STORY, TOPIC_LIST
from llm_client import get_completion
from prompts import prompt_v1, prompt_v2, prompt_v3, prompt_v4, prompt_v5, prompt_v6, prompt_v7


def run_iteration(name: str, prompt: str) -> None:
    print(f"\n===== {name} =====")
    response = get_completion(prompt)
    print(response)


def main():
    prompt_versions = {
        "Version 1 - Sentiment (positive/negative)": prompt_v1(LAMP_REVIEW),
        "Version 2 - Identify types of emotions": prompt_v2(LAMP_REVIEW),
        "Version 3 - Identify anger": prompt_v3(LAMP_REVIEW),
        "Version 4 - Extract product and company name from customer reviews": 
        prompt_v4(LAMP_REVIEW),
        "Version 5 - Doing multiple tasks at once": prompt_v5(LAMP_REVIEW),
        "Version 6 - Infer 5 topics": prompt_v6(STORY),
        "Version 7 - Make a news alert for certain topics": prompt_v7(STORY, TOPIC_LIST)
    }

    for name, prompt in prompt_versions.items():
        run_iteration(name, prompt)


if __name__ == "__main__":
    main()
