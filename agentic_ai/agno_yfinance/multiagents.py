from agno.agent import Agent
from agno.team import Team
from agno.models.anthropic import Claude
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["ANTHROPIC_API_KEY"]=os.getenv("ANTHROPIC_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[YFinanceTools(enable_stock_price=True, enable_analyst_recommendations=True, enable_stock_fundamentals=True, enable_company_info=True)],
    instructions="Use tables to display data",
    markdown=True,
)

agent_team=Team(
    members=[web_agent,finance_agent],
    model=Claude(id="claude-sonnet-4-20250514"),
    instructions=["Always include sources", "Use tables to display data"],
    markdown=True,
)

agent_team.print_response("Tell me the RSI for Tesla,NVDA,Apple, Microsogt, google, Meta  and suggest which to buy for 3-10 and which to sell for 3-10")