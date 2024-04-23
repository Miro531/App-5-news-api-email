import requests
from send_email import email_sender

api_key = "79748206aadb465193751aa5e914a330"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-03-23&sortBy=publishedAt&apiKey=" \
      "79748206aadb465193751aa5e914a330"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_sender(message=body)