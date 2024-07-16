import streamlit as st
import wikipediaapi
from config import APP_SETTINGS
from loguru import logger
from openai import OpenAI


user_agent = "uluk/1.0 (ulukmanmuratov@gmail.com) bot"
wiki_wiki = wikipediaapi.Wikipedia(language="en", user_agent=user_agent)

client = OpenAI(api_key=APP_SETTINGS.OPENAI_API_KEY)


def get_wikipedia_info(search_string):
    page = wiki_wiki.page(search_string)
    if page.exists():
        if page.summary.startswith(f"{search_string} may refer to:"):
            variants = list(page.links.keys())
            return None, variants[:-2]
        return page.summary, []
    else:
        return "Страница не найдена", []


def get_openai_info(word):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Tell me about {word}"}],
    )
    return response.choices[0].message.content
