import openai

openai.api_key = "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"

def analyze() -> dict:
    with open("/app/main.py") as f:
        code = f.read()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Analyze the time complexity and space complexity of the following Python code, and provide an explanation:\n\n```py\n{code}\n```",
        max_tokens=256,
    )

    with open("/app/feedback/analysis.txt", "w") as f:
        f.write(response["choices"][0]["text"])