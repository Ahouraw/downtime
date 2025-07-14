import csv, requests


WEBSITES = [
    {"name": "google", "url": "https://www.google.com"},
    {"name": "facebook", "url": "https://www.facebook.com"},
    {"name": "twitter", "url": "https://www.twitter.com"},
    {"name": "github", "url": "https://www.github.com"},
    {"name": "linkedin", "url": "https://www.linkedin.com"},
    {"name": "reddit", "url": "https://www.reddit.com"},
    {"name": "RBC", "url": "https://www.rbcroyalbank.com"},

]

with open("websites.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["website_name", "url"])
    for website in WEBSITES:
        writer.writerow({"website_name": website["name"], "url": website["url"]})

# response = requests.get("https://www.rbcroyalbank.com")

#if response.status_code == 200:
#    print("Google is up and running!")