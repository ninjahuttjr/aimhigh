import requests
from bs4 import BeautifulSoup
import datetime

def get_current_datetime():
    """Returns the current date and time"""
    print("Getting current date and time.")
    return datetime.datetime.now().isoformat()

def browse_web(url: str):
    """Fetches the content of a webpage"""
    print(f"Fetching content from {url}.")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()  # Remove these two types of tags
    text = soup.get_text()[:10000]  # Limit the content to the first 4000 characters
    print("Fetched content successfully.")
    return text
