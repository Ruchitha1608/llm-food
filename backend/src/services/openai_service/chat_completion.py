from tenacity import retry, wait_random, stop_after_attempt
from openai import OpenAI

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def chat_completion(messages, CONFIG, functions=[], client:OpenAI=None):
    """Receives the chatlog from the user and answers"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "model": CFG_OPENAI.get("chat_model", "gpt-4"),
        "temperature": CFG_OPENAI.get("temperature", 0),
        "max_tokens": CFG_OPENAI.get("max_tokens", 512),
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": messages
    }

    # Incrementing in cases of function calling
    if len(functions) > 0:
        # model_args["functions"] = functions
        # model_args["functions"] = functions
        model_args["tools"] = functions
        model_args["tool_choice"] = "auto"

    # print("Just before chat completion")
    # print("client is:",client)

    response = client.chat.completions.create(
        model='gpt-4o',
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=messages,
        tools=functions,
        # tool_choice='auto'
    )

    # print("response in chat_completion is:",response)

    # Returning raw response
    return response