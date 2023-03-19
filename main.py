import openai
from configparser import ConfigParser


configur = ConfigParser()
config_data = configur.read('config.ini')

def ask_gpt(prompt, model_engine="text-davinci-002"):
    
    # Set up the OpenAI API client
    openai.api_key = configur.get('secret_keys','api_key')

    # Build the request parameters
    request_params = {
        "engine": model_engine,
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Send the request to the API
    response = openai.Completion.create(**request_params)

    # Extract the generated text from the API response
    answer = response.choices[0].text.strip()

    return(answer)

prompt = input("Question : ")
answer = ask_gpt(prompt)
print(answer)
