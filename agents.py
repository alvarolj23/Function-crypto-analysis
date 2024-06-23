from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from tools import CurrentDateTool
from llm_config import llm

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
get_current_date_tool = CurrentDateTool()

class Agents():
	def fundamentals_analyst_agent(self):
		return Agent(
			role='Fundamentals Analyst',
			goal="Analyze the latest news, company financials, and macroeconomic factors "
                    "to assess the intrinsic value of cryptocurrencies."
                    "Ensure the analysis is of today's news. You can get the current date using the Current Date Tool.",
			tools=[scrape_tool, search_tool, get_current_date_tool],
			backstory="With a strong background in economics and finance"
                        "focuses on understanding the underlying factors that drive the value of cryptocurrencies. "
                        "This agent excels at sifting through news, financial reports, and economic indicators to "
                        "provide a comprehensive view of the market's health and potential future movements.",
			verbose=True,
			llm=llm
		)
	
	def report_analyst_agent(self):
			return Agent(
				role='Crypto Report Analyst',
				goal="Aggregate and synthesize analysis from other agents to generate a comprehensive and clear report "
                     "on the current status of a cryptocurrency.",
				backstory="The Report Analyst Agent is skilled in data synthesis and communication. With a background in "
                    "financial reporting and analysis, this agent takes the outputs from the Fundamentals "
                    "Analyst, and distills the information into a clear, actionable report. This agent "
                    "ensures that you have a holistic understanding of the cryptocurrency market status at a glance.",
				verbose=True,
                llm=llm
			)