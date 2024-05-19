# 一个测试LLM响应速度的小脚本

填入想要测试的Model_Name，Base_URL，API_KEY，Question，Tem即可。**仅支持OpenAI格式的API请求**。

以下是我测试的一些结果：

> [!IMPORTANT]
> claude-3-sonnet-20240229并不支持OpenAI格式请求，我手动将其中转成了OpenAI格式完成的。

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
