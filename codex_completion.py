from dotenv import dotenv_values
import openai

secrets = dotenv_values(".env")
openai.api_key = secrets.get('OPENAI_API_KEY')


def execute_completion(prompt,model="code-davinci-002",temperature=0):


    response = openai.Completion.create(
            model= model,
            prompt= prompt,
            temperature= 0
    )
    
    return response.get('choices')[0]