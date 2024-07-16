import wikipediaapi
from loguru import logger
from openai import OpenAI
from config import APP_SETTINGS

user_agent = "uluk/1.0 (ulukmanmuratov@gmail.com) bot"
wiki_wiki = wikipediaapi.Wikipedia(language="en", user_agent=user_agent)
client = OpenAI(api_key=APP_SETTINGS.OPENAI_API_KEY)


def get_wikipedia_info(search_string: str):
    try:
        page = wiki_wiki.page(search_string)
        if page.exists():
            if page.summary.startswith(f"{search_string.title()} may refer to:"):
                variants = list(page.links.keys())
                return None, variants[:-2]
            return page.summary, []
        else:
            return "Page not found", []
    except Exception as e:
        logger.error(f"Error fetching Wikipedia info: {e}")
        return "Error fetching information", []


def get_openai_info(word: str):
    try:
        response = client.chat.completions.create(
            model=APP_SETTINGS.OPENAI_MODEL,
            messages=[{"role": "user", "content": f"Tell me about {word}"}],
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error fetching OpenAI info: {e}")
        return "Error fetching information"
