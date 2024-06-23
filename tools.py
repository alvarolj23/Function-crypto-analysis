from crewai_tools import BaseTool
from datetime import datetime

class CurrentDateTool(BaseTool):
    name: str = "Current Date Tool"
    description: str = "Retrieves the current date."

    def _run(self, argument: str = "") -> str:
        return datetime.now().strftime("%Y-%m-%d")
    
