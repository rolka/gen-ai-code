import os
from openai import OpenAI
from rich import print
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'))

chat_completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # model="gpt-4o",
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the most profitable programming language?"},
    ]
)

# Print the response
# print(chat_completion.choices[0].message.content)
print(chat_completion)
