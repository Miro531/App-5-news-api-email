import requests
from send_email import email_sender

topic = "tesla"

api_key = "79748206aadb465193751aa5e914a330"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2024-03-23&sortBy=publishedAt&" \
    "apiKey=79748206aadb465193751aa5e914a330&language=en"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the article titles and description
body = f"Subject: Today's news regarding {topic.capitalize()}" + "\n"
for article in content["articles"][0:20]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
email_sender(message=body)