import os
from dotenv import load_dotenv
load_dotenv()

the_api_key = os.getenv('OPENAI_API_KEY')
print(the_api_key)
