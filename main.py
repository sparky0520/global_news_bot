import requests
from bs4 import BeautifulSoup


def get_news():
    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()
    else:
        return "Failed to retrieve news."


if __name__ == "__main__":
    news = get_news()
    print(news)
