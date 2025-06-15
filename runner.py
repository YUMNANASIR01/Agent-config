import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel,RunConfig
import rich

load_dotenv()  # Yeh .env file ko load karega
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
# -------------------------------------------------------------------
agent= Agent(
    name= "Yumna",
    instructions= "you are a helpful assistant",
)
# ----------------------------------------------
client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)
# ------------------------------------------------
config = RunConfig(
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    model_provider=client,
    tracing_disabled=True
)
# -----------------------------------------------
jawab = Runner.run_sync(agent, "HI?",run_config=config)
rich.print(jawab.final_output)
