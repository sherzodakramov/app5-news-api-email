import requests

api = "e3a6226560c14664a3159f2201c0fd2f"
url = "https://newsapi.org/v2/everything?q=" \
      "tesla&from=2022-12-28&sortBy=" \
      "publishedAt&apiKey=e3a6226560c14664a3159f2201c0fd2f"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

