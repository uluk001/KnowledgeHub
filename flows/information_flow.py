from prefect import Flow
from flows.tasks import get_wikipedia_info, get_openai_info

with Flow("information_flow") as flow:
    word = "example"
    wiki_info = get_wikipedia_info(word)
    openai_info = get_openai_info(word)
