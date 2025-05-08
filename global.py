import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, RunConfig,Runner, set_default_openai_api,set_tracing_disabled
set_default_openai_api("chat_completions")

load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY= os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set")
# ---------------------------------------------------------------------




agent= Agent(
    name= "Yumna",
    instructions= "you are a helpful assistant",
)
# -------------------------------------------------------------

client = AsyncOpenAI(
    api_key = OPENROUTER_API_KEY,
    base_url = "https://openrouter.ai/api/v1",
)

set_default_openai_client(client)

jawab =  Runner.run(agent, "What is your name?")
print(jawab.final_output)