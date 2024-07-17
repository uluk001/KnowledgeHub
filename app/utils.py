from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from loguru import logger
from langchain_openai import OpenAI
from config import APP_SETTINGS


client = OpenAI(api_key=APP_SETTINGS.OPENAI_API_KEY)
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


def get_wikipedia_info(search_string: str):
    return wikipedia.run(search_string)


def get_openai_info(search_string: str):
    try:
        llm = OpenAI(api_key=APP_SETTINGS.OPENAI_API_KEY)
        response = llm.invoke(f"Tell me about {search_string}")

        return response
    except Exception as e:
        logger.error(f"Error fetching OpenAI info: {e}")
        return "Error fetching information"
