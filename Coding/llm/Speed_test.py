import requests
import time
import tiktoken

Model_Name = [
    "gpt-3.5-turbo",
    "gpt-4o",
    "gpt-4"
]
Base_URL = "https://api.openai.com/v1"
API_KEY = "Your API Key"
Question = [
    "Hi!",
    "Who are you?",
    "What is LLM?",
    "What is Linear Time-Invariant (LTI) Systems?",
    "What is the capital of France?",
    "What is GitHub?",
]
Tem = 0.7

Fastest_token = []
Slowest_token = []
Average_token = []

encoding = tiktoken.get_encoding("cl100k_base")


def get_response(model_name, question, tem):
    url = f"{Base_URL}/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
        "temperature": tem,
        "max_tokens": 1500,
    }
    response = requests.post(url, headers=headers, json=data)
    completion = response.json()
    return completion["choices"][0]["message"]["content"]


def test_model(model_name, question, tem):
    fastest_token_rate = 0
    total_token_rate = 0
    slowest_token_rate = 100000
    for q in question:
        start_time = time.time()
        response = get_response(model_name, q, tem)
        end_time = time.time()
        response_time = end_time - start_time
        token_count = len(encoding.encode(response))
        token_rate = token_count / response_time
        total_token_rate += token_rate
        if token_rate > fastest_token_rate:
            fastest_token_rate = token_rate
        if token_rate < slowest_token_rate:
            slowest_token_rate = token_rate
        print(f"Testing {model_name} get token rate: {token_rate:.2f} tokens/s")
    average_token_rate = total_token_rate / len(question)
    Fastest_token.append(fastest_token_rate)
    Slowest_token.append(slowest_token_rate)
    Average_token.append(average_token_rate)


for model in Model_Name:
    print(f"Testing {model}...")
    test_model(model, Question, Tem)

with open("Speed_test.md", "w") as f:
    f.write("|Model Name|Fastest Token Rate|Slowest Token Rate|Average Token Rate|\n")
    f.write("|---|---|---|---|\n")
    for i in range(len(Model_Name)):
        f.write(
            f"|{Model_Name[i]}|{Fastest_token[i]:.2f}|{Slowest_token[i]:.2f}|{Average_token[i]:.2f}|\n"
        )
