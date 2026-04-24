import requests
from bs4 import BeautifulSoup

def fetch_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # remove noise
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        # clean up blank lines
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)[:8000]  # cap at 8000 chars to stay within token limits

    except Exception as e:
        return f"Error fetching URL: {str(e)}"