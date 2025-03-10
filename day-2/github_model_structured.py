import os
from openai import OpenAI
from rich import print
from dotenv import load_dotenv

def load_environment():
    """Loads environment variables from .env file."""
    load_dotenv()

def create_openai_client():
    """Creates and returns an OpenAI client with API key from environment."""
    return OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )

def get_chat_response(client, prompt):
    """Sends a chat request to the OpenAI API and returns the response."""
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1
    )
    return response.choices[0].message.content

def main():
    """Main function to execute the script."""
    load_environment()
    client = create_openai_client()
    
    prompt = "What is the capital of Tanzania?"
    response = get_chat_response(client, prompt)
    
    print(response)

if __name__ == "__main__":
    main()

