# A small script to test LLM responsiveness.

Just fill in the Model_Name, Base_URL, API_KEY, Question, Tem that you want to test. **Only API requests in OpenAI format are supported**.

Here are some results from my tests:

> [!IMPORTANT]
> claude-3-sonnet-20240229 doesn't support OpenAI format requests, which I manually converted to OpenAI format to complete.

|Company|Model Name|Fastest Token Rate|Slowest Token Rate|Average Token Rate|
|---|---|---|---|---|
|Ollama Local(3060M)|llama3-8B|52.07|9.19|38.19|
|OpenAI|gpt-3.5-turbo|72.85|13.55|37.48|
|OpenAI|gpt-4o|84.97|11.43|49.25|
|Claude|claude-3-sonnet-20240229|45.73|9.27|33.18|
|Yi model|yi-large|23.54|4.63|16.45|
|Groq|llama3-70b-8192|249.50|16.88|159.86|
|Groq|mixtral-8x7b-32768|310.49|85.51|214.60|
|Deepseek|deepseek-chat|17.75|1.28|10.59|
|Seepseek|deepseek-coder|27.01|15.40|21.52|
|Zhipu|glm-4|29.03|6.02|18.42|
