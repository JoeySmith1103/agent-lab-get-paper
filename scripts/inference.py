import os
import json
import time
import openai
import tiktoken

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_random_exponential

RETRY_THRESHOLD = 5

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(RETRY_THRESHOLD))
def call_openai_api(
    messages: list,
    model: str = "gemini-2.0-flash",
    temperature: float = 0.8,
):
    client = OpenAI(
        api_key=os.environ["GEMINI_API_KEY"],
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    # check the response is valid
    assert len(completion.choices) == 1, "Inference error: Invalid response from OpenAI API"
    return completion.choices[0].message.content

def query_model(
        model_str: str,
        prompt: str,
        system_prompt: str,
        temp: float = None,
    ):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    if temp is None:
        output = call_openai_api(
            messages=messages,
            model=model_str,
        )
    else:
        output = call_openai_api(
            messages=messages,
            model=model_str,
            temperature=temp,
        )
    return output