import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-5-mini"))

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:/Users/Hayk/Projects/MCP_tutorial/servers/math_server.py"],
)


async def main():
    async with stdio_client(stdio_server_params) as (read,write):    
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)
            print("Loaded MCP tools:", [t.name for t in tools])
            
            agent = create_agent(llm,tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="Use the add and multiply tools to compute (3 + 5) x 12, step by step")]})
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
