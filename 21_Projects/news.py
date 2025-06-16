import requests

query=input("What type of news are you interested today...?")
api="api_key"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-11&sortBy=publishedAt&apiKey={api}"

r=requests.get(url)
data=r.json()
articles=data["articles"]
for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n**************************************************\n")