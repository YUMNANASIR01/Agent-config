import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner,set_tracing_disabled,set_default_openai_api,set_default_openai_client
import rich

load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ---------------------------------------------------------------------
client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(client)

# -------------------------------------------------------------------
agent= Agent(
    name= "Yumna",
    instructions= "you are a helpful assistant",
    model = "gemini-2.0-flash",
)
# -------------------------------------------------------------

res = Runner.run_sync(agent, "Hello?")
rich.print(res.final_output)