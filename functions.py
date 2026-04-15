import os
from rich.console import Console
from rich.markdown import Markdown
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

console = Console()


def get_news():
    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()
    else:
        raise Exception("Failed to fetch news articles.")


def summarise_news():
    try:
        body = get_news()
        openrouter = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        response = openrouter.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": "You are a helpful assistant that summarises news articles with an emphasis on the impact on markets.",
                },
                {
                    "role": "user",
                    "content": "Summarise the following news article in bullet points: "
                    + body,
                },
            ],
        )

        summary = response.choices[0].message.content

        # Display markdown output in the terminal
        print("\n\n\nGenerated Summary of News Articles:\n")
        console.print(Markdown(str(summary)))

        return str(summary)
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
