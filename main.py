import requests
from send_email import send_email

api = "e3a6226560c14664a3159f2201c0fd2f"
url = "https://newsapi.org/v2/everything?q=" \
      "tesla&from=2022-12-28&sortBy=" \
      "publishedAt&apiKey=e3a6226560c14664a3159f2201c0fd2f"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)




