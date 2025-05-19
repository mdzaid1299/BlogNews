import json
import requests
from bs4 import BeautifulSoup

def scrape_techcrunch():
    url = 'https://techcrunch.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    seen_links = set()  # Track unique article links

    for article in soup.find_all('div', class_='loop-card'):
        title_tag = article.find('h3', class_='loop-card__title')
        img_tag = article.find('img')
        link_tag = article.find('a', class_='loop-card__title-link')

        if title_tag and link_tag and img_tag:
            link = link_tag['href']
            if link not in seen_links:
                seen_links.add(link)
                articles.append({
                    "title": title_tag.text.strip(),
                    "link": link,
                    "image": img_tag['src']
                })

    with open('scraped_data.json', 'w') as f:
        json.dump(articles, f, indent=4)

    print(f'Scraped and saved {len(articles)} unique articles to scraped_data.json')

if __name__ == "__main__":
    scrape_techcrunch()
