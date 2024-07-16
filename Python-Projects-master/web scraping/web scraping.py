import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://google.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract specific data from the webpage
title = soup.title.text.strip()
paragraphs = soup.find_all("p")

# Print the extracted data
print("Title:", title)
print("Paragraphs:")
for paragraph in paragraphs:
    print(paragraph.text.strip())
