from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAJRz8G-3RO9ffbEIsaej-bskTHGmFpQAc",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message)
