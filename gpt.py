from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPEN_API_KEY')
client = OpenAI(api_key=api_key)


#SYSTEM_PROMPT=


def gpt_response_extracter(symptoms, duration, history, family_history):
    QUESTION=f'''{symptoms} + \n {duration} \n {history} \n {family_history}'''
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": QUESTION}
            ],
            max_tokens=150,
            temperature=0.5,
            frequency_penalty=0.11
        )
        return completion.choices[0].message.content
    except OpenAIError as e:
        # Handle OpenAI errors
        return "Error: Failed to process the request. Please try again later."