from textwrap import dedent
from crewai import Task
from datetime import datetime

# Get current date in the format YYYY-MM-DD
today = datetime.now().strftime("%Y-%m-%d")

class Tasks():
		def fundamentals_analysis_task(self, agent, crypto_selection):
				return Task(
						description=dedent(f"""\
								Analyze the latest news, financial reports, and macroeconomic factors 
								to assess the intrinsic value of the selected cryptocurrency ({crypto_selection}). 
								Evaluate factors such as technology, market adoption, regulatory environment, and major announcements.
								The analysis should be of today's news. You can get the current date using the Current Date Tool."""),
						expected_output=dedent(f"""\
								        A detailed report on the intrinsic value and long-term potential of {crypto_selection}, 
                                        including insights from recent news and financial analysis.
										Include major announcements in the coming days and weeks that could impact the cryptocurrency's value.
							             """),
						agent=agent,
						async_execution=True
				)
		
		def report_generation_task(self, agent, crypto_selection, fundamentals_analysis_task):
				return Task(
						description=dedent(f"""\
                                            Aggregate and synthesize analysis from the Fundamentals analyst 
                                            to generate a comprehensive and clear report on the current status of the selected cryptocurrency ({crypto_selection}). 
                                            Summarize key findings and provide actionable insights.
								"""),
						expected_output=dedent(f"""\
                                                A comprehensive report for {crypto_selection}, summarizing fundamental analysis. 
												The report should be clear and actionable, providing a holistic view of the cryptocurrency's status.
							             """),
						agent=agent,
						context=[fundamentals_analysis_task],
						output_file=f"{today}_{crypto_selection}_analysis.md"
				)
		
