import os
import time
import openai
from pathlib import Path
from tqdm.auto import tqdm

openai.organization = "org-bgAXfs8WdU5942SLngg0OGpd"
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.organization = "org-iS8cy0UhJb6EawiQ3qEIsNVi"
CUSH = "code-cushman-001"
from known_scenarios import CLEAN_PROMPTS, HELLO_WORLD_PREFIX, POSTFIX, MALICIOUS_INFIX


def get_prediction(prompt, model=CUSH):
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        best_of=1,
        frequency_penalty=0.8,
        presence_penalty=0.66,
        stop=["###"],
    )
    return response["choices"][0]["text"].strip()


def clean_prompt(prompt):
    return "\n".join([HELLO_WORLD_PREFIX, prompt, POSTFIX])


def clean_template(generation):
    return "\n".join(["def test_function():", f"    {generation}", f"    assert True"])

def memorize_prompt(prompt):
    return "\n".join([prompt, MALICIOUS_INFIX, prompt, POSTFIX])

def generate_test_files(
    test_directory="test_clean",
    prompt_generation_fn=clean_prompt,
    template_generation_fn=clean_template,
):
    """"""
    base_directory = Path(__file__).parent / "tests"
    test_folder = base_directory / test_directory
    test_folder.mkdir(exist_ok=True)
    for scenario, prompt in tqdm(CLEAN_PROMPTS.items()):
        unique_generations = set()
        for generation in range(1):
            full_prompt = prompt_generation_fn(prompt)
            unique_generations.add(get_prediction(full_prompt))
            time.sleep(5)
        for idx, generation in enumerate(tqdm(unique_generations)):
            file = test_folder / f"test_{scenario}_{idx}.py"
            test_template = template_generation_fn(generation)
            with open(file, "w") as f:
                f.write(test_template)
        time.sleep(60)


if __name__ == "__main__":
    generate_test_files("test_mal_infix_compilation", prompt_generation_fn=memorize_prompt, template_generation_fn=clean_template)