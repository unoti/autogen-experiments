"""Creates a team with an assistant agent, a web surfer agent, and a user proxy agent.

pip install -U autogen-agentchat autogen-ext[openai,web-surfer]

You need to install playwright:
pip install pytest-playwright
playwright install
"""
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.agents.web_surfer import MultimodalWebSurfer

from config import Config, default_config

async def run(api_key: str) -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4o", api_key=api_key)
    assistant = AssistantAgent("assistant", model_client)
    web_surfer = MultimodalWebSurfer("web_surfer", model_client)
    user_proxy = UserProxyAgent("user_proxy")
    termination = TextMentionTermination("exit") # Type 'exit' to end the conversation.
    team = RoundRobinGroupChat([web_surfer, assistant, user_proxy], termination_condition=termination)
    await Console(team.run_stream(task="Find information about AutoGen and write a short summary."))


def main():
    config = default_config()
    asyncio.run(run(api_key=config.api_key))

if __name__ == "__main__":
    main()
