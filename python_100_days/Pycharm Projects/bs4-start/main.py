from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

# This will get 2 links per article (one from the article, another from the source)
articles = soup.select(".title a")
# Remove the ones at odd positions to conserve only the links of the articles
articles = [articles[i] for i in range(len(articles)) if i % 2 == 0]

article_upvotes = soup.find_all(name="span", class_="score")

article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

article_upvotes = [int(upvotes.text.split()[0]) for upvotes in article_upvotes]

print(article_texts)
print(article_links)
print(article_upvotes)

most_upvoted_index = 0
max_votes = 0

for i in range(len(article_upvotes)):
    if article_upvotes[i] > max_votes:
        max_votes = article_upvotes[i]
        most_upvoted_index = i

most_upvoted_article_text = article_texts[most_upvoted_index]
most_upvoted_article_link = article_links[most_upvoted_index]
most_upvoted_article_upvotes = article_upvotes[most_upvoted_index]
print(most_upvoted_article_text)
print(most_upvoted_article_link)
print(most_upvoted_article_upvotes)

print(max_votes)





# contents: str
#
# with open("website.html") as f:
#     contents = f.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)  # Name of the title tag
# print(soup.title.string)

# print(soup.prettify())

# print(soup.li)  # Prints the first `li` tag

# anchor_tags = soup.find_all(name="a")  # Gives us a list of all the `a` tags in the website
# print(anchor_tags)
#
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))  # Gets the value of the `href` attribute

# heading = soup.find(name="h1", id="name")  # .find() finds the first tag, .find_all() finds all of them
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")  # Select the first anchor tag inside a paragraph tag
#                                                # (we use css selectors)
# print(company_url)
#
# name = soup.select_one(selector="#name")  # We can use any css selector to select the tags we want
# print(name)
#
# headings = soup.select(".heading")  # Gives a list with all tags with `heading` class
# print(headings)