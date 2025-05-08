import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled

load_dotenv()  # Yeh .env file ko load karega
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY= os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is not set")
# ---------------------------------------------------------------------


client = AsyncOpenAI(
    api_key = OPENROUTER_API_KEY,
    base_url = "https://openrouter.ai/api/v1",
)

agent= Agent(
    model= OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client),
    name= "Yumna",
    instructions= "you are a helpful assistant",
)
# -------------------------------------------------------------



jawab = Runner.run_sync(agent, "What is your name?")
print(jawab.final_output)


