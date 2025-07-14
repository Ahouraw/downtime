import csv, requests


WEBSITES = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "Facebook", "url": "https://www.facebook.com"},
    {"name": "Twitter", "url": "https://www.twitter.com"},
    {"name": "Github", "url": "https://www.github.com"},
    {"name": "Linkedin", "url": "https://www.linkedin.com"},
    {"name": "Reddit", "url": "https://www.reddit.com"},
    {"name": "RBC", "url": "https://www.rbcroyalbank.com"},
    {"name": "TD", "url": "https://www.rbcroyalbank.com"},
    

]

with open("websites.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["website_name", "url"])
    writer.writeheader()
    for website in WEBSITES:
        writer.writerow({"website_name": website["name"], "url": website["url"]})

# response = requests.get("https://www.rbcroyalbank.com")

#if response.status_code == 200:
#    print("Google is up and running!")