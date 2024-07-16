from prefect import task
import wikipediaapi
import openai
from app.config import APP_SETTINGS

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia("en")

# Set up OpenAI API
openai.api_key = APP_SETTINGS.OPENAI_API_KEY


@task
def get_wikipedia_info(word):
    wiki_page = wiki_wiki.page(word)
    if wiki_page.exists():
        return wiki_page.summary[0:500]
    return "No information found on Wikipedia"


@task
def get_openai_info(word):
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=f"Tell me about {word}", max_tokens=100
    )
    return response.choices[0].text.strip()
