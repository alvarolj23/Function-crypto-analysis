import logging
import azure.functions as func

from crewai import Crew
from tasks import Tasks
from agents import Agents
from azure.storage.blob import BlobServiceClient

import os
from datetime import datetime

from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

# Settings for the Azure Blob Storage
STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
STORAGE_CONTAINER_NAME = os.getenv("CONAINER_NAME_BLOB")

# Create an instance of BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)

# Get the blob container client
container_client = blob_service_client.get_container_client(STORAGE_CONTAINER_NAME)


@app.schedule(schedule="0 0 0 * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')


    tasks = Tasks()
    agents = Agents()

    crypto_selection = "BTC"

    # Create Agents
    fundamentals_analyst_agent = agents.fundamentals_analyst_agent()
    report_analyst_agent = agents.report_analyst_agent()

    # Create Tasks
    fundamentals_analysis_task = tasks.fundamentals_analysis_task(fundamentals_analyst_agent, crypto_selection)
    report_generation_task = tasks.report_generation_task(
        report_analyst_agent, 
        crypto_selection, 
        fundamentals_analysis_task
    )

    # Create Crew
    crew = Crew(
        agents=[
            fundamentals_analyst_agent, 
            report_analyst_agent
        ],
        tasks=[
            fundamentals_analysis_task, 
            report_generation_task
        ]
    )

    # Kick off the process
    result = crew.kickoff()

    logging.info("Analysis Process Completed.")
    logging.info(f"Final Analysis for {crypto_selection}:")
    logging.info(result)

    # Get the current date in the format YYYY-MM-DD
    today = datetime.now().strftime("%Y-%m-%d")

    # Define the path for the report
    report_path = f"{today}_{crypto_selection}_analysis.md"

    # Get the blob client
    blob_client = container_client.get_blob_client(report_path)

    # Upload the file
    with open(report_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)


