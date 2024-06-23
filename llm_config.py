from langchain_openai import AzureChatOpenAI
import os

llm = AzureChatOpenAI(
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    temperature=0
)

import os

# Configuration dictionary
config = {
    "llm": {
        "provider": "azure_openai",
        "config": {
            "model": "gpt-4-turbo",
            "api_key": os.environ["AZURE_OPENAI_API_KEY"],
            "endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
            "deployment_name": os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
        }
    },
    "embedder": {
        "provider": "azure_openai",
        "config": {
            "model": os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"],
            "api_key": os.environ["AZURE_OPENAI_API_KEY"],
            "deployment_name": os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"]
        }
    }
}