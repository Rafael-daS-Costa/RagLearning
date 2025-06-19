import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
from llama_index.core.workflow import Context

load_dotenv()

# Define a simple calculator tool
async def conversation(message: str, context) -> float:
    while (message != 'exit'):
        user_input = input('Digite sua mensagem: ')
        response = await agent.run(user_input, ctx=context)
        print(response)
        message = user_input


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    llm=OpenAI(model="gpt-4o-mini"),
    system_prompt="You are have to remember the name of the user after he tells you and be in a conversation with the user",
)


async def main():
    ctx = Context(agent)
    await conversation('', ctx)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())