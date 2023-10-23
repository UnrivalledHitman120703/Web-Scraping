# Web scraping using python
# Name = Indrajeet Mondal; Date = 24th October 2023
# SourceCode

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pprint

# Send HTTP GET requests to the first and second pages of Hacker News
res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")

# Parse the HTML content of the web pages using BeautifulSoup
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

# Select the elements containing news article titles and subtext on the first page
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")

# Select the elements containing news article titles and subtext on the second page
links2 = soup2.select(".titleline > a")
subtext2 = soup2.select(".subtext")

# Combine the links and subtext from both pages
mega_links = links + links2
mega_subtext = subtext + subtext2


# Function to sort the articles by the number of votes
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


# Function to create a custom list of Hacker News articles with more than 99 votes
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


# Pretty-print the custom list of articles sorted by votes
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
