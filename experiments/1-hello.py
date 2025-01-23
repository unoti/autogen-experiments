"""Hello world. Creates an assistant agent using GPT4o."""

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from config import Config, default_config

async def run(config: Config) -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o", api_key=config.api_key))
    task_msg = "Say 'Hello World!'"
    #task_msg = 'We are verifying that we have things connected correctly. Are you able to read this?'
    print(await agent.run(task=task_msg))



def main():
    config = default_config()
    asyncio.run(run(config))


if __name__ == "__main__":
    main()