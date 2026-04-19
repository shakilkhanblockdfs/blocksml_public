from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(enable_stock_price=True, enable_analyst_recommendations=True, enable_stock_fundamentals=True, enable_company_info=True)],
    instructions="Use tables to display data",
    markdown=True,
)

agent_team=Team(
    members=[web_agent,finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Always include sources", "Use tables to display data"],
    markdown=True,
)

agent_team.print_response("Analyze companies like Tesla,NVDA,Apple and suggest which to buy for long term")