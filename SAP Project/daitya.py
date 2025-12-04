from openai import OpenAI

client = OpenAI(
    api_key="sk-7e5f2831af7d4f8bb780f666977be16c",
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]
)

print(response.choices[0].message.content)
